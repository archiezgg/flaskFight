from flask import Flask, render_template, request
from logics.barbarian import Barbarian
from logics.mage import Mage
from logics.arena import *

# Hard coded DB

list_of_characters = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/characters', methods =('GET', 'POST'))
def create_characters():
    if request.method == 'POST':
        barbarian_name = request.form.get('barbarian_name')
        mage_name = request.values.get('mage_name')

        barb_char = Barbarian(barbarian_name)
        list_of_characters.append(barb_char)
        mage_char = Mage(mage_name)
        list_of_characters.append(mage_char)
        return render_template('characters.html', barbarian = barb_char, mage = mage_char)


@app.route('/arena')
def arena():
    barb_char = list_of_characters[0]
    mage_char = list_of_characters[1]

    return render_template('arena.html', barbarian = barb_char, mage = mage_char)


if __name__ == '__main__':
    app.run(debug = True)
