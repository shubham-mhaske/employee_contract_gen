

def replace_position(text,position,out):
    if 'Position' in out.keys():
        for i in out['Position']:
            text = text[:i[2] + 1] + position + text[i[2] + len(position):]
    return text