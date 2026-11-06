"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "opencv-python",
  "5.0.0.93",
  "cv2"
 ],
 [
  "albumentations",
  "2.0.8",
  "albumentations"
 ],
 [
  "scikit-image",
  "0.26.0",
  "skimage"
 ],
 [
  "imageio",
  "2.37.4",
  "imageio"
 ],
 [
  "pillow",
  "11.3.0",
  "PIL"
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
