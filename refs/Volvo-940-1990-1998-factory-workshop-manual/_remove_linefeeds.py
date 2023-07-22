import glob

def remove_form_feed_chars(md_file):
    with open(md_file, 'r') as file:
        content = file.read()

    # Remove the form feed character '\f'
    content = content.replace('\f', '')

    with open(md_file, 'w') as file:
        file.write(content)

def main():
    md_files = glob.glob('./*.md')
    for md_file in md_files:
        remove_form_feed_chars(md_file)

if __name__ == "__main__":
    main()

