# ✨CREATING A PROGRAM THAT ORGANISES FILES IN A DIRECTORY✨

# 📚 Import the necessary libraries.
import os
import shutil

current_directory = os.getcwd()
files = os.listdir(current_directory)

# 📖 Create a dictionary of file extensions and folders
# with folder name as keys 🔑 and extension name as values.
extensions = {
    'Applications': 'exe',
    'Files': 'pdf',
    'Music': 'mp3',
    'Movies': 'mp4',
    'Pictures': 'jpg',
    'Pictures': 'png',
    'Videos': 'mkv',
    'Python': 'py',
    'JavaScript': 'js'
}

# Go through all the files 📄 in the current directory and
# get their extensions.
for document in files:
    document_path = os.path.join(current_directory, document)
    if os.path.isfile(document_path):
        if document.split('.')[-1] in set(extensions.values()):
            print(document)

# Depending on the file extension, create an appropriate
# folder 📁 named after the extensions key and place it in
# there. E.g `.mp3` in Music Folder

# Brag about what I just created on Instagram, Twitter,
# LinkedIN and GitHub. 😁🐍

# Clearly the ability of this program depends largely on the
# size of the dictionary 📚,and that's why I'm going to make it
# open source 👨🏾‍💻 so you can add your own extensions to it.