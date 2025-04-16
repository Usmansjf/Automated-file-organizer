import os
import shutil
from pathlib import Path

def create_file_organizer(directory):
    """
    Organizes files in the specified directory into subfolders based on file type.
    
    Args:
        directory (str): Path to the directory to organize
    """
    # Dictionary mapping file extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
        'Audio': ['.mp3', '.wav', '.ogg', '.flac'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.html', '.css', '.java'],
        'Executables': ['.exe', '.msi', '.apk']
    }

    # Convert directory to Path object
    directory = Path(directory)
    
    # Create directories if they don't exist
    for folder in file_types.keys():
        folder_path = directory / folder
        folder_path.mkdir(exist_ok=True)

    # Counter for organized files
    organized_count = 0
    skipped_count = 0

    # Iterate through all files in the directory
    for item in directory.iterdir():
        # Skip if it's a directory
        if item.is_dir():
            continue
            
        # Get file extension
        file_ext = item.suffix.lower()
        
        # Find matching folder for the file extension
        destination_folder = None
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                destination_folder = folder
                break
        
        # If no matching folder found, move to 'Others'
        if destination_folder is None:
            destination_folder = 'Others'
            (directory / 'Others').mkdir(exist_ok=True)
        
        try:
            # Move the file to its destination folder
            destination = directory / destination_folder / item.name
            shutil.move(str(item), str(destination))
            organized_count += 1
            print(f"Moved: {item.name} -> {destination_folder}")
        except Exception as e:
            skipped_count += 1
            print(f"Error moving {item.name}: {str(e)}")

    return organized_count, skipped_count

def main():
    # Get the directory to organize (default is current directory)
    directory = input("Enter directory to organize (press Enter for current directory): ").strip()
    if not directory:
        directory = os.getcwd()

    # Verify directory exists
    if not os.path.exists(directory):
        print("Error: Directory does not exist!")
        return

    print(f"\nOrganizing files in: {directory}")
    print("-" * 50)

    try:
        organized, skipped = create_file_organizer(directory)
        print("\n" + "-" * 50)
        print(f"Organization complete!")
        print(f"Files organized: {organized}")
        print(f"Files skipped (due to errors): {skipped}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()