import re

def replace_address(text,emp_address):
    flag = False
    add_result = []
    add_pattern = r'[Aa]ddress[\s:_-]*'
    for match in re.finditer(add_pattern,text):
        add_result.append(match)
        flag = True
    if flag:
        text = text.replace(add_result[0][0], 'Hadapsar,Pune \n')
    return text

