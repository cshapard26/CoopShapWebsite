import sys
import re
import json

def load_replacements(config_file):
    with open(config_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def convert_markdown(md_file, replacements):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    for md, html in replacements.items():
        content = re.sub(md, html, content, flags=re.MULTILINE)
    return content

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input.md> <output.html>")
        sys.exit(1)
    md_file, output_file = sys.argv[1], sys.argv[2]
    config_file = "html-config.json"
    replacements = load_replacements(config_file)
    html_content = convert_markdown(md_file, replacements)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    main()
