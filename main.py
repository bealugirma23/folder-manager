# Python automation for organizing downloads
# Adjusting folders by the file type to the given folders

import os
from shutil import move
from pyuac import main_requires_admin

# Main directory
global user
user = os.getenv('username')

main_dir = f"C:/Users/{user}/Downloads"

# Destination directories
destination_dirs = {
    'Images': f'C:/Users/{user}/Downloads/Images',
    'Programs': f'C:/Users/{user}/Downloads/Programs',
    'Documents': f'C:/Users/{user}/Downloads/Documents',
    'Compressed': f'C:/Users/{user}/Downloads/Compressed',
    'Music': f'C:/Users/{user}/Downloads/Music',
    'Fonts': f'C:/Users/{user}/Downloads/Fonts'
}

@main_requires_admin  
def main():
    # Create destination directories if they do not exist
    for dir_name, dir_path in destination_dirs.items():
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print(f"Created directory: {dir_path}")

    # List files in the main directory
    directory = os.listdir(main_dir)
    print('Initial file count:', len(directory))

    # Move files based on their extensions
    for item in directory:
        file_name, file_extension = os.path.splitext(item)
        source_path = os.path.join(main_dir, item)  # Full path of the source file

        # Move image files
        if file_extension in ['.png', '.jpg', '.jpeg']:
            dest_path = os.path.join(destination_dirs['Images'], item)
            print(f'Moved {item} to Images folder')

        # Move program files (example extensions)
        elif file_extension in ['.exe', '.msi']:
            dest_path = os.path.join(destination_dirs['Programs'], item)
            print(f'Moved {item} to Programs folder')

        # Move document files (example extensions)
        elif file_extension in ['.pdf', '.docx', '.txt']:
            dest_path = os.path.join(destination_dirs['Documents'], item)
            print(f'Moved {item} to Documents folder')

        elif file_extension in ['.zip', '.rar', 'tar', '.iso']:
            dest_path = os.path.join(destination_dirs['Compressed'], item)
            print(f'Moved {item} to Compressed folder')

        elif file_extension in ['.mp3', '.mp4', '.m4a']:
            dest_path = os.path.join(destination_dirs['Music'], item)
            print(f'Moved {item} to Music folder')

        elif file_extension in ['.otf',]:
            dest_path = os.path.join(destination_dirs['Fonts'], item)
            print(f'Moved {item} to Music folder')
           
        elif file_extension in ['.crdownload']: 
            print('unfinished downloades found')

        else:
            continue

        base_name = file_name
        counter = 1

        while os.path.exists(dest_path):
            dest_path = os.path.join(destination_dirs[{ '.png': 'Images',
                '.jpg': 'Images',
                '.jpeg': 'Images',
                '.exe': 'Programs',
                '.msi': 'Programs',
                '.pdf': 'Documents',
                '.docx': 'Documents',
                '.txt': 'Documents',
                '.zip': 'Compressed',
                '.rar': 'Compressed',
                '.tar': 'Compressed',
                '.iso': 'Compressed',
                '.mp3': 'Music',
                '.mp4': 'Music',
                '.m4a': 'Music',
                '.otf': 'Fonts',
                '.ttf': 'Fonts'}], f"{base_name}_{counter}{file_extension}")
            counter += 1

          # Move the file
        move(source_path, dest_path)
        print(f'Moved {item} to {dest_path}')

    # Final count of files in the main directory
    total = len(os.listdir(main_dir))
    print('Final file count:', total)

if __name__ == "__main__":
    main()