import re
import glob

def format_list(md_file):
    with open(md_file, 'r') as file:
        content = file.readlines()

    # Leave the title as it is
    title = content[0]
    rest_of_content = content[1:]

    # Join the rest_of_content back into a string for regex operations
    rest_of_content = ''.join(rest_of_content)

    # Remove the extra newlines after numbered list items.
    rest_of_content = re.sub(r'(\d+.)\n\n', r'\1 ', rest_of_content)

    # Add an indentation (two spaces) before lettered list items and remove the extra newlines.
    rest_of_content = re.sub(r'([A-Z].)\n\n', r'  \1 ', rest_of_content)

    # Combine the title and rest_of_content
    content = title + rest_of_content

    with open(md_file, 'w') as file:
        file.write(content)

def main():
    md_files = glob.glob('./*.md')
    for md_file in md_files:
        format_list(md_file)

if __name__ == "__main__":
    main()

