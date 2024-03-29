import datetime
import csv
import os
import matplotlib.pyplot as plt

ruta_carpeta = r'\MACHINE-LEARNING\IMC_Calculadora\datos.csv'
ruta_csv = os.path.join(ruta_carpeta, 'datos.csv')

def determinar_estado_IMC(IMC):
    switch = {
        1: "Bajo peso",
        2: "Peso normal",
        3: "Pre-obesidad o Sobrepeso",
        4: "Obesidad clase I",
        5: "Obesidad clase II",
        6: "Obesidad clase III"
    }
    return switch.get(IMC, "Estado no definido")

def obtener_estado_segun_IMC(IMC):
    if IMC < 18.5:
        return 1
    elif 18.5 <= IMC < 25.0:
        return 2
    elif 25.0 <= IMC < 30.0:
        return 3
    elif 30.0 <= IMC < 35.0:
        return 4
    elif 35.0 <= IMC < 40.0:
        return 5
    else:
        return 6

def calcular_IMC(peso, altura):
    return peso / altura ** 2

def mostrar_fecha_hora():
    now = datetime.datetime.now()
    print("Fecha y hora actual:", now.strftime("%Y-%m-%d %H:%M:%S"))

def registrar_datos_csv(IMC, estado_IMC):
    now = datetime.datetime.now()
    with open(ruta_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([now.strftime("%Y-%m-%d"), IMC, estado_IMC])

def leer_datos_csv():
    datos_registrados = []
    with open(ruta_csv, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            datos_registrados.append((datetime.datetime.strptime(row[0], "%Y-%m-%d"), float(row[1]), row[2]))
    return datos_registrados

def mostrar_grafica():
    datos_registrados = leer_datos_csv()
    fechas = [registro[0] for registro in datos_registrados]
    IMCs = [registro[1] for registro in datos_registrados]
    plt.plot(fechas, IMCs)
    plt.title('Registro de IMC a lo largo del año')
    plt.xlabel('Fecha')
    plt.ylabel('IMC')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    print("\n¡HOLA!\n Este es un menú para saber más sobre tu anatomía, y si tu estado físico es correcto.\n Podrás observar que se pueden calcular y guardar información que proporciones. \n ¡Ahí van los primeros pasos!:")
    while True:
        print("\nMENU:")
        print("1. Calcular IMC")
        print("2. Mostrar fecha y hora")
        print("3. Mostrar gráfica de IMC")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            peso = float(input("Introduce tu peso en kilogramos: "))
            altura = float(input("Introduce tu altura en metros: "))
            IMC = calcular_IMC(peso, altura)
            estado_IMC = determinar_estado_IMC(obtener_estado_segun_IMC(IMC))
            print(f"Tu IMC es: {IMC}")
            print(f"Estado: {estado_IMC}")
            registrar_datos_csv(IMC, estado_IMC)
        elif opcion == "2":
            mostrar_fecha_hora()
        elif opcion == "3":
            mostrar_grafica()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
