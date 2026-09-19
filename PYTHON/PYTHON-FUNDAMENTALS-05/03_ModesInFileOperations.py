# Modes in File Operations in Python
# In Python, you can open files in different modes to perform various operations. The most common modes are:
# 1. Read Mode ('r'): Opens a file for reading. The file pointer is placed at the beginning of the file. This is the default mode.
# 2. Write Mode ('w'): Opens a file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# 3. Append Mode ('a'): Opens a file for appending. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.
# 4. X Mode ('x'): Opens a file for exclusive creation. If the file already exists, the operation fails.
# 5. Binary Mode ('b'): Opens a file in binary mode. This is used for non-text files like images or executable files.
# 6. Text Mode ('t'): Opens a file in text mode. This is the default mode and is used for text files.
# 7. Read and Write Mode ('r+'): Opens a file for both reading and writing. The file pointer is placed at the beginning of the file.
# 8. Write and Read Mode ('w+'): Opens a file for both writing and reading. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# 9. Append and Read Mode ('a+'): Opens a file for both appending and reading. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.
# 10. Exclusive Creation and Read Mode ('x+'): Opens a file for exclusive creation and reading. If the file already exists, the operation fails.
# 11. Binary Read and Write Mode ('rb+'): Opens a file for both reading and writing in binary mode. The file pointer is placed at the beginning of the file.
# 12. Binary Write and Read Mode ('wb+'): Opens a file for both writing and reading in binary mode. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# 13. Binary Append and Read Mode ('ab+'): Opens a file for both appending and reading in binary mode. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.
# 14. Binary Exclusive Creation and Read Mode ('xb+'): Opens a file for exclusive creation and reading in binary mode. If the file already exists, the operation fails.
# 15. Binary Text Mode ('bt'): Opens a file in binary text mode. This is used for text files in binary format.
# 16. Binary Text Read and Write Mode ('r+b'): Opens a file for both reading and writing in binary text mode. The file pointer is placed at the beginning of the file.
# 17. Binary Text Write and Read Mode ('w+b'): Opens a file for both writing and reading in binary text mode. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# 18. Binary Text Append and Read Mode ('a+b'): Opens a file for both appending and reading in binary text mode. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.
# 19. Binary Text Exclusive Creation and Read Mode ('x+b'): Opens a file for exclusive creation and reading in binary text mode. If the file already exists, the operation fails.
# 20. Universal Newline Mode ('U'): Opens a file in universal newline mode. This mode allows you to read files with different newline conventions (e.g., '\n', '\r\n', '\r') and automatically converts them to '\n' when reading.
