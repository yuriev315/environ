"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "pytest",
  "9.1.1",
  "pytest"
 ],
 [
  "black",
  "26.5.1",
  null
 ],
 [
  "ruff",
  "0.16.1",
  null
 ],
 [
  "mypy",
  "2.3.0",
  null
 ],
 [
  "pre-commit",
  "4.6.1",
  null
 ],
 [
  "ipython",
  "9.16.0",
  "IPython"
 ],
 [
  "pylint",
  "4.0.6",
  null
 ],
 [
  "isort",
  "8.0.1",
  null
 ],
 [
  "flake8",
  "7.3.0",
  null
 ],
 [
  "pyinstaller",
  "6.21.0",
  null
 ],
 [
  "build",
  "1.5.0",
  null
 ],
 [
  "twine",
  "7.0.0",
  null
 ],
 [
  "setuptools",
  "83.0.0",
  "setuptools"
 ],
 [
  "wheel",
  "0.47.0",
  "wheel"
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
