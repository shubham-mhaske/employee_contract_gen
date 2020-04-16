import re

def replace_dear(text,employee_name):
    name_set = []
    dear_pattern = r'[Dd]ear[a-zA-Z0-9\s/\.\_]*\,+|[Dd]ear\s*((-|_)[a-zA-Z0-9]*(-|_)*(-|_))|[Dd]ear\s*\([a-zA-Z0-9\s]*\)|[Dd]ear[\s\.]*'

    for match in re.finditer(dear_pattern, text):
        name_set.append(match)

    text = text.replace(name_set[0][0], 'Dear Shubham,\n')
    return text
