# Green Day: Rock Band Deluxe

![Header Image](dependencies/header.png)

## Introduction

This Repo contains everything you need to build an ark for Green Day: Rock Band Deluxe for Xbox 360.

## Features

### Quality of Life
* No strum limit executable modification
* Fast start executable modification
* Additional intro skip scripting to skip the intro movie
* "Overshell" - a custom on-screen menu system for changing speeds. Opened by pressing `SELECT, SELECT` on most menu screens
* Full Combo indicator per instrument via the multiplier
* Bass streak effect from RB3/RB4 available on all instruments
* Selectable song speed and track speed by 5% increments
* Selectable venue framerate up to 60fps
* Manual calibration adjusts by 1ms instad of 5ms

### Additional Modifications
* Nice (69%) and Awesome Choke (98-99%) callouts on solo completion

## Install

NOTE: You WILL need a modded/hacked console to play this mod on console. I hope this is clear

### Repo Setup

Setting up the Green Day: Rock Band Deluxe repo for the first time is meant to be as easy as possible.
As well, it is designed to allow you to automatically receive updates as the repo is updated.

Simply go to the Releases of this repo and grab all three files. (two .exe, one .bat)

The two exe's are a couple dependencies, [Git for Windows](https://gitforwindows.org/), and [Dot Net 6.0 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime).
Git is required for you to take advantage of auto updating via github pulls. Dot Net is required to build an ARK file, the archive format the game needs to run.
You can setup git with all default options, same with dot net.

Once the dependencies are installed, run `_init_repo.bat` in an **empty folder**. git will pull the repo and make sure you are completely up to date.

### Build Xbox

Copy your base game Green Day: Rock Band main_xbox.hdr and ark files to `_build/Xbox/gen`.

From then on simply run `_build_xbox.bat`. This script will pull the repo again for updates, and build the ARK for you and spit it out in `_build/Xbox`

Then copy the gen folder and the xex from `_build/xbox/` to the location you have installed Green Day: Rock Band. Subsequent copies only require `main_xbox.hdr` and `main_xbox_10.ark` from `_build/Xbox/gen` to be copied

Make sure you clear your system cache.

To clear system cache, navigate to Storage, and press Y to clear the system cache.

If installing for the first time, make sure you rename the vanilla `default.xex` to `default_vanilla.xex` before copying for safety.

Run the build script again to pull any new updates committed to the repo and rebuild a new ark.

### Build PS3

Simply run `_build_ps3.bat`. This script will pull the repo again for updates, and build the ARK for you and spit it out in `_build/ps3`.

Then copy all of the contents of `_build/ps3` to an extracted Green Day: Rock Band disc folder labelled `PS3_GAME`.

If installing for the first time, make sure you rename the vanilla `EBOOT.BIN` to `EBOOT_VANILLA.BIN` before copying for safety.

Run the build script again to pull any new updates committed to the repo and rebuild a new ark.

## Included Dependencies

[Git for Windows](https://gitforwindows.org/) - CLI application to allow auto updating gdrbdx repo files

[Dot Net 6.0 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime) - Needed to run ArkHelper

[Mackiloha](https://github.com/PikminGuts92/Mackiloha) - ArkHelper for building Green Day: Rock Band ARK - Superfreq for editing milo files

[dtab](https://github.com/mtolly/dtab) - For serializing Rock Band dtb files
