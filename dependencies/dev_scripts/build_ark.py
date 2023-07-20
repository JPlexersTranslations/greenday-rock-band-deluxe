# build_ark.py
from pathlib import Path
from subprocess import CalledProcessError
from sys import platform
import subprocess
from check_git_updated import check_git_updated
import os

def rm_tree(pth):
    pth = Path(pth)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()

def make_executable_binaries():
    # Make the binaries executable if on a non-Windows platform
    if platform != "win32":
        try:
            cmd_chmod_arkhelper = ["chmod", "+x", "dependencies/linux/arkhelper"]
            subprocess.check_output(cmd_chmod_arkhelper, cwd="..")
        except subprocess.CalledProcessError:
            print("Failed to make arkhelper executable.")
            sys.exit(1)

        try:
            cmd_chmod_dtab = ["chmod", "+x", "dependencies/linux/dtab"]
            subprocess.check_output(cmd_chmod_dtab, cwd="..")
        except subprocess.CalledProcessError:
            print("Failed to make dtab executable.")
            sys.exit(1)

# darwin: mac

# if xbox is true, build the Xbox ARK
# else, build the PS3 ARK
def build_patch_ark(xbox: bool, rpcs3_directory: str = None, rpcs3_mode: bool = False):
    # directories used in this script
    print("Building Green Day: Rock Band Deluxe patch arks...")
    cwd = Path().absolute() # current working directory (dev_scripts)
    root_dir = cwd.parents[0] # root directory of the repo
    ark_dir = root_dir.joinpath("_ark")

    files_to_remove = "*_ps3" if xbox else "*_xbox"
    if rpcs3_mode:
        if platform == "win32":
            build_location = rpcs3_directory + "\\game\\BLUS30350\\USRDIR\\gen"
        else:
            build_location = rpcs3_directory + "/game/BLUS30350/USRDIR/gen"
    else:
        if platform == "win32":
            build_location = "_build\\xbox\gen" if xbox else "_build\ps3\\USRDIR\gen"
        else:
            build_location = "_build/xbox/gen" if xbox else "_build/ps3/USRDIR/gen"

        # build the binaries if on linux/other OS
        if platform != "darwin":
            make_executable_binaries()
    patch_hdr_version = "patch_xbox" if xbox else "patch_ps3"

    # pull the latest changes from the Green Day: Rock Band Deluxe repo if necessary
    if not check_git_updated(repo_url="https://github.com/hmxmilohax/greenday-rock-band-deluxe", repo_root_path=root_dir):
        cmd_pull = "git pull https://github.com/hmxmilohax/greenday-rock-band-deluxe main".split()
        subprocess.run(cmd_pull, shell=(platform == "win32"), cwd="..")

    # temporarily move other console's files out of the ark to reduce overall size
    for f in ark_dir.rglob(files_to_remove):
        temp_path = str(f).replace(f"{str(root_dir)}\\", "").replace(f"{str(root_dir)}/","")
        # print(temp_path)
        the_new_filename = root_dir.joinpath("_tmp").joinpath(temp_path)
        the_new_filename.parent.mkdir(parents=True, exist_ok=True)
        # print(f"moving file {temp_path} to {the_new_filename}")
        f.rename(the_new_filename)

    # build the ark
    failed = False
    try:
        if platform == "win32":
            cmd_build = f"dependencies\windows\\arkhelper.exe dir2ark _ark {build_location} -n {patch_hdr_version} -e -v 5".split()
        elif platform == "darwin":
            cmd_build = f"dependencies/macos/arkhelper dir2ark _ark {build_location} -n {patch_hdr_version} -e -v 5".split()
        else:
            cmd_build = f"dependencies/linux/arkhelper dir2ark _ark {build_location} -n {patch_hdr_version} -e -v 5".split()
        subprocess.check_output(cmd_build, shell=(platform == "win32"), cwd="..")
    except CalledProcessError as e:
        print(e.output)
        failed = True

    # move the other console's files back
    for g in root_dir.joinpath("_tmp").rglob(files_to_remove):
        final_path = str(g).replace(f"{str(root_dir)}\\_tmp\\", "").replace(f"{str(root_dir)}/_tmp/","")
        # print(final_path)
        g.rename(root_dir.joinpath(final_path))

    # remove temp directory
    if os.path.exists(root_dir.joinpath("_tmp")):
        rm_tree(root_dir.joinpath("_tmp"))

    if not failed:
        print("Successfully built Green Day: Rock Band Deluxe ARK.")
        return True
    else:
        print("Error building ARK. Check your modifications or run git_reset.py to rebase your repo.")
        return False