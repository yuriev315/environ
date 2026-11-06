"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "openpyxl",
  "3.1.5",
  "openpyxl"
 ],
 [
  "python-docx",
  "1.2.0",
  "docx"
 ],
 [
  "python-pptx",
  "1.0.2",
  "pptx"
 ],
 [
  "pypdf",
  "6.14.2",
  "pypdf"
 ],
 [
  "pdfplumber",
  "0.11.9",
  "pdfplumber"
 ],
 [
  "reportlab",
  "5.0.0",
  "reportlab"
 ],
 [
  "xlsxwriter",
  "3.2.9",
  "xlsxwriter"
 ],
 [
  "pymupdf",
  "1.28.0",
  "pymupdf"
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
