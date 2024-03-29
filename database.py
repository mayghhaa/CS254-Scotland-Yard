import sqlalchemy
from sqlalchemy import create_engine, text

# print(sqlalchemy.__version__)

engine = create_engine("mysql+pymysql://root:changeme%403@localhost/Scotland_Yard?charset=utf8mb4")

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
def add_game_entry(game_id, playerid, role):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("INSERT INTO games_played (gameid, playerid, role) VALUES (:game_id, :playerid, :role)"),
                {"game_id": game_id, "playerid": playerid, "role": role}
            )
            print(f"Game entry added: Game ID {game_id}, Player ID {playerid}, Role {role}")
            conn.commit()
    except Exception as e:
        print(f"Error during insertion: {e}")


def add_player_to_db(player_name, player_score,positions,gameid):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("INSERT INTO players (player_name, playerid, Current_Location, Role) VALUES (:player_name, :player_score, :pos, 'police')"),
                {"player_name": player_name, "player_score": player_score,"pos":positions}
            )
            
            print(f"Player inserted: {player_name}, {player_score}")
            conn.commit()
            '''conn.execute(
                text("INSERT INTO game_history(GameId, PlayerID, TurnNo, Start_pos, End_pos) VALUES (:gid, :pid, 1,0,:pos)"),
                {"gid": gameid, "pid": player_score,"pos":positions}
            )
            conn.commit()'''
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
              

def game_history(gameid):
    try:
        with engine.connect() as conn:
            # Select playerid and turn_no for the given game_id
            result = conn.execute(
                text("SELECT playerid, turnno FROM players"))
            # Iterate over the result and insert into game_history table
            for row in result:
                playerid, turnno = row
                conn.execute(
                    text("INSERT INTO game_history (gameid, playerid, turnno, Start_Pos, End_Pos, Transport ) VALUES (:gameid, :playerid, :turnno, 1, 1, 'T')"),
                    {"gameid": gameid, "playerid": playerid, "turnno": turnno}
                )
            conn.commit()
            print("Game history updated successfully!")
    except Exception as e:
        print(f"Error updating game history: {e}")

# def add_player_role_to_db(role, positions):
#     try:
#         with engine.connect() as conn:
#             # Update all players' role to 'police' and set their positions
#             for player_position, playerid in zip(positions, range(1, len(positions) + 1)):
#                 result1 = conn.execute(
#                     text("UPDATE players SET role='police', turnno=1, taxi=10, bus=8, ug=4, position=:position WHERE playerid=:playerid"),
#                     {"position": player_position, "playerid": playerid}
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
    



  
  