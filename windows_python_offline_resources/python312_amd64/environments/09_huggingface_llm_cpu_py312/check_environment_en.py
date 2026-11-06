"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "torch",
  "2.13.0",
  "torch"
 ],
 [
  "transformers",
  "5.14.1",
  "transformers"
 ],
 [
  "datasets",
  "5.0.1",
  "datasets"
 ],
 [
  "tokenizers",
  "0.22.2",
  "tokenizers"
 ],
 [
  "accelerate",
  "1.14.0",
  "accelerate"
 ],
 [
  "sentencepiece",
  "0.2.2",
  "sentencepiece"
 ],
 [
  "safetensors",
  "0.8.0",
  "safetensors"
 ],
 [
  "peft",
  "0.20.0",
  "peft"
 ],
 [
  "evaluate",
  "0.4.6",
  "evaluate"
 ],
 [
  "huggingface-hub",
  "1.26.0",
  "huggingface_hub"
 ]
]

def main():
    bad = 0
    print("python", sys.version.split()[0], "(expected 3.12.10)")
    for dist, version, module in EXPECTED:
        try:
            got = md.version(dist)
        except md.PackageNotFoundError:
            print(f"MISSING  {dist}"); bad += 1; continue
        status = "OK" if got == version else "VERSION"
        if module:
            try:
                importlib.import_module(module)
            except Exception as e:
                status = f"IMPORT-ERROR {type(e).__name__}: {e}"
        if status != "OK":
            bad += 1
        print(f"{status:8} {dist}=={got} (lock {version})" + (f" import {module}" if module else ""))
    print("result:", "all ok" if not bad else f"{bad} problem(s)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
