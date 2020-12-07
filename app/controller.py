from flask import render_template, request
from app import app
from app.src.player import *
from app.src.player_list import players, add_new_player, player_make_choice, play_janken


@app.route('/')
def index():
    return render_template('index.html', title ='Home ', players = players)

# @app.route('/add_players')
# def render_name() -> 'html':
#     return render_template(name.html) 

#@app.route('/add_players', methods = ['POST'])
@app.route('/add-players', methods = ['POST'])
def add_players():
    # print(request.form)
    # return "done"
    player_1_name = request.form["name1"]
    player_2_name = request.form["name2"]
    new_player_1 = Player(name = player_1_name,)
    new_player_2 = Player(name = player_2_name)
    add_new_player(new_player_1)
    add_new_player(new_player_2)
    return render_template('index.html', title = 'Home', players = players)


# @app.route('/play-mutliplayer', methods = ['POST'])
# def play_multiplayer(first_player, second_player):
#     return play_janken(first_player, second_player)


