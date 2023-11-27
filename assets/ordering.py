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
            short_title = title[:50]  # Consider only the first 40 characters
            if short_title not in seen_titles:
                unique_lines.append(line)
                seen_titles.add(short_title)
    return unique_lines

new_lines = []

with open('../README.md', 'r', encoding="UTF-8") as f:
    lines = f.read().split('\n')
    lines = lines[:-1]
    grouping_lines = []
    for line in lines:
        if line.startswith('- ['):
            grouping_lines.append(line[3:])
        elif grouping_lines:
            ordered_list = alphabet_ordering(grouping_lines)
            unique_list = remove_duplicates(ordered_list)
            for oline in unique_list:
                oline = "- [" + oline
                new_lines.append(oline)
            grouping_lines = []
            new_lines.append(line)
        else:
            new_lines.append(line)

with open('../README_new.md', 'w', encoding='UTF-8') as f:
    for line in new_lines:
        f.write(line + '\n')
