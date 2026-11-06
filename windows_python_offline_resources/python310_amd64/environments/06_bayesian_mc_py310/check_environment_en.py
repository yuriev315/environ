"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "pymc",
  "5.25.1",
  "pymc"
 ],
 [
  "arviz",
  "0.23.4",
  "arviz"
 ],
 [
  "emcee",
  "3.1.6",
  "emcee"
 ],
 [
  "corner",
  "2.3.0",
  "corner"
 ],
 [
  "numpy",
  "2.2.6",
  "numpy"
 ],
 [
  "scipy",
  "1.15.3",
  "scipy"
 ],
 [
  "pandas",
  "2.3.3",
  "pandas"
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
