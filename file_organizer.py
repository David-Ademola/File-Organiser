# 📚 Import the necessary libraries.
import os
import shutil

# 📖 Create a dictionary of file extensions and folders
# with extension name as keys 🔑 and folder name as values.
extensions = {
    'exe': 'Applications',
    'pdf': 'PDF\'s',
    'mp3': 'Music',
    'mp4': 'Movies',
    'jpg': 'Pictures',
    'png': 'Pictures',
    'py': 'Python',
    'txt': 'Text Files',
    'mkv': 'Videos',
    'js': 'JavaScript',
}

# Go through all the files 📄 in the current directory and
# depending on the file extension, create an appropriate
# folder 📁 named after the extensions value and place it in
# there. E.g `.mp3` in Music folder
current_directory = os.getcwd()
files = os.listdir(current_directory)

for document in files:
    document_path = os.path.join(current_directory, document)

    if os.path.isfile(document_path):
        extension = document.split('.')[-1]

        if extension in set(extensions.keys()):
            folder = extensions[extension]
            folder_path = os.path.join(current_directory, folder)

            # TODO: Add an if statement to check if the folder already exists
            os.mkdir(folder)
            shutil.move(document, folder_path)
            print(f'{document} was moved to folder {folder}')