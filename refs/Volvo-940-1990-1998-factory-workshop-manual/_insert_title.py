import os
import glob

def add_title(md_file):
    # Get the filename without extension and replace underscores and dashes with spaces.
    title = os.path.splitext(os.path.basename(md_file))[0].replace('_', ' ').replace('-', ' ')

    with open(md_file, 'r+') as file:
        content = file.read()

        # Move the pointer to the beginning of the file.
        file.seek(0)

        # Write the new title and then the original content.
        file.write('# ' + title + '\n\n' + content)

def main():
    md_files = glob.glob('./*.md')
    for md_file in md_files:
        add_title(md_file)

if __name__ == "__main__":
    main()
    #  add_title("ELECTRONIC ENGINE CONTROLS.md")

