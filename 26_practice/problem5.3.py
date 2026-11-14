# Write a Python command-line tool that takes a folder name and prints the total size of all files inside it (use os.path.getsize()).

import os
import sys

def get_folder_size(folder_name):
    total_size = 0
    file_count = 0

    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename)

        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            total_size += size
            file_count += 1
            print(f"{filename} - {size} bytes")

    print(f"\nTotal Files: {file_count}")
    print(f"Total Size: {total_size} bytes")
    print(f"Total Size: {total_size / 1024:.2f} KB")
    print(f"Total Size: {total_size / (1024*1024):.2f} MB")

if __name__ == "__main__":
    folder = sys.argv[1]
    get_folder_size(folder)