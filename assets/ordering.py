import markdown

new_lines = []

def alphabetordering(grouping_lines):
    grouping_lines.sort(key=str.lower)
    return grouping_lines

with open('../README.md', 'r') as f:
    lines = f.read().split('\n')
    grouping_lines = []
    for line in lines:
        if line[0:3] == '- [':
            grouping_lines.append(line[3:])
        elif grouping_lines != []:
            ordered_list = alphabetordering(grouping_lines)
            for line in ordered_list:
                line = "- [" + line
                new_lines.append(line)
            grouping_lines = []
            new_lines.append(line)
        else:
            new_lines.append(line)

with open('../README_new.md', 'w') as f:
    for line in new_lines:
        f.write(line + '\n')