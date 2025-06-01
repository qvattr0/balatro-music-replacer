import subprocess
import os
import urllib.request
import shutil
import sys
import platform
from sys import exit

def look_for_balatro_windows() -> str:
    # check if a path file exists
    if os.path.isfile("gamepath.txt"):
        with open("gamepath.txt", "r") as file:
            path = file.read()
            return os.path.realpath(path)

    path = "C:/Program Files (x86)/Steam/steamapps/common/Balatro/Balatro.exe"
    does_balatro_exist = os.path.isfile(path)
    if does_balatro_exist:
        print("Balatro found! " + path)
    else: print("Balatro not found in default path!")
    
    while not does_balatro_exist:
        path = input("Enter the file path of Balatro (including /Balatro.exe at the end): ")
        path = path.removeprefix("\"").removesuffix("\"")

        does_balatro_exist = os.path.isfile(path)
        if does_balatro_exist:
            print("Balatro found! " + path)
            print("> Saving the path to gamepath.txt for future use...")

            with open("gamepath.txt", "w", encoding="utf-8") as f:
                f.write(path)
            
            print("Done!")
        else:
            print("Balatro not found in the path you entered!")

    return os.path.realpath(path)

def look_for_balatro_macos() -> str:
        # check if a path file exists
    if os.path.isfile("gamepath.txt"):
        with open("gamepath.txt", "r") as file:
            path = file.read()
            return os.path.realpath(path)
        
    home_dir = os.path.expanduser("~")
    relative_path = "Library/Application Support/Steam/steamapps/common/Balatro/Balatro.app"
    path = os.path.join(home_dir, relative_path)
    does_balatro_exist = os.path.exists(path) and os.path.isdir(path)
    if does_balatro_exist:
        print("Balatro found! " + path)
    else:
        print("Balatro not found in default path!")
    while not does_balatro_exist:
        path = input("Enter the file path of Balatro (including /Balatro.app at the end): ")
        path = path.removeprefix("\"").removesuffix("\"")

        does_balatro_exist = os.path.exists(path) and os.path.isdir(path)
        if does_balatro_exist:
            print("Balatro found! " + path)
            print("> Saving the path to gamepath.txt for future use...")

            with open("gamepath.txt", "w", encoding="utf-8") as f:
                f.write(path)
            
            print("Done!")
        else:
            print("Balatro not found in the path you entered!")

    path = os.path.join(path, "Contents/Resources/Balatro.love")
    if not os.path.isfile(path):
        print("Balatro directory corrupted")
        return ""
    return os.path.realpath(path)


def check_7zip():
    sevenzip_download = "https://www.7-zip.org/a/7z1900-x64.exe"
    sevenzip_path = r"C:\Program Files\7-Zip\7z.exe"
    
    if os.path.exists(sevenzip_path):
        print("7zip found!")
    else:
        print("7zip not found! Installing 7zip...")
        # Download 7zip installer
        urllib.request.urlretrieve(sevenzip_download, "7zip.exe")
        sevenzip_installer = os.path.realpath("7zip.exe")

        print("We will now open the 7zip installer. You will be asked for admin permissions.")
        input("Press Enter to continue...")
        print("Installing 7zip...")
        try:
            subprocess.run(
                [
		    "powershell",
                    "-Command",
                    f"Start-Process '{sevenzip_installer}' -ArgumentList '/S /D=\"{sevenzip_path.removesuffix('7z.exe')}\"'"
                ],
                check=True
            )

            # hold until the installer is done
            while not os.path.exists(sevenzip_path):
                pass


        except Exception as e:
            print(e)
            print("Failed to install 7zip! Install 7zip manually from the 7zip.exe file in this folder.")
            print("Press any key to exit...")
            input()
            exit(1)

        print("7zip installed!")
        # Clean up the installer
        if os.path.exists("7zip.exe"):
            try:
                os.remove("7zip.exe")
                print("Installer removed.")
            except Exception as e:
               print("Failed to remove 7zip installer. Please remove it manually.")

def main():
    os_platform = platform.system()
    path = ""
    print(chr(27) + "[2J")

    print("Balatro Music Multipatcher")
    print("**************************")
    if platform.system() == "Darwin":
        # make this fix for macos as there are weird issues with the working directory
        path = os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1])
        os.chdir(path)


    if os_platform == "Windows":
        check_7zip()
        path = look_for_balatro_windows()
        check_7zip()
    elif os_platform == "Darwin":
        path = look_for_balatro_macos()

    if path == "":
        print("Failed to find path to Balatro!")
        print("Press any key to exit...")
        input()
        return


    # find all the installed music packs in resources and store their names
    packs = [name for name in os.listdir('./packs') if os.path.isdir(name)]

    # check if the packs folder is empty
    # TODO: test this feature
    if not packs:
        print("No music packs detected! Please place your pack inside the `packs/` folder while following this folder structure: ")
        print("soundpack_name/\n├── music1.ogg\n├── music2.ogg\n├── music3.ogg\n├── music4.ogg\n└── music5.ogg")

    # print all the options and let the user choose
    print("Available Music Packs:")
    print("----------------------")

    for i, pack in enumerate (packs, start=1):
        print(f"[{i}] {pack}")

    # checking for option validity
    while True:
        try:
            selection = int(input(f"Select a music pack to patch: (1-{len(packs)})"))
            if 0 < selection <= len(packs):
                break
            else:
                print("Invalid selection, pack index does not exist. Please try again.")
        except ValueError:
            print("That's not a valid number. Try again.")

    # open music folder read files
    music_folder = os.path.join(os.getcwd(), 'packs', packs[selection])
    music_files = os.listdir(music_folder)
    sevenzip_path = "C:/Program Files/7-Zip/7z.exe"


    # apparently this works on extracting select music files too, great implementation!
    # extract the original music if not done so already
    if os.path.exists("./packs/Original OST/") is False:
        print("Extracting Balatro.exe's original music...")
        os.makedirs("packs/Original OST", exist_ok=True)
        for file in music_files:
            print("Extracting " + file + "...")
            if os_platform == "Windows":
                process = subprocess.Popen([sevenzip_path, "e", path, f"resources/sounds/{file}", "-o" + "./packs/Original OST"])
            elif os_platform == "Darwin":
                process = subprocess.Popen(["unzip", path, f"resources/sounds/{file}", "-d" + "original/"])
            else:
                print("Unsupported OS")
                print("Press any key to exit...")
                input()
                exit(1)

            process.wait()

    # after the extraction is complete, begin replacement
    for file in music_files:
        print("Replacing " + file + "...")
        if os_platform == "Windows":
            process = subprocess.Popen([sevenzip_path, "u", path, f"resources/sounds/{file}"])
        elif os_platform == "Darwin":
            process = subprocess.Popen(["zip", path, f"resources/sounds/{file}"])
        else:
            print("Unsupported OS")
            print("Press any key to exit...")
            input()
            exit(1)

        process.wait()

    print(chr(27) + "[2J")
    print("Music files replaced! Enjoy your new music!")
    print("Press any key to exit...")
    input()
    exit(0)

if __name__ == "__main__":
    main()