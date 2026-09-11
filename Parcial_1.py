import json, os

class Transaccion():
    def __init__(self, id:int, titular:str, valor:int, hora:int, pais:str, dispositivo_conocido:bool, puntaje=None, clasificacion=None):
        
        if not isinstance(id,int):
            raise ValueError("Error datos incorrectos")
        if not isinstance(titular,str):
            raise ValueError("Error datos incorrectos")
        if not isinstance(valor,int):
            raise ValueError("Error datos incorrectos")
        if not isinstance(hora,int):
            raise ValueError("Error datos incorrectos")
        if not isinstance(pais,str):
            raise ValueError("Error datos incorrectos")
        if not isinstance(dispositivo_conocido,bool):
            raise ValueError("Error datos incorrectos")

        self.id = id
        self.titular = titular
        self.valor = valor
        self.hora = hora
        self.pais = pais
        self.dispositivo_conocido = dispositivo_conocido
        self.puntaje = puntaje
        self.clasificacion = clasificacion
        
        if puntaje is None:
            self.calcular_riesgo()
            self.clasificar()

    def calcular_riesgo(self):
        self.puntaje = 0
        if self.valor >= 2000000:
            self.puntaje = self.puntaje + 30
        if self.hora >= 0 and self.hora <= 5:
            self.puntaje = self.puntaje + 20
        if self.pais.lower() != "colombia":
            self.puntaje = self.puntaje + 25
        if self.dispositivo_conocido == False:
            self.puntaje = self.puntaje + 30
        return self.puntaje

    def clasificar(self):
        if self.puntaje >= 0 and self.puntaje <= 29:
            self.clasificacion = "normal".upper()
        if self.puntaje >= 30 and self.puntaje <= 59:
            self.clasificacion = "sospechosa".upper()
        if self.puntaje >= 60:
            self.clasificacion = "alto riesgo".upper()
        return self.clasificacion

    def to_dict(self):
        return {"id" : self.id, "titular" : self.titular, "valor" : self.valor, "hora" : self.hora, "pais" : self.pais, "dispositivo_conocido" : self.dispositivo_conocido, "puntaje" : self.puntaje, "clasificacion" : self.clasificacion}

    @classmethod
    def from_dict(cls, datos):
            return cls(
                id = datos["id"],
                titular = datos["titular"],
                valor = datos["valor"],
                hora = datos["hora"],
                pais = datos["pais"],
                dispositivo_conocido = datos["dispositivo_conocido"],
                puntaje = datos["puntaje"],
                clasificacion = datos["clasificacion"]
            )

def cargar_transacciones():
    if os.path.exists("transacciones.json"):
        with open ("transacciones.json", "r", encoding="utf-8") as archivo:
            transacciones = json.load(archivo)
        return [Transaccion.from_dict(d) for d in transacciones]
    return []

transacciones = cargar_transacciones()
def guardar_transacciones(transaccion):
    transacciones = [t.to_dict() for t in transaccion]
    with open ("transacciones.json", "w", encoding="utf-8", ) as t:
        json.dump(transacciones, t, indent=4, ensure_ascii=False)

def menu():
    print(f"\n" , " MENÚ - Sistema Antifraude ".center(50, "="))

    print(  "|                                                  |\n"
            "| 1. Registrar Nueva Transacción                   |\n"
            "|                                                  |\n"
            "| 2. Listar Transacciones                          |\n"
            "|                                                  |\n"
            "| 3. Buscar Transaccion por ID                     |\n"
            "|                                                  |\n"
            "| 4. Eliminar Transaccion                          |\n"
            "|                                                  |\n"
            "| 5. Guardar y Salir                               |\n"
            " ================================================== \n"
    )

def registrar():
    print("Registrando nueva Transaccion...")

    while True:
        new_id = len(transacciones) + 1
        new_titular = input("Ingrese Nombre del titular: ")
        if new_titular == "" or new_titular == " ":
            print("¡ERROR, No deje este espacio vacio!")
            continue

        new_valor_texto = input("Ingrese el Valor de la Transaccion: ")
        try:
            new_valor = int(new_valor_texto)
        except ValueError:
            print("¡ERROR, Ingrese un valor numerico valido!")
            continue
        if new_valor < 0:
            print("¡ERROR, Ingrese un Valor mayor a cero!")
            continue

        new_hora_texto = input("Ingrese la hora de la transaccion (0-23): ")
        try:
            new_hora = int(new_hora_texto)
        except ValueError:
            print("¡ERROR, Ingrese una hora numerica valida!")
            continue
        if new_hora < 0 or new_hora > 23:
            print("¡ERROR, Ingrese la hora entre 0-23!")
            continue

        new_pais = input("Ingrese el pais: ")
        if new_pais == "" or new_pais == " ":
            print("¡ERROR, No deje este espacio vacio!")
            continue
        new_disp_conocido = (input("El dispositivo es conocido? (S/N): ").upper() == "S")

        nueva_transaccion = Transaccion(new_id, new_titular, new_valor, new_hora, new_pais, new_disp_conocido)

        transacciones.append(nueva_transaccion)
        print(f"¡Transaccion registrada con exito! Puntaje: {nueva_transaccion.puntaje}, Clasificacion: {nueva_transaccion.clasificar()}")

        guardar_transacciones(transacciones)
        break

