# Educational "semantic" sealing: zlib + XOR keystream (SHA-256) + HMAC-SHA256
# ⚠️ Not production-grade crypto. Use audited libs (AES-GCM/ChaCha20-Poly1305) for real security.
import os, json, zlib, base64, hmac, hashlib, struct
from typing import Tuple, Optional

def _kdf(passphrase: str, nonce: bytes) -> bytes:
    return hashlib.sha256(passphrase.encode("utf-8") + nonce).digest()

def _keystream(key: bytes, length: int) -> bytes:
    out = bytearray()
    counter = 0
    while len(out) < length:
        block = hashlib.sha256(key + struct.pack(">Q", counter)).digest()
        out.extend(block)
        counter += 1
    return bytes(out[:length])

def _xor(data: bytes, ks: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(data, ks))

def _hmac(key: bytes, data: bytes) -> bytes:
    return hmac.new(key, data, hashlib.sha256).digest()

def seal(obj, passphrase: str, nonce: Optional[bytes]=None) -> str:
    raw = json.dumps(obj, separators=(",",":")).encode("utf-8")
    comp = zlib.compress(raw, level=9)
    nonce = nonce or os.urandom(16)
    key = _kdf(passphrase, nonce)
    ks = _keystream(key, len(comp))
    ct = _xor(comp, ks)
    tag = _hmac(key, nonce + ct)
    blob = b"Z5::" + base64.b64encode(nonce + ct + tag)
    return blob.decode("ascii")

def open_sealed(blob: str, passphrase: str) -> dict:
    assert blob.startswith("Z5::")
    data = base64.b64decode(blob[4:])
    nonce, rest = data[:16], data[16:]
    ct, tag = rest[:-32], rest[-32:]
    key = _kdf(passphrase, nonce)
    exp = _hmac(key, nonce + ct)
    if not hmac.compare_digest(exp, tag):
        raise ValueError("HMAC verification failed (tampered or wrong key)")
    ks = _keystream(key, len(ct))
    comp = _xor(ct, ks)
    raw = zlib.decompress(comp)
    return json.loads(raw.decode("utf-8"))

def verify(blob: str, passphrase: str) -> bool:
    try:
        open_sealed(blob, passphrase)
        return True
    except Exception:
        return False
