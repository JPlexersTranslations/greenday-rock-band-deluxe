import sys
sys.path.append("../dependencies/dev_scripts")

from download_mackiloha import download_mackiloha
from build_ark import build_patch_ark

# Download and extract Mackiloha-suite-archive.zip
if not download_mackiloha():
    print("Failed to download and extract Mackiloha-suite-archive.zip. Exiting.")
    sys.exit(1)

if build_patch_ark(True, rpcs3_mode=False):
    print("Xbox ARK built successfully.")
    print("You may find the files needed to place on your Xbox 360 in /_build/Xbox/.")
else:
    print("Error building Xbox ARK. Check your modifications or run git_reset.py to rebase your repo.")