def listar():
    if not transacciones:
        print("\n¡No hay transacciones registradas!\n")
        return

    print("\n" + "=" * 170, "\n",
            f"{'ID'}".ljust(10),
            f"{'TITULAR'}".ljust(20),
            f"{'VALOR'}".ljust(20),
            f"{'HORA'}".ljust(20),
            f"{'PAIS'}".ljust(25),
            f"{'DISPOSITIVO_CONOCIDO'}".ljust(30),
            f"{'PUNTAJE_RIESGO'}".ljust(20),
            f"{'CLASIFICACION'}".ljust(15), "\n" + "=" * 170
    )

    for t in transacciones:
        print(  f" {t.id}".ljust(12),
                f"{t.titular}".ljust(18),
                f"{t.valor}".ljust(23),
                f"{t.hora}".ljust(17),
                f"{t.pais}".ljust(28),
                f"{t.dispositivo_conocido}".ljust(33),
                f"{t.puntaje}".ljust(16),
                f"{t.clasificacion}".ljust(15),
        )

def buscar():
    print("Buscando Transaccion...")

    if not transacciones:
        print("\n¡No hay transacciones registradas!\n")
        return

    id_texto = input("Ingrese el ID de la transaccion que desea buscar: ")
    try:
        id_buscar = int(id_texto)
    except ValueError:
        print("¡ERROR, Ingrese un ID numerico valido!")
        return

    id_encontrado = False

    for t in transacciones:
        if id_buscar == t.id:
            print("\n" + "=" * 170, "\n",
                f"{'ID'}".ljust(10),
                f"{'TITULAR'}".ljust(20),
                f"{'VALOR'}".ljust(20),
                f"{'HORA'}".ljust(20),
                f"{'PAIS'}".ljust(25),
                f"{'DISPOSITIVO_CONOCIDO'}".ljust(30),
                f"{'PUNTAJE_RIESGO'}".ljust(20),
                f"{'CLASIFICACION'}".ljust(15), "\n" + "=" * 170
            )

            print(  f" {t.id}".ljust(12),
                f"{t.titular}".ljust(18),
                f"{t.valor}".ljust(23),
                f"{t.hora}".ljust(17),
                f"{t.pais}".ljust(28),
                f"{t.dispositivo_conocido}".ljust(33),
                f"{t.puntaje}".ljust(16),
                f"{t.clasificacion}".ljust(15),
            )
            id_encontrado = True
    if id_encontrado == False:
        print("¡ERROR, ID no encontrado!")
        
def borrar():
    print("Eliminando Transaccion...")

    if not transacciones:
        print("\n¡No hay transacciones registradas!\n")
        return

    id_texto = input("Ingrese el ID de la transaccion que desea Eliminar: ")
    try:
        id_buscar = int(id_texto)
    except ValueError:
        print("¡ERROR, Ingrese un ID numerico valido!")
        return

    id_encontrado = False
    for t in transacciones:
        if id_buscar == t.id:
            id_encontrado = True
            transacciones.remove(t)
            print("¡Transaccion Eliminada con Exito!")
            break

    if id_encontrado == False:
        print("¡ERROR, El ID ingresado no se encuentra en nuestra base de Datos!")
    else:
        for indice, t in enumerate(transacciones):
            t.id = indice + 1
        guardar_transacciones(transacciones)


def main():
    while True:
        menu()
        opcion_texto = input("Ingrese una opcion: ")

        try:
            opcion = int(opcion_texto)
        except ValueError:
            print("¡ERROR, Ingrese un numero valido!")
            continue

        match opcion:
            case 1 :
                registrar()
            case 2 :
                listar()
            case 3:
                buscar()
            case 4:
                borrar()
            case 5:
                guardar_transacciones(transacciones)
                break
            case _:
                print("¡ERROR, Opcion invalida!")

main()
