"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "numpy",
  "2.4.6",
  "numpy"
 ],
 [
  "scipy",
  "1.18.0",
  "scipy"
 ],
 [
  "pywavelets",
  "1.9.0",
  "pywt"
 ],
 [
  "scikit-image",
  "0.26.0",
  "skimage"
 ],
 [
  "opencv-python-headless",
  "5.0.0.93",
  "cv2"
 ],
 [
  "pillow",
  "11.3.0",
  "PIL"
 ],
 [
  "librosa",
  "0.11.0",
  "librosa"
 ],
 [
  "soundfile",
  "0.14.0",
  "soundfile"
 ],
 [
  "imageio",
  "2.37.4",
  "imageio"
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
