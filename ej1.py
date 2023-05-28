#contar la cantidad de veces que se menciona la palabra "universidad"

texto = "La Universidad de los Lagos es una institución estatal fundada en 1993. Esta universidad regional  entrega una contribución significativa al desarrollo sostenible del territorio. Como Universidad sus  pilares fundamentales se basan en la inclusión, pluralismo, conciencia ambiental y participación democrática."
texto.lower
texto.count("universidad")  
sum = texto.count("universidad")
print(sum)
print("La palabra universidad se repiten:",sum)

'''
horas = int(10)
Tdiario = int(12000)
Tnocturno = int(16000)
SalOrdD = Tdiario * horas
SalOrdN = Tnocturno* horas
SalOrdDD = SalOrdD * 0.2
SalOrdND = SalOrdN * 0.3

E1 = SalOrdN * 3 + SalOrdD * 2
print ("El salario del primer trabajador es de: ",int(E1))
E2 = SalOrdN * 3 + SalOrdDD
print ("El salario del segundo trabajador es de: ",int(E2))
E3 = SalOrdD * 3+ SalOrdN + SalOrdND
print ("El salario del tercer trabajador es : ",int(E3))

D = {"Sueldo semanal del empleado 1":int(E1),
     "Sueldo turno diurno diario del empleado 1":int(SalOrdD),
     "Sueldo turno nocturno diario del empleado 1":int(SalOrdN),
     "Sueldo turno diurno Domingo del empleado 1":int(SalOrdDD),
     "Sueldo turno nocturno Domingo del empleado 1":int(SalOrdND),
     "Sueldo semanal del empleado 2":int(E2),
     "Sueldo turno diurno diario del empleado 2":int(SalOrdD),
     "Sueldo turno nocturno diario del empleado 2":int(SalOrdN),
     "Sueldo turno diurno Domingo del empleado 2":int(SalOrdDD),
     "Sueldo turno nocturno Domingo del empleado 2":int(SalOrdND),
     "Sueldo semanal del empleado 3":int(E3),
     "Sueldo turno diurno diario del empleado 3":int(SalOrdD),
     "Sueldo turno nocturno diario del empleado 3":int(SalOrdN),
     "Sueldo turno diurno Domingo del empleado 3":int(SalOrdDD),          
     "Sueldo turno nocturno Domingo del empleado 3":int(SalOrdND)
     }
print(D)
'''