# HORAS PROLONGACIÓN JORNADA

def calculo_horario_semana():
    pregunta_dias_trabajo_semana = int(input("\nIndica cuántos días a la semana trabaja el empleado: "))
    numero_dias_trabajo_semana = pregunta_dias_trabajo_semana
    print("\n")
    
    contador_dias = 0
    lista_dias_trabajo_semana = []
    print("Indica los días de la semana. Después de cada día introducido, pulsa enter.")
    while contador_dias < numero_dias_trabajo_semana:
            dias_semana = input()
            contador_dias += 1
            lista_dias_trabajo_semana.append (dias_semana)
           
    print("\n")
    contador_horas = 0
    lista_horas_dias_trabajo_semana = []
    print("Indica cuantas horas trabaja cada día. Después de cada hora introducida, pulsa enter.")
    while contador_horas < numero_dias_trabajo_semana:
        for indice, dia in enumerate (lista_dias_trabajo_semana):
            print(dia,":")
            horas_semana = float(input())
            contador_horas += 1
            lista_horas_dias_trabajo_semana.append (horas_semana)
   
    horas_prolongacion_jornada = (sum(lista_horas_dias_trabajo_semana) - 40) / 5


    total_horas_trabajadas_semana = sum(lista_horas_dias_trabajo_semana)
    print("\nEl empleado trabaja de", lista_dias_trabajo_semana [0], "a", lista_dias_trabajo_semana[-1],"." )
    print("Trabaja un total de", numero_dias_trabajo_semana, "días a la semana.")
    print("\nY hace un total de:", total_horas_trabajadas_semana, """horas de trabajo a la semana, siendo""", 
    horas_prolongacion_jornada, """las horas de prolongación jornada que hace al día""" )

    return horas_prolongacion_jornada


def calculo_dias_laborables_año():
    
    dias_año = 365
    sabados = 48
    domingos = 48
    festivos = 14
    vacaciones = 22
    suma_dias_no_laborables = (sabados+domingos+festivos+vacaciones)
    
    dias_laborables_año = dias_año - suma_dias_no_laborables

    return dias_laborables_año



if __name__ == "__main__":
    print("Cálculo HORAS PROLONGACIÓN JORNADA")
    print("Bienvenido al programa para calcular las horas de prolongación de jornada al mes que realiza el trabajador.")
    
    comunidad = input("\nIntroduce la comunidad de propietarios: ")
    empleado = input("Introduce nombre y apellidos del empleado: ") 
    
    resultado_horas_prolongacion_jornada_dia = calculo_horario_semana()
    resultado_dias_laborables_año = calculo_dias_laborables_año()
    horas_prolongación_jornada_mes = (resultado_horas_prolongacion_jornada_dia * resultado_dias_laborables_año) / 11
    
    print("\n",resultado_horas_prolongacion_jornada_dia,"horas prolongación jornada al día")
    print("X")
    print(resultado_dias_laborables_año,"dias laborables al año sin vacaciones, y entre once meses laborables")
    print("____________")
    print("{:05.2f}" .format(horas_prolongación_jornada_mes),"HORAS PROLONGACIÓN JORNADA AL MES")
    