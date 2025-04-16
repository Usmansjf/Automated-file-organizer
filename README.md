🗂️ Automated File Organizer Script:

This Python script automatically organizes files in a specified directory into categorized subfolders based on their file types. It's a handy utility to tidy up messy download folders, desktops, or any other cluttered directories.



📦 Features
Categorizes files into subfolders:

Images

Documents

Videos

Audio

Archives

Scripts

Executables

Others (for uncategorized file types)

Automatically creates folders if they don’t exist.

Skips folders and only processes files.

Handles file moving errors gracefully.




🧠 How It Works
The script scans the given directory and sorts files based on their extensions using predefined categories. For example:

.jpg, .png → Images/

.pdf, .docx, .txt → Documents/

.mp4, .mkv → Videos/

and so on...

Files that don't match any predefined category are moved to an Others/ folder.




⚠️ Notes
The script only processes files in the top-level of the specified directory (not recursive).

It skips directories and will not modify their contents.

Files with the same name in the destination folder may cause errors or overwrite — handle with care.



