"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "cvxpy",
  "1.9.2",
  "cvxpy"
 ],
 [
  "pulp",
  "3.3.2",
  "pulp"
 ],
 [
  "casadi",
  "3.7.2",
  "casadi"
 ],
 [
  "control",
  "0.10.2",
  "control"
 ],
 [
  "pyomo",
  "6.10.1",
  "pyomo"
 ],
 [
  "scipy",
  "1.18.0",
  "scipy"
 ],
 [
  "numpy",
  "2.4.6",
  "numpy"
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
