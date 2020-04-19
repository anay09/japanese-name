from flask import Flask
app = Flask(__name__)

alphabet_map = {
    'A': 'ka',
    'B': 'tu',
    'C': 'mi',
    'D': 'te',
    'E': 'ku',
    'F': 'lu',
    'G': 'ji',
    'H': 'ri',
    'I': 'ki',
    'J': 'zu',
    'K': 'me',
    'L': 'ta',
    'M': 'rin',
    'N': 'to',
    'O': 'mo',
    'P': 'no',
    'Q': 'ke',
    'R': 'shi',
    'S': 'ari',
    'T': 'chi',
    'U': 'do',
    'V': 'ru',
    'W': 'mei',
    'X': 'na',
    'Y': 'fu',
    'Z': 'zi',
}


@app.route('/')
def introductory_page():
    return '<h1><marquee>-------------English to Japanese Name Converter----------------'


@app.route('/<username>')
def converter(username):
    output_name = list()
    [output_name.append(alphabet_map[i.upper()]) for i in username]
    return 'Original Name: {i}, Translated Name: {o}'.format(
            o=''.join(output_name),
            i=username)
