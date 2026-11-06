"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
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
  "scikit-learn",
  "1.7.2",
  "sklearn"
 ],
 [
  "statsmodels",
  "0.14.6",
  "statsmodels"
 ],
 [
  "xgboost",
  "3.2.0",
  "xgboost"
 ],
 [
  "lightgbm",
  "4.7.0",
  "lightgbm"
 ],
 [
  "catboost",
  "1.2.10",
  "catboost"
 ],
 [
  "imbalanced-learn",
  "0.14.2",
  "imblearn"
 ],
 [
  "joblib",
  "1.5.3",
  "joblib"
 ],
 [
  "matplotlib",
  "3.10.9",
  "matplotlib"
 ],
 [
  "seaborn",
  "0.13.2",
  "seaborn"
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
