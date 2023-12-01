import re

with open("Day07/day07_input.txt") as f:
    content = f.read().splitlines(False)

print(content)

tree = {}

for line in content:
    rgx_dirs = re.findall("\w+", line)
    if rgx_dirs[0] == 'dir':
        tree[rgx_dirs[1]] = {}

# for line in content:
#     rgx_files = re.findall("\w.\w+", line)
#     if rgx_files[1]:
#         pass


rgx_files = re.match("^\d\w.\w+", content[3])[0]
print(rgx_files)

print(tree)