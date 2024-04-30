from flask import Flask, render_template, request
from helperFunctions import convert_message_to_morse_code
from helperData import MORSE_CODE_DICT

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/morse-code', methods=['GET', 'POST'])
def get_morse_message():
    morse_message = convert_message_to_morse_code(request.form['message'].upper(), MORSE_CODE_DICT)
    return render_template('result.html', html_morse_message=morse_message)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
