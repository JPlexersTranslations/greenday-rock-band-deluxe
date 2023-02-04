git pull https://github.com/hmxmilohax/greenday-rock-band-deluxe main
@echo off
echo:Make sure your vanilla ark files are in _build/ps3/USRDIR/gen/
del "%~dp0\_build\ps3\USRDIR\gen\main_ps3.hdr"
del "%~dp0\_build\ps3\USRDIR\gen\main_ps3_10.ark"
xcopy "%~dp0\_build\_rebuild_files\main_ps3.hdr" "%~dp0\_build\ps3\USRDIR\gen" >nul
echo:
echo:Temporarily moving Xbox files out of the ark path to reduce final ARK size
@%SystemRoot%\System32\robocopy.exe "%~dp0_ark" "%~dp0_temp\_ark" *.milo_xbox /S /MOVE /XD "%~dp0_temp\_ark" /NDL /NFL /NJH /NJS /R:0 >nul
@%SystemRoot%\System32\robocopy.exe "%~dp0_ark" "%~dp0_temp\_ark" *.png_xbox /S /MOVE /XD "%~dp0_temp\_ark" /NDL /NFL /NJH /NJS /R:0 >nul
@%SystemRoot%\System32\robocopy.exe "%~dp0_ark" "%~dp0_temp\_ark" *.bmp_xbox /S /MOVE /XD "%~dp0_temp\_ark" /NDL /NFL /NJH /NJS /R:0 >nul
echo:
echo:Building PS3 ARK
echo:The "Unhandled exception" below is expected, and does not indicate failure.
"%~dp0dependencies/arkhelper" patchcreator -a "%~dp0_ark" -o "%~dp0_build\ps3\USRDIR" "%~dp0_build\ps3\USRDIR\gen\main_ps3.hdr" >nul
echo:
echo:Moving back Xbox files
@%SystemRoot%\System32\robocopy.exe "%~dp0_temp\_ark" "%~dp0_ark" *.milo_xbox /S /MOVE /XD "%~dp0_ark" /NDL /NFL /NJH /NJS /R:0 >nul
@%SystemRoot%\System32\robocopy.exe "%~dp0_temp\_ark" "%~dp0_ark" *.png_xbox /S /MOVE /XD "%~dp0_ark" /NDL /NFL /NJH /NJS /R:0 >nul
@%SystemRoot%\System32\robocopy.exe "%~dp0_temp\_ark" "%~dp0_ark" *.bmp_xbox /S /MOVE /XD "%~dp0_ark" /NDL /NFL /NJH /NJS /R:0 >nul
rd _temp
echo:
echo:Successfully built Green Day Rock Band Deluxe ARK. You may find the files needed to place on your PS3 in /_build/PS3/
echo:
pause