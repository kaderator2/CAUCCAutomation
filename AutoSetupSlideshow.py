# search network drive for imgs
# P:\Worship\Video-Powerpoints\2022\7 July 2022\7.10.22\
import os
import shutil
from datetime import date
import ctypes

def get_directory_path():
    today = date.today()
    year = today.strftime("%Y")
    month_num = today.strftime("%m").lstrip("0")
    month_name = today.strftime("%B")
    day = today.strftime("%d").lstrip("0")
    return f"P:/Worship/Video-Powerpoints/{year}/{month_num} {month_name} {year}/{month_num}.{day}.{year[-2:]}/"

def copy_files(source_dir, target_dir, extensions):
    try:
        source_files = os.listdir(source_dir)
    except FileNotFoundError:
        print(f"Cannot find source folder: {source_dir}")
        return False

    try:
        target_files = os.listdir(target_dir)
    except FileNotFoundError:
        print(f"Cannot find target folder: {target_dir}")
        return False

    for extension in extensions:
        print(f"Clearing {target_dir} of {extension} files")
        for file in target_files:
            if file.lower().endswith(extension):
                os.remove(os.path.join(target_dir, file))

        print(f"Copying {extension} files!")
        for file in source_files:
            if file.lower().endswith(extension):
                shutil.copy(os.path.join(source_dir, file), target_dir)

    return True

def main():
    source_dir = get_directory_path()
    target_dir = "C:/Users/Loft/Desktop/RollingSlideshowsDONOTDELETE/"
    extensions = [".png", ".mp3"]

    success = copy_files(source_dir, target_dir, extensions)
    if success:
        print("Files copied successfully!")
        ctypes.windll.user32.MessageBoxW(0, "Slideshow files copied successfully!", "Slideshow Success", 0)
    else:
        print("An error occurred while copying files.")
        ctypes.windll.user32.MessageBoxW(0, "An error occurred while copying the slideshow files. Please refer to the troubleshooting manual.", "Slideshow Error", 0)


if __name__ == "__main__":
    main()