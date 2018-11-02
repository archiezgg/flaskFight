from flask import Flask, render_template, request
from logics.barbarian import Barbarian
from logics.mage import Mage


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/characters', methods =('GET', 'POST'))
def create_characters():
    if request.method == 'POST':
        barbarian_name = request.values.get('barbarian_name')
        mage_name = request.values.get('mage_name')

        barb_char = Barbarian(barbarian_name)
        mage_char = Mage(mage_name)

    return render_template('characters.html', barbarian = barb_char, mage = mage_char)


if __name__ == '__main__':
    app.run(debug = True)
