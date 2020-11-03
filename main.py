import json
from jugadores import FootballPlayer, BasketballPlayer

print("¡ingresa algunas datos de jugadores de futbol!")

f_name = input("introduce el nombre del jugador: ")
l_name = input("introduze el apellido del jugador: ")
height = input("introduce la altura del jugador: ")
weight = input("introduce el peso del jugador: ")
goals = input("introduce los goles del jugador: ")
y_cards = input("introduce el numero de tarjetas amarillas del jugador:")
r_cards = input("introduce el numero de tarjetas rojas del jugador: ")

nuevo_jugador = FootballPlayer(first_name= f_name,last_name= l_name,height_cm= height,
                               weight_kg= float(weight), goals=int(goals),
                               yellow_cards=int(y_cards), red_cards=int(r_cards))

with open("jugadores.json", "w") as fd:
    fd.write(json.dumps(nuevo_jugador.to_dict()))

print("!el jugador se ingreso con exito¡")

kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

print(kev_dur.last_name)
print(kev_dur.rebounds)
print(kev_dur.weight_to_lbs())

messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

print(messi.first_name)
print(messi.goals)
print(messi.weight_to_lbs())

