import read_file
import name
import sub
import address
import company
import  predic
import position
import startdate


text  = read_file.read_file('docs/3.pdf')

out = predic.predict_spacy(text,'my_model.pkl')
text = name.replace_dear(text,'Dear Shubham')
text = address.replace_address(text,'Hadapsar, Pune')
text = position.replace_position(text,' Software Developer ',out)
text = startdate.replace_startdate(text,' 12-12-2020 ',out)
text = company.replace_cname(text,' ABC Pvt. Ltd ',out)


print(text)


