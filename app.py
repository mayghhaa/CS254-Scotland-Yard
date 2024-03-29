import random
from flask import Flask, render_template, request
from database import add_player_to_db, add_player_role_to_db, load_players_from_db, add_game_entry, leaderboard, game_id

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/store_values', methods=['POST'])
def store_values():
    entries = {}
    role = request.form['role']
    pos = [1,2,3,4,5]
    count = 0
    # Store player information
    for i in range(1, 11):
        if i % 2 == 1:  # Odd-indexed values
            key = request.form[f'entry{i}']
        else:  # Even-indexed values
            value = request.form[f'entry{i}']
            entries[key] = value
            add_player_to_db(key, value,pos[count])
            count = count+1
            add_player_role_to_db(role)
    print(entries, role)
    leaderboard()

    # Start a new game
    start_new_game(role)

    return 'New game started successfully!'

def start_new_game(role):
    game_id = random.randint(1000, 9999)  # Generate a random game ID
    
    game_history(game_id)
    # Add entries for each player in the game
    for i in range(2, 11, 2):
        player_id = request.form[f'entry{i}']
        role = load_players_from_db(player_id)
        if role:
            add_game_entry(game_id, player_id, role)
        else:
            print(f"Role not found for player ID: {player_id}")
        print(game_id, player_id, role)

if __name__ == "__main__":
    app.run(debug=True)
