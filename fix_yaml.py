import glob
import re

def fix_yaml():
    files = glob.glob('_posts/*.md')
    fixed_count = 0
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        changed = False
        in_frontmatter = False
        
        for i, line in enumerate(lines):
            if i == 0 and line == '---':
                in_frontmatter = True
                continue
            if in_frontmatter and line == '---':
                in_frontmatter = False
                continue
                
            if in_frontmatter:
                # Fix image
                if line.startswith('image: "'):
                    rest = line[8:]
                    if rest.endswith('"'):
                        rest = rest[:-1]
                    if ' "' in rest:
                        url = rest.split(' "')[0]
                        lines[i] = f'image: "{url}"'
                        changed = True

                # Fix title and description with internal double quotes
                for prefix in ('title: "', 'description: "'):
                    if line.startswith(prefix) and line.endswith('"'):
                        inner = line[len(prefix):-1]
                        # If there are double quotes inside
                        if '"' in inner:
                            # Replace internal double quotes with single quotes
                            new_inner = inner.replace('"', "'")
                            lines[i] = f'{prefix}{new_inner}"'
                            changed = True

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            fixed_count += 1

    print(f"Fixed {fixed_count} files.")

if __name__ == '__main__':
    fix_yaml()
