import markdown

new_lines = []

def write_ordering_list(ordering_list):
    ordering_list = sorted(ordering_list)
    for line in ordering_list:
        line = "- [" + line
        new_lines.append(line)

with open('../README.md', 'r') as f:
    lines = f.read().split('\n')
    ordering_list = []
    for line in lines:
        if line == '':
            if ordering_list != []:
                write_ordering_list(ordering_list)
                ordering_list = []
            new_lines.append(line)
        elif line[0:3] == '- [':
            first_letter = line[3]
            ordering_list.append(line[3:])
        else:
            if ordering_list != []:
                write_ordering_list(ordering_list)
                ordering_list = []
            new_lines.append(line)

with open('../README_new.md', 'w') as f:
    for line in new_lines:
        f.write(line + '\n')