# Path of the Bloodied One

Version 2.1.0.

Agraphon Studios.

## Run

1. Install Python 3.11+.
2. Run `python -m pip install -e .`.
3. Run `python main.py`.

Developer/test shortcuts are enabled by default when running the source tree. Set `PATH_BLOODIED_DEV=0` to disable them. Saves, settings, and crash logs are stored in the operating system's per-user application-data directory.

## Controls and accessibility

Keyboard bindings remain rebindable. A controller action layer supports movement, confirm/back, attack, block, dash, interact, inventory, quick-use, save, and pause. Settings include fullscreen/borderless/windowed display modes, camera-shake intensity, flash intensity, color-accessibility palettes, hold/toggle block input, reduced motion, and instant dialogue text.

The Load Game screen supports more than seven saves, save metadata, corrupt-save detection, and `.bak` recovery when available. Save files are stamped with schema/build metadata.

## Test controls

Development shortcuts: Ctrl+1..4 grants test spells; Ctrl+U grants coin; Ctrl+I grants levels; Ctrl+O grants alchemy consumables; Ctrl+P unlocks all abilities; Ctrl+" toggles the test panel.

## Release builds

`build_windows.bat` and `build_unix.sh` force `PATH_BLOODIED_DEV=0`, install the package plus PyInstaller, and build with `PathOfTheBloodiedOne.spec`.
