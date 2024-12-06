players = {
            "MICHAEL JORDAN": "El mejor jugador de basketball de todos los tiempos",
            "KAWHI LEONARD": "El mejor defensa de todos los tiempos",
            "STEPH CURRY": "El mejor tirador de 3 puntos en la NBA",
            "NIKOLA JOKIC": "El mejor jugador europeo de la NBA",
            }
jugadores = input("Escribe un jugador que quieras conocer (¡con mayúsculas!): ")

if jugadores in players.keys():
    print(players[jugadores])
else:
   print("No conozco a ese jugador")
