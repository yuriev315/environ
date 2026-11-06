"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "numba",
  "0.66.0",
  "numba"
 ],
 [
  "xarray",
  "2025.6.1",
  "xarray"
 ],
 [
  "netcdf4",
  "1.7.4",
  "netCDF4"
 ],
 [
  "dask",
  "2026.7.1",
  "dask"
 ],
 [
  "polars",
  "1.43.2",
  "polars"
 ],
 [
  "pyarrow",
  "25.0.0",
  "pyarrow"
 ],
 [
  "networkx",
  "3.4.2",
  "networkx"
 ],
 [
  "sympy",
  "1.14.0",
  "sympy"
 ],
 [
  "astropy",
  "6.1.7",
  "astropy"
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
