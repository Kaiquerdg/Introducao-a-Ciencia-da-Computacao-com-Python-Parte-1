tempo = int(input("Por favor, entre com o npumero de segundos que deseja converter:"))

dias = tempo // 86400
horasrest = tempo % 86400
horas = horasrest // 3600
minrest = horasrest % 3600
minuto = minrest // 60
seg = minrest % 60

print(dias, "dias,", horas, "horas,", minuto, "minutos e", seg, "segundos." )