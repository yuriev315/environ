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
  "matplotlib",
  "3.10.9",
  "matplotlib"
 ],
 [
  "seaborn",
  "0.13.2",
  "seaborn"
 ],
 [
  "sympy",
  "1.14.0",
  "sympy"
 ],
 [
  "jupyterlab",
  "4.6.2",
  "jupyterlab"
 ],
 [
  "ipykernel",
  "7.3.0",
  "ipykernel"
 ],
 [
  "ipywidgets",
  "8.1.8",
  "ipywidgets"
 ],
 [
  "openpyxl",
  "3.1.5",
  "openpyxl"
 ],
 [
  "xlrd",
  "2.0.2",
  "xlrd"
 ],
 [
  "tqdm",
  "4.70.0",
  "tqdm"
 ],
 [
  "requests",
  "2.34.2",
  "requests"
 ],
 [
  "pyyaml",
  "6.0.3",
  "yaml"
 ],
 [
  "h5py",
  "3.16.0",
  "h5py"
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
