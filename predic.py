import pickle
import spacy

def predict_spacy(content, model_filepath):

    with open(model_filepath, 'rb') as f:
        model = pickle.load(f)
    nlp = spacy.blank(model['lang'])
    for pipe_name in model['pipeline']:
        pipe = nlp.create_pipe(pipe_name)
        nlp.add_pipe(pipe)
    nlp.from_bytes(model['bytes_data'])

    content = content.lower()
    doc = nlp(content)

    output = dict()
    for ent in doc.ents:
        output[ent.label_] = []
    for ent in doc.ents:
        if ent.text not in output[ent.label_]:
            output[ent.label_].append([ent.text, ent.start_char, ent.end_char])
        pass
    return output