import re
def replace_cname(text,cname):
    pattern = '[cC]ompany\s*[nN]ame'
    cname_set = []
    for match in re.finditer(pattern,text):
            cname_set.append(match)
    return cname_set