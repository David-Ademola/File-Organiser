# 📚 Import the necessary libraries.
import os
import shutil

# 📖 Create a dictionary of file extensions and folders
# with extension name as keys 🔑 and folder name as values.
extensions = {
    'exe': 'Applications',
    'ico': 'Icons',
    'mp3': 'Music',
    'pdf': 'PDF\'s',
    'jpg': 'Pictures',
    'png': 'Pictures',
    'py': 'Python',
    'txt': 'Text Files',
    'md': 'README\'s',
    'mkv': 'Videos',
    'mp4': 'Videos',
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

            if folder in os.listdir(os.getcwd()):
                shutil.move(document, folder_path)
                print(f'{document} was moved to folder {folder}')
            else:
                os.mkdir(folder)
                print(f'{folder} folder was created.')
                shutil.move(document, folder_path)
                print(f'{document} was moved to {folder} folder.')

input('Press ENTER key to quit.')