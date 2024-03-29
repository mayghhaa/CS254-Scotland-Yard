# insert into Players (Playername) values (:playername);

# @app.route("/submitform", methods=['post'])
# def submitform():
#   data = request.form
#   add_player_to_db(data)
#   return jsonify(data)


# def add_player_to_db( data):
#   with engine.connect() as conn:
#     query = text(insert into players (player_name, role, turnno, current_location, t
# xi, bus, ug) values (:player1, 'police', 0, 1, 10, 8, 4), (:player2, 'poli
# e', 0, 7, 10, 8, 4), (:player3, 0, 101, 'mrX', 1000, 1000, 1000), (:player
# , 'police', 179, 10, 8, 4), (:player5, 'police', 0, 186, 10, 8, 4);)

#     conn.execute(query,  
#                  player1=data['player1'],
#                  player2=data['player2'],
#                  player3=data['player3'],
#                  player4=data['player4'],
#                  player5=data['player5'])

                  def insert_appointment(appointment_id, appointment_date, appointment_time):
    query = text("INSERT INTO appointment (appointment_id, appointment_date, appointment_time) VALUES (:appointment_id, :appointment_date, :appointment_time)")
    connection.execute(query, {
        'appointment_id': appointment_id,
        'appointment_date': appointment_date,
        'appointment_time': appointment_time
    })
    connection.commit()