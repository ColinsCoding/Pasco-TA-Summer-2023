# import os

# # Specify the directory you want to explore
# directory_path = '/Users/colincasey/Dropbox/Phys 350/350 Labs'

# # Get list of all .docx files in the directory
# file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f)) and f.endswith('.docx')]

# # Specify the name of the txt file you want to create
# txt_file_name = 'file_list.txt'

# # Open the txt file in write mode and write each file name to it
# with open(txt_file_name, 'w') as f:
#     for file_name in file_list:
#         f.write(f'{file_name}\n')

# import os

# # Specify the directory you want to explore
# directory_path = '/Users/colincasey/Dropbox'

# # Specify the name of the txt file you want to create
# txt_file_name = 'file_list.txt'

# # Open the txt file in write mode
# with open(txt_file_name, 'w') as f:
#     # Walk through the directory
#     for dirpath, dirnames, filenames in os.walk(directory_path):
#         # Filter out the .docx files
#         docx_files = [file for file in filenames if file.endswith('.docx')]

#         # If there are .docx files in this directory
#         if docx_files:
#             f.write(f'Directory: {dirpath}\n')
#             for file_name in docx_files:
#                 f.write(f'\t{file_name}\n')


import os

# The directory you want to start from.
directory_path = '/Users/colincasey/Dropbox'

# The name of the output text file.
txt_file_name = 'file_list.txt'

# This list will store all the directories that contain .docx files.
directories_with_docx = []

# Open the output file in write mode.
with open(txt_file_name, 'w') as f:
    # Walk through the directory tree.
    for dirpath, dirnames, filenames in os.walk(directory_path):
        # Check if 'lab' is in the directory name.
        if 'lab' in dirpath.lower():
            # Get a list of all .docx files in this directory.
            docx_files = [file for file in filenames if file.endswith('.docx')]

            # If there are .docx files in this directory, add the directory path to the list.
            if docx_files:
                directories_with_docx.append(dirpath)

    # First, write the list of directories to the file.
    f.write("Directories with .docx files:\n")
    for directory in directories_with_docx:
        f.write(f"{directory}\n")

    # Then, leave a blank line before the detailed file list.
    f.write("\nDetailed list of .docx files:\n")

    # Now, walk through the directory tree again to write the detailed file list.
    for dirpath in directories_with_docx:
        # Get a list of all .docx files in this directory.
        docx_files = [file for file in os.listdir(dirpath) if file.endswith('.docx')]

        # Write the directory path and the file names to the file.
        f.write(f"Directory: {dirpath}\n")
        for file_name in docx_files:
            f.write(f"\t{file_name}\n")
