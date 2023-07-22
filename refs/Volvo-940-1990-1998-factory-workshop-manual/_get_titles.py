import os
from dotenv import load_dotenv
import openai
from pathlib import Path

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_title(doc_title, section_text):
    section_text = section_text[:1000]  # Limit to first 1000 characters
    message = f"""
    We are working on a set of documents for servicing, diagnosing and maintaining a 1993 Volvo 940.
    You are helping to provide titles for sections within the documents. 
    The following section is in the document entitled: {doc_title}
    ```
    {section_text}
    ```
    suggest a one line title, do not use quotes in the title:
    """

    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": message},
        ],
        temperature=0.6,
        max_tokens=60,
    )


    response_text = response.choices[0]['message']['content']
    print(response_text)
    return response_text

def add_section_titles(md_file):
    with open(md_file, 'r') as file:
        content = file.readlines()

    new_content = []
    section_text = ''
    doc_title = content[0].split('#')[1].strip()  # Get document title

    for line in content:
        if line.strip() == '---':
            title = generate_title(doc_title, section_text)
            new_content.append('\n## ' + title + '\n\n')
            new_content.append(section_text)
            new_content.append(line)
            section_text = ''  # Reset the section_text
        else:
            section_text += line

    with open(md_file, 'w') as file:
        file.writelines(new_content)

def main():
    md_file = 'ELECTRONIC ENGINE CONTROLS.md'
    add_section_titles(md_file)

if __name__ == "__main__":
    main()

