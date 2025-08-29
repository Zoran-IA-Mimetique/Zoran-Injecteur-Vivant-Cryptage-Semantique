from pathlib import Path
from src.injecteur_vivant import run

if __name__ == "__main__":
    out = Path("demo/output")
    trace = run(out)
    print("Trace:", trace)
    print("OK — fragments.zgs et trace.json générés dans", out)
