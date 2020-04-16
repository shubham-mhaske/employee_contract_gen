import re
def replace_cname(text,cname,out):
    # replace cname


    if 'Cname' in out.keys():
        for i in out['Cname']:
            print(i[0])
            text = text[:i[2] + 1] + cname + text[i[2] + len(cname):]
    pattern = '[cC]ompany\s*[nN]ame'
    cname_set = []
    for match in re.finditer(pattern,text):
            cname_set.append(match)
    for i in range(len(cname_set)):
        text = text.replace(cname_set[i][0], cname)

    return text