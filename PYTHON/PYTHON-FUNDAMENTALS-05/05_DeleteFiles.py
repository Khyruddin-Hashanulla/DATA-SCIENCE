# Delete Files in Python refers to the process of removing files from the file system using Python's built-in functions.
# This can be useful for cleaning up temporary files, managing storage, or automating file management tasks.

import os

# Specify the file path to be deleted
file_path = "PYTHON/PYTHON-FUNDAMENTALS-05/SampleDel.txt"

# Check if the file exists before attempting to delete it
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file '{file_path}' has been deleted successfully.")
else:
    print(f"The file '{file_path}' does not exist.")
