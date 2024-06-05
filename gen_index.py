# Generate nav part of mkdocs.yaml
# from markdown file titles in file/
import os
import re
import yaml

# base: index_base.yaml (with everything except nav)
# result: mkdocs.yaml 

authorname_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_'

def tokenize(text):
    token_specification = [
        ('SECTION_START', r'\{section\}'),
        ('SECTION_END', r'\{section end\}'),
        ('HEADER', r'(?<!#)# [^\r\n]*\r?\n'),
        ('CONTENT', r'(?:[^#\{]+|(?:##+ [^\r\n]*\r?\n))+')
    ]
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    get_token = re.compile(tok_regex)
    
    tokens = []
    for match in get_token.finditer(text):
        kind = match.lastgroup
        value = match.group()
        tokens.append((kind, value))
    return tokens

def parse(tokens):
    stack = []
    ast = []
    current_section = None

    for kind, value in tokens:
        if kind == 'SECTION_START':
            new_section = []
            section_node = {'section': new_section}
            if current_section is not None:
                current_section.append(section_node)
            else:
                ast.append(section_node)
            stack.append(current_section)
            current_section = new_section
        elif kind == 'SECTION_END':
            if not stack:
                raise SyntaxError("Unmatched section end.")
            current_section = stack.pop()
        else:
            if current_section is not None:
                current_section.append((kind, value))
            else:
                ast.append((kind, value))
    
    if stack:
        raise SyntaxError("Unmatched section start.")
    
    return ast

def get_markdown_files(directory):
    """Get a list of all markdown files in the specified directory."""
    if __debug__:
        return [f for f in os.listdir(directory) if f.endswith('.md')]
    return [f for f in os.listdir(directory) if f.endswith('.md') and f != 'guide_template.md']

def match_guide_info(content):
    """Match the author name, date, and author nickname in the content."""
    title = re.search(r'title: (.+)', content).group(1)
    date = re.search(r'date: (.+)', content).group(1)
    author = re.search(r'author: (.+)', content).group(1)
    author_nickname = re.search(r'author_nickname: (.+)', content).group(1)
    if any([c not in authorname_chars for c in author]):
        raise ValueError('Invalid author name')
    return title, date, author, author_nickname

def create_page(content, file_dir, title = "", date = "", author_nickname = ""):
    if title != "":
        # create mkdocs !!!note block at the beginning
        content = f"!!! note\n    - 作者: {author_nickname}\n    - 日期: {date}\n\n" + content
    # create file
    with open(file_dir, 'w', encoding='utf-8') as f:
        f.write(content)

def append_content_to_file(content, file_dir):
    with open(file_dir, 'a', encoding='utf-8') as f:
        f.write(content)

def generate_by_ast(ast, directory, title, date, author_nickname, page_id: list, section_id: list):
    for node in ast:
        if isinstance(node, dict):
            section_id.append(section_id[-1] + 1)
            page_id.append(0)
            if section_id[-1] != 0:
                dir_with_section = directory + f's{section_id[-1]}/'
                os.mkdir(dir_with_section)
            else:
                dir_with_section = directory
            generate_by_ast(node['section'], dir_with_section, title, date, author_nickname, page_id, section_id)
            section_id.pop()
            page_id.pop()
        else:
            kind, value = node
            if kind == 'HEADER':
                # TODO: 匹配 section 标题, 有些时候 (在 {section 底下的时候)
                # header 不是新建页面的标题, 而是 nav 一个层级的标题
                page_id[-1] += 1
                if not value.isspace():
                    create_page(value, directory + f'p{page_id[-1]}.md', title, date, author_nickname)
            elif kind == 'CONTENT':
                if page_id[-1] != 0:
                    append_content_to_file(value, directory + f'p{page_id[-1]}.md')
    # TODO: 生成 nav
            
def split_content_to_files(content, title, date, author, author_nickname, directory):
    # the following code may be extremely ugly
    # because I haven't learned complier theory
    # A better way is to implement a parser then generate AST
    
    """
    create dir docs/guide/authorname/
    create sub dir for {section} tag
    create a markdown file for every level 1 header
    
    single page be like:  docs/guide/authoname/p{page id}.md
    section be like: docs/guide/authoname/s{section id}/p{page id}.md
    id starts from 1
    """
    author_dir = directory + author + '/'
    if not os.path.exists(author_dir):
        os.mkdir(author_dir)
    tokens = tokenize(content)
    ast = parse(tokens)
    page_id, section_id = [0], [0]
    current_page = None
    generate_by_ast(ast, author_dir, title, date, author_nickname, page_id, section_id)
    # TODO: 生成 nav
    # 这里的返回值应该是包含单个用户 nav 信息的一个 dict?list?
    return 114514
    

def generate_single_file_nav(directory, file):
    with open(directory + file, 'r', encoding='utf-8') as f:
        content = f.read()
        title, date, author, author_nickname = match_guide_info(content)
        if __debug__:
            print(title, date, author, author_nickname)
        content = content.split('---', 2)[2].strip()
        return split_content_to_files(content, title, date, author, author_nickname, directory)
        

def generate_nav_section(files, directory):
    """Generate the nav section from markdown file titles."""
    nav = []
    for file in files:
        nav.append(generate_single_file_nav(directory, file))
    return nav

def merge_with_base_nav(base_file, guide_section):
    """Merge the base YAML content with the generated nav section."""
    # dump file
    with open(base_file, 'r', encoding='utf-8') as f:
        base_content = yaml.safe_load(f)
        # extract '经验分享' section
        guide_index = base_content['nav'].index({'经验分享': 'leave this empty'})
        if __debug__:
            print(base_content)
        base_content['nav'][guide_index]['经验分享'] = guide_section
        if __debug__:
            print(base_content['nav'][guide_index])
    
    return base_content

def save_yaml(content, output_file):
    """Save the content to a YAML file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(content, f, default_flow_style=False, allow_unicode=True)

def main():
    base_file = 'index_base.yaml'
    output_file = 'mkdocs.yaml'
    if __debug__:
        output_file = 'mkdocs_temp.yaml'
    file_dir = 'docs/guide/'
    markdown_files = get_markdown_files(file_dir)
    nav_section = generate_nav_section(markdown_files, file_dir)
    merged_content = merge_with_base_nav(base_file, nav_section)
    save_yaml(merged_content, output_file)

if __name__ == '__main__':
    # main()
    # still in progress
    print("Finished generating nav section in mkdocs.yaml")