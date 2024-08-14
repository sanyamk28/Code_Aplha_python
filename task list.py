import os
import shutil

def organize_files(directory):
    # Dictionary to hold extensions and their corresponding folder names
    extensions_folders = {
        'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp']
    }

    # Create folders if they don't exist
    for folder in extensions_folders:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their corresponding folders
    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Find the folder for the file extension
        for folder, extensions in extensions_folders.items():
            if file_ext in extensions:
                # Move the file to the appropriate folder
                src_path = os.path.join(directory, filename)
                dest_path = os.path.join(directory, folder, filename)
                shutil.move(src_path, dest_path)
                print(f"Moved: {filename} to {folder}")
                break

# Example usage
directory_path = '/path/to/your/directory'  # Replace with your directory path
organize_files(directory_path)
