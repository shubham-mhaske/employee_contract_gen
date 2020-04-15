import re

def replace_send_date(text):
    date_set = []
    date_pattern = r'[Dd]ate[\s:_-]*'

    for match in re.finditer(date_pattern, text):
        date_set.append(match)
    return text.replace(date_set[0][0], datetime.today().strftime('%d %B %Y') + '\n')
