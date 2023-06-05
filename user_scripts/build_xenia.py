import sys
import subprocess
sys.path.append("../dependencies/dev_scripts")
from build_ark import build_patch_ark

if build_patch_ark(True):
    print("Ready to run Green Day Rock Band Deluxe in Xenia.")
    cmd_xenia = "_xenia\\xenia_canary.exe _build\\xbox\\default.xex"
    subprocess.run(cmd_xenia, shell=True, cwd="..")