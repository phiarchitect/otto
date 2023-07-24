import glob

def remove_section_breaks(md_file):
    with open(md_file, 'r') as file:
        content = file.readlines()

    new_content = []
    skip_next = False

    for line in content:
        if line.strip() == '---':
            skip_next = True
        elif skip_next and line.strip() == '':
            skip_next = False
        else:
            new_content.append(line)

    with open(md_file, 'w') as file:
        file.writelines(new_content)

def main():
    md_files = glob.glob('./*.md')
    for md_file in md_files:
        remove_section_breaks(md_file)

if __name__ == "__main__":
    main()

