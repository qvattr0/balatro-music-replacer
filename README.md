![Banner](assets/banner_balatro-music-replacer.jpg)
# Balatro Music Replacer

A simple program for patching custom music into Balatro. Supports storing
different soundpacks and switching between them on-demand. The soundpacks are stored in the `packs/` folder with the following structure:
```
soundpack_name/
├── music1.ogg
├── music2.ogg
├── music3.ogg
├── music4.ogg
└── music5.ogg
```

You can also have a folder with *only specific* music files that you'd like to
replace. Note that the application creates a temporary directory in the folder.

> [!IMPORTANT]
> This program does not work properly on macOS. I will add macOS functionality sometime soon, so hold off on using it on macOS for now.

On Windows, this program uses 7zip to replace in-game files with the custom music.
If 7zip is not installed, the program will download it for you, but it is
recommended to install it yourself. [here](https://www.7-zip.org/)

[Latest Release](https://github.com/qvattr0/balatro-music-multipatcher/releases/latest)

## Music Packs
For your convenience, I've compiled a list of all the music replacement packs I've come across. If you know of more, please let me know!

1. [Bonne Soirée](https://youtu.be/KiIXRr_GGCw) by Vongola
2. [Monkey Business](https://youtu.be/V3ps8wvrmxw) by Bombaflex
3. [Balatro: B-side](https://youtu.be/_u8tHrRMNG8) by Afterlight
4. [Raise The Stakes](https://youtu.be/p6TGmmQ_Fj4) by JohnathanSucks
5. [Cardsauce](https://youtu.be/Swe_WOWdaqQ) by Bassclefff
6. [Going in Blind](https://youtu.be/oRoLuU3vA8E) by Recycled Scraps

### Partial Music Packs
The program also allows you to replace parts of the soundtrack instead of all
the files. Just put in the specific music files you'd like to have replaced in
the dedicated music pack folder, and you're good to go!
1. [Main Theme Lo-Fi Mix](https://youtu.be/lGqeOnB0Vjg?list=PLuijNdiAVrbY19dl9MrjWfR12EJ6UgVUh) by VRIME
2. [FFVII Soundfont](https://youtu.be/p8YDa_khyKg?list=PLuijNdiAVrbY19dl9MrjWfR12EJ6UgVUh) by rocketbirdie
3. [Dom Palombi's](https://www.youtube.com/@DomPalombiMusic) works

## Windows

### Usage

1. Download the latest release from the link above.
2. Extract the zip file.
3. (If necessary) Allow the app through Windows Security
   (Audit code through GitHub to verify.)
4. Import music replacement packs to the `packs/` folder
5. Make sure the music is directly within the folder of the replacement pack
   - An example pack with dummy files has been placed in the `packs/` folder.
     Internal structure of your replacement files should be similar to that of
     the example pack
6. Run `balatro-music-patch.exe` (Windows might give you a warning from SmartScreen,
   but press `More Info -> Run Anyway`.)
7. Follow the instructions in the program.

### Manually Patching Music (Windows)

1. Download 7zip from [here](https://www.7-zip.org/download.html).
2. Get the music files from the music replacement source 
   - The music files should be named `music1.ogg`, `music2.ogg`,..., `music5.ogg`
3. Open the location of Balatro on your computer and right-click
   on the Balatro executable (Balatro.exe).
4. Go to `7-Zip -> Open Archive`.
5. Navigate to the `resources/sounds/` folder in the archive.
6. Drag and drop the music files into the archive.
7. Close the archive and run Balatro.

## macOS

### Usage

1. Download the latest release from the link above.
2. Extract the zip file.
3. Open terminal
4. Navigate to the release directory
5. Run `./balatro-music-patch`
6. Follow the instructions in the program.

### Manually Patching Music (macOS)

1. Get the music files from the music replacement source 
   - The music files should be named `music1.ogg`, `music2.ogg`,..., `music5.ogg`
2. Navigate to '~/Library/Application Support/Steam/steamapps/common/Balatro'
   (It's easiest to use 'Go To Folder' in the menu bar or Cmd-Shift-G)
3. Right click on Balatro.app and click 'Show Package Contents'.
4. Navigate to 'Contents/Resources/'
5. Rename 'Balatro.love' to 'Balatro.zip'
6. Double click 'Balatro.zip' to extract and navigate into the Balatro folder
7. Navigate to the `resources/sounds/` folder.
8. Drag and drop the music files into the folder.
9.  Return to the Balatro folder from step 7
10. Press shift-A to select all, right click, and press 'Compress'
11. Rename 'Archive.zip' to 'Balatro.love' and copy it to the
    'Contents/Resources/' folder from step 5
12. Delete the Balatro folder and 'Balatro.zip' from 'Contents/Resources/'
13. Run Balatro.

## Building from Source

1. Clone the repository.
2. Install `pyinstaller` with `pip install pyinstaller`.
3. Run `pyinstaller --onefile main.py`.
4. The executable will be in the `dist/` folder.
5. Run the executable in a directory with the resources folder

## Credit

- 7zip for opening archives.
- PyInstaller for .exe creation.
- The Balatro team for the game.
