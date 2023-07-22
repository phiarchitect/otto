import os
import re
import glob

def remove_header(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    pattern = re.compile(r"199[23] Volvo 940\nSubmodel: \| Engine Type: L4 \| Liters: 2.3\nFuel Delivery: FI \| Fuel: GAS\n")
    new_content = pattern.sub("---\n", content)

    with open(output_file, 'w') as file:
        file.write(new_content)

def main():
    txt_files = glob.glob('./*.txt')
    for txt_file in txt_files:
        md_file = os.path.splitext(txt_file)[0] + '.md'
        remove_header(txt_file, md_file)

if __name__ == "__main__":
    main()

