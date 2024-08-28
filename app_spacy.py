from flask import Flask, request, jsonify, render_template
from spacy_bot import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_spacy.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json.get('message')
    response = get_response(user_message)
    return jsonify({'text': response})

if __name__ == '__main__':
    app.run(debug=True)
