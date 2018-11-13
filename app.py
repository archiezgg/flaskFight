from flask import Flask, render_template, request, redirect
from logics.barbarian import Barbarian
from logics.mage import Mage
from logics.arena import *

# Hard coded DB
list_of_characters = []

app = Flask(__name__)

@app.route('/')
def index():
    if len(list_of_characters) > 0:
        list_of_characters.clear()

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

    if len(list_of_characters) == 0:
        return redirect('/')

    barb_char = list_of_characters[0]
    mage_char = list_of_characters[1]

    console_log = fight(barbarian=barb_char, mage=mage_char)
    part_of_log = []

    starter_index = 0
    for char in console_log:
        if char == ';':
            index_of_char = console_log.find(char)
            part = console_log[starter_index:index_of_char]
            starter_index = index_of_char
            part_of_log.append(part)
            console_log = list(console_log)
            console_log[index_of_char] = ''
            console_log = ''.join(console_log)

    list_of_characters.clear()


    return render_template('arena.html', part_of_log=part_of_log)


if __name__ == '__main__':
    app.run(debug = True)
