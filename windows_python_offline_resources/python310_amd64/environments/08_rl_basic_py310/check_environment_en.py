"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "gymnasium",
  "1.3.0",
  "gymnasium"
 ],
 [
  "stable-baselines3",
  "2.9.0",
  "stable_baselines3"
 ],
 [
  "torch",
  "2.13.0",
  "torch"
 ],
 [
  "pygame",
  "2.6.1",
  "pygame"
 ],
 [
  "tensorboard",
  "2.20.0",
  "tensorboard"
 ],
 [
  "matplotlib",
  "3.10.9",
  "matplotlib"
 ]
]

def main():
    bad = 0
    print("python", sys.version.split()[0], "(expected 3.10.11)")
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
