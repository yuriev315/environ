"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "pingouin",
  "0.6.1",
  "pingouin"
 ],
 [
  "lifelines",
  "0.30.0",
  "lifelines"
 ],
 [
  "scikit-optimize",
  "0.10.2",
  "skopt"
 ],
 [
  "hyperopt",
  "0.3.0",
  "hyperopt"
 ],
 [
  "optuna",
  "4.9.0",
  "optuna"
 ],
 [
  "statsmodels",
  "0.14.6",
  "statsmodels"
 ],
 [
  "linearmodels",
  "7.0",
  "linearmodels"
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
