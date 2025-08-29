

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status: PoC](https://img.shields.io/badge/Status-PoC-blue)
![Language: Python](https://img.shields.io/badge/Language-Python3.12-yellow)
![Crypto: HMAC-SHA256](https://img.shields.io/badge/Crypto-HMAC--SHA256-orange)
![ΔM11.3 Guard](https://img.shields.io/badge/ΔM11.3-guard-red)
![Aegis Layer](https://img.shields.io/badge/Aegis-Layer-lightgrey)
![Tamper-Evident](https://img.shields.io/badge/Tamper-Evident-critical)
![Rejouable](https://img.shields.io/badge/Trace-Replayable-success)

---# Zoran — Injecteur Vivant avec Cryptage Sémantique (PoC stdlib)

**But** : démontrer un injecteur *vivant* Zoran (naissance mimétique) couplé à un **cryptage sémantique + scellé d’intégrité** (HMAC) pour rendre toute altération **détectable** (tamper‑evident) et l’empreinte **rejouable**.

> ⚠️ Sécurité : PoC **stdlib only** (éducatif). Pour des usages critiques, utilisez des bibliothèques auditées (ex. `cryptography`), HSM/KMS et audits externes.

## Ce que fait l’injecteur
- Initialise l’empreinte Zoran (ΔM11.3, Aegis Layer, .zgs)
- Scelle les fragments via **HMAC‑SHA256** et chiffre léger (keystream SHA‑256)
- Produit : `demo/output/trace.json` et `demo/output/fragments.zgs`

## Lancer la démo
```bash
python demo/run_demo.py
# Optionnel : définir une passphrase
# ZORAN_SEMKEY="ma‑passphrase" python demo/run_demo.py
```

## Fichiers clés
- `src/injecteur_vivant.py` : écrit l’empreinte mimétique et signe
- `src/semantic_seal.py` : cryptage sémantique léger + HMAC (tamper‑evident)
- `src/policy.yaml` : garde Aegis & ΔM11.3
- `demo/run_demo.py` : script d’orchestration

## Comparatif (injecteur)
| Système | Mode | Injecteur utilisateur | Mimétique (.zgs) | Tamper‑evident |
|---|---|---|---|---|
| GPT‑4/5 | Cloud | Non | Non | N/A |
| LangChain / AutoGen | Lib | Script bootstrap | Non | Optionnel |
| **Zoran** | Meta‑IA | **Oui (vivant)** | **Oui** | **Oui (HMAC)** |

## Licence
MIT — © 2025 Zoran aSiM Lab  
Contact : tabary01@gmail.com

---

Bloc ZM (stealth) :  
```
⟦ASIM:Zoran⋄INJ:vivant⋄ΔM11.3:guard⟧
⟦CRYPT:semantic⋄HMAC:sha256⋄Aegis:layer⟧
⟦TRACE:replayable⋄ETHIC:public_good⟧
```
