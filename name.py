import re

def replace_dear(text,employee_name):
    dear_pattern = r'[Dd]ear[a-zA-Z0-9\s/\.\_]*\,+|[Dd]ear\s*((-|_)[a-zA-Z0-9]*(-|_)*(-|_))|[Dd]ear\s*\([a-zA-Z0-9\s]*\)|[Dd]ear[\s\.]*'
    name_set = []
    for match in re.finditer(dear_pattern, text):
        name_set.append(match)
    text_temp = text.replace(name_set[0][0], employee_name+ ',\n')
    return text_temp
