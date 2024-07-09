# Generate docs/file.md from docs/file/ folder

import os
import argparse


def main(file_dir: str, output: str):
    folder_to_title = {"Chinese": ["语文"],
                       "Math": ["数学"],
                       "English": ["英语"],
                       "Physics": ["物理"],
                       "Chemistry": ["化学"],
                       "Biology": ["生物"],
                       "History": ["历史"],
                       "Geography": ["地理"],
                       "Politics": ["政治"],
                       "Others": ["其他"]
                       }
    for folder in os.listdir(file_dir):
        if folder in folder_to_title and os.listdir(file_dir + folder):
            folder_to_title[folder] += \
                sorted(os.listdir(file_dir + folder),
                       key=lambda x: os.path.getmtime(os.path.join(file_dir, folder, x)))
    with open(output, 'w', encoding='utf-8') as f:
        f.write("# 学习资料\n\n")
        for folder, info in folder_to_title.items():
            folder_title, *files = info
            if not files:
                continue
            f.write(f"### {folder_title}\n\n")
            for file in files:
                file_name, _ = os.path.splitext(file)
                f.write(
                    f'[{file_name}](./file/{folder}/{file}){{:download="{file}"}}\n\n')


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--dir', '-d', help='File directory', default='docs/file/')
    arg_parser.add_argument(
        '--output', '-o', help='Output file', default='docs/file.md')
    print("Generating docs from folders...")
    main(arg_parser.parse_args().dir, arg_parser.parse_args().output)
    print("Genetation complete.")
