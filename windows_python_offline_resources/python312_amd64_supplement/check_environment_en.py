"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "akshare",
  "1.18.88",
  "akshare"
 ],
 [
  "lime",
  "0.2.0.1",
  "lime"
 ],
 [
  "ta",
  "0.11.0",
  "ta"
 ],
 [
  "jieba",
  "0.42.1",
  "jieba"
 ],
 [
  "odfpy",
  "1.4.1",
  "odfpy"
 ],
 [
  "numpy",
  "2.4.6",
  "numpy"
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
  "matplotlib",
  "3.11.1",
  "matplotlib"
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
