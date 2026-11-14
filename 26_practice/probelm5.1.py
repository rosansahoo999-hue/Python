# Write a program that reads a file and creates another file with all words converted to uppercase.

import sys

def convert_to_uppercase(input_filename, output_filename):
    with open(input_filename, 'r') as infile:
        content = infile.read()

    upper_content = content.upper()

    with open(output_filename, 'w') as outfile:
        outfile.write(upper_content)

    print(f"Done! {input_filename} -> {output_filename} me uppercase me save ho gaya.")

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_to_uppercase(input_file, output_file)