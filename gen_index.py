# Generate nav part of mkdocs.yaml
# from markdown file titles in file/
import os
import yaml

# base: index_base.yaml (with everything except nav)
# result: mkdocs.yaml 

def get_markdown_files(directory):
    """Get a list of all markdown files in the specified directory."""
    return [f for f in os.listdir(directory) if f.endswith('.md')]

def generate_nav_section(files, directory):
    """Generate the nav section from markdown file titles."""
    nav = []
    for file in files:
        title = os.path.splitext(file)[0]  # Remove .md extension
        nav.append({title: os.path.join(directory, file)})
    return nav

def merge_with_base_nav(base_file, nav_section):
    """Merge the base YAML content with the generated nav section."""
    with open(base_file, 'r') as f:
        base_content = yaml.safe_load(f)

    base_content['nav'] = nav_section
    
    return base_content

def save_yaml(content, output_file):
    """Save the content to a YAML file."""
    with open(output_file, 'w') as f:
        yaml.dump(content, f, default_flow_style=False)

def main():
    base_file = 'index_base.yaml'
    output_file = 'mkdocs.yaml'
    file_dir = 'docs/guide/'
    markdown_files = get_markdown_files(file_dir)
    nav_section = generate_nav_section(markdown_files, file_dir)
    merged_content = merge_with_base_nav(base_file, nav_section)
    save_yaml(merged_content, output_file)

if __name__ == '__main__':
    print("Finished generating nav section in mkdocs.yaml")
    # still working in progress...
    # main()