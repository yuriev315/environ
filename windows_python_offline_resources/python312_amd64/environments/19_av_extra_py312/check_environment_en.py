"""Check that the packages of this environment import and report the expected versions."""
import importlib, importlib.metadata as md, sys

EXPECTED = [
 [
  "moviepy",
  "2.2.1",
  "moviepy"
 ],
 [
  "imageio-ffmpeg",
  "0.6.0",
  "imageio_ffmpeg"
 ],
 [
  "pydub",
  "0.25.1",
  "pydub"
 ],
 [
  "sounddevice",
  "0.5.5",
  "sounddevice"
 ],
 [
  "av",
  "18.0.0",
  "av"
 ],
 [
  "numpy",
  "2.4.6",
  "numpy"
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
