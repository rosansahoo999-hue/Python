# Create a script that deletes all .tmp files from the current directory using os and os.remove().

import os

def delete_tmp_files():
    deleted_count = 0
    for filename in os.listdir('.'):
        if filename.endswith('.tmp'):
            os.remove(filename)
            print(f"Deleted: {filename}")
            deleted_count += 1

    if deleted_count == 0:
        print("Koi .tmp file nahi mili.")
    else:
        print(f"Done! Total {deleted_count} .tmp files delete ho gayi.")

if __name__ == "__main__":
    delete_tmp_files()