import read_file
import name
import sub
import address
import company


text  = read_file.read_file('final/10.pdf')
text = name.replace_dear(text,'Dear Shubham')
print(text)


