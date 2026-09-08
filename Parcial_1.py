import json, os

class Transaccion():
    def __init__(self, id:int, titular:str, valor:int, hora:int, pais:str, dispositivo_conocido:bool, puntaje:int, clasificacion:str):
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
        if not isinstance(puntaje,int):
            raise ValueError("Error datos incorrectos")
        if not isinstance(clasificacion,str):
            raise ValueError("Error datos incorrectos")

        self.id = id
        self.titular = titular
        self.valor = valor
        self.hora = hora
        self.pais = pais
        self.dispositivo_conocido = dispositivo_conocido
        self.puntaje = puntaje
        self.clasificacion = clasificacion

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
    return [

    ]

transacciones = cargar_transacciones()

def guardar_transacciones(transaccion):
    transacciones = [t.to_dict() for t in transaccion]
    with open ("transacciones.json", "w", encoding="utf-8", ) as t:
        json.dump(transacciones, t, indent=4, ensure_ascii=False)

