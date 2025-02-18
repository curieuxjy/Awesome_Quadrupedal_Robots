import difflib
import os
import markdown

def alphabet_ordering(grouping_lines):
    grouping_lines.sort(key=str.lower)
    return grouping_lines

def remove_duplicates(lines):
    seen_titles = set()
    unique_lines = []
    for line in lines:
        if line.startswith("![]"):
            unique_lines.append(line)
        else:
            title = line.split(']')[0]  # Extract the title part
            short_title = title[:50]  # Consider only the first 50 characters
            if short_title not in seen_titles:
                unique_lines.append(line)
                seen_titles.add(short_title)
    return unique_lines

new_lines = []

# Process the original README.md file
old_file_path = '../README.md'
with open(old_file_path, 'r', encoding="UTF-8") as f:
    # Read and split into lines (remove the extra empty string if file ends with a newline)
    lines = f.read().split('\n')
    if lines and lines[-1] == '':
        lines = lines[:-1]

    grouping_lines = []
    for line in lines:
        if line.startswith('- ['):
            grouping_lines.append(line[3:])
        elif grouping_lines:
            # Flush the current grouping_lines before processing this non-group line
            ordered_list = alphabet_ordering(grouping_lines)
            unique_list = remove_duplicates(ordered_list)
            for oline in unique_list:
                new_lines.append("- [" + oline)
            grouping_lines = []
            new_lines.append(line)
        else:
            new_lines.append(line)
    # Flush any remaining grouping_lines at end-of-file
    if grouping_lines:
        ordered_list = alphabet_ordering(grouping_lines)
        unique_list = remove_duplicates(ordered_list)
        for oline in unique_list:
            new_lines.append("- [" + oline)

# Write the new content to README_new.md
new_file_path = '../README_new.md'
with open(new_file_path, 'w', encoding='UTF-8') as f:
    for line in new_lines:
        f.write(line + '\n')

# Read both files with preserved line endings for an accurate diff
with open(old_file_path, 'r', encoding='UTF-8') as f:
    old_text = f.read()
    old_lines = old_text.splitlines(keepends=True)

with open(new_file_path, 'r', encoding='UTF-8') as f:
    new_text = f.read()
    new_lines_for_diff = new_text.splitlines(keepends=True)

# Generate unified diff (deleted lines are marked with a '-' sign)
diff = list(difflib.unified_diff(
    old_lines,
    new_lines_for_diff,
    fromfile='README.md',
    tofile='README_new.md',
    lineterm=''
))

# Alert the user to check the differences
print("The difference between 'README.md' and 'README_new.md'. You can check the changes below:")
print("\n".join(diff))

# Confirm whether to update README.md with the new file
confirm = input("Do you want to update 'README.md' with 'README_new.md'? [y]es/[n]o: ").strip().lower()
if confirm.startswith('y'):
    # Replace README.md with README_new.md and remove the new file
    os.replace(new_file_path, old_file_path)
    print("README.md updated successfully.")
else:
    print("Update cancelled. The file README_new.md remains available for review.")
