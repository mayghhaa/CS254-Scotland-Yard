import sqlalchemy
from sqlalchemy import create_engine, text

# print(sqlalchemy.__version__)

engine = create_engine("mysql+pymysql://root:MeghaArya@localhost/ScotlandYard?charset=utf8mb4")

with engine.connect() as conn:
  result=conn.execute(text("select * from Players"))
  print(result.all())


def load_players_from_db(playerID):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("SELECT role FROM players WHERE playerID=:playerID"),
                {"playerID": playerID}
            )
            role_row = result.fetchone()  # Fetch the first row
            if role_row:
                role = role_row[0]  # Extract the role value
                return role
            else:
                print("Player not found.")
                return None
    except Exception as e:
        print(f"Error loading players from database: {e}")
        return None
def add_game_entry(game_id, player_id, role):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("INSERT INTO games_played (gameid, playerid, role) VALUES (:game_id, :player_id, :role)"),
                {"game_id": game_id, "player_id": player_id, "role": role}
            )
            print(f"Game entry added: Game ID {game_id}, Player ID {player_id}, Role {role}")
            conn.commit()
    except Exception as e:
        print(f"Error during insertion: {e}")


def add_player_to_db(player_name, player_score,positions):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("INSERT INTO players (player_name, playerid, Current_Location) VALUES (:player_name, :player_score, :pos)"),
                {"player_name": player_name, "player_score": player_score,"pos":positions}
            )
            
            print(f"Player inserted: {player_name}, {player_score}")
            conn.commit()
    except Exception as e:
        print(f"Error during insertion: {e}")


def leaderboard():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT PLAYERS.PlayerID, PLAYERS.Player_Name FROM PLAYERS WHERE PLAYERS.PlayerID NOT IN (SELECT LEADERBOARD.PlayerID FROM LEADERBOARD)"))
    
    #Add new players to Leaderboard
        if result:
           for row in result.all():
              conn.execute(text("INSERT INTO LEADERBOARD VALUES (:Pid, :Pname, 0,0,0,0,0)"),{"Pid": row[0], "Pname":row[1]})
              conn.commit()
    
  
def add_player_role_to_db(role):
    try:
        with engine.connect() as conn:
            # Update all players' role to 'police'
            result1 = conn.execute(
                text("UPDATE players SET role='police', turnno=1, taxi=10, bus=8, ug=4")
            )
            
            # Update players with the specified playerid to 'MRX'
            result = conn.execute(
                text("UPDATE players SET role='MRX', taxi=1000, bus=1000, ug=10000 WHERE playerid=:role"),
                {"role": role}
            )
            conn.commit()
    except Exception as e:
        print(f"Error during insertion: {e}")
              


# def add_player_role_to_db(role, positions):
#     try:
#         with engine.connect() as conn:
#             # Update all players' role to 'police' and set their positions
#             for player_position, player_id in zip(positions, range(1, len(positions) + 1)):
#                 result1 = conn.execute(
#                     text("UPDATE players SET role='police', turnno=1, taxi=10, bus=8, ug=4, position=:position WHERE playerid=:player_id"),
#                     {"position": player_position, "player_id": player_id}
#                 )

#             # Update players with the specified role to 'MRX'
#             result = conn.execute(
#                 text("UPDATE players SET role='MRX', taxi=1000, bus=1000, ug=10000 WHERE playerid=:role"),
#                 {"role": role}
#             )
#             conn.commit()
#     except Exception as e:
#         print(f"Error during insertion: {e}")(

#     def add_start_loc(Pos):
    



  
  