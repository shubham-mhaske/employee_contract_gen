import re

def replace_address(text,emp_address):
    add_result = []
    add_pattern = r'[Aa]ddress[\s:_-]*'
    for match in re.finditer(add_pattern,text):
        add_result.append(match)
    return (text.replace(add_result[0][0],emp_address+'\n'))
