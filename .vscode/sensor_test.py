sensor = "sensor de temperatura"
valor = 15

if valor > 0.2 and sensor == "sensor de temperatura":
    registro = valor
    print ("El " + sensor + " ha registrado el valor " + str(registro))
else:
    print ("El valor registrado es incorrecto o las mediciones vienen de un sensor desconocido")