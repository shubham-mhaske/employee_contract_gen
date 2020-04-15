import  re

def replace_subject(text,letter_subject):
    sub_pattern = r'[Ss]ub(ject)?[\(\s:\-_a-zA-z1-9\)]*(_|\)|\.)'
    sub_set = []
    for match in re.finditer(sub_pattern, text):
        sub_set.append(match)
    for i in range(len(sub_set)):
        if 'appoint' in sub_set[i][0]:
            return text.replace(sub_set[i][0], letter_subject)