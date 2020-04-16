

def replace_startdate(text,date,out):
    if 'StartDate' in out.keys():
        for i in out['StartDate']:
            text = text[:i[2] + 1] + date + text[i[2] + len(date):]
    return text