# Parcial — Detector de Transmisiones Sospechosas

Nombre: Nezareth Gonzalez Sanchez
Código: Sistema Antifraude
Grupo: 4E 

## 1. ¿Qué debe hacer el programa?

Escriba en máximo 3 o 4 líneas cuál es el objetivo del programa.

Respuesta:

--- El objetivo del programa es registrar transacciones y analizar automaticamente el nivel de riesgo de cada operacion. Tambien debera darle un puntaje a cada transaccion y clasificarla en base a el puntaje obtenido.

## 2. Clase `Transmision`

La clase tendrá los siguientes atributos:

- `id`: Es el codigo unico que identifica cada transaccion
- `titular`: El nombre de quien hace la transaccion
- `valor`: La cantidad de dinero que se ingresa al momento de hacer la transaccion
- `hora`: La hora a la que se hace la transaccion
- `pais`: El pais del cual es la transaccion se originó
- `dispositivo_conocido`: 
- `puntaje_riesgo`: El valor del riesgo de la transaccion y el valor segun cada condicion
- `clasificacion`: La clasificacion segun el puntaje

Escriba brevemente qué representa cada uno.
 
---

## 3. Métodos

### `analizar()`

Responsabilidad: Analiza la transaccion

### `clasificar()`

Responsabilidad: La clasifica segun el puntaje

### `to_dict()`

Responsabilidad: Convierte un objeto a un diccionario json

### `from_dict()`

Responsabilidad: Convierte un diccionario json a un objeto

---

## 4. Algoritmo de análisis

Complete el siguiente pseudocódigo:

```text
puntaje = 0

SI la condicion contiene Valor mayor o igual a $2.000.000
    sumar +30 puntos

SI la condicion contiene Hora entre 0 y 5
    sumar +20

SI la condicion contiene País diferente de Colombia
    sumar +25 puntos

SI la condicion contiene Dispositivo NO conocido
    sumar +30 puntos


```

---

## 5. Persistencia

Explique brevemente qué ocurre al iniciar el programa:

```text
JSON
 ↓
lista de diccionario
 ↓
objeto from_dict()
```

Explique qué ocurre al guardar:

```text
Objetos
 ↓
diccionario to_dict()
 ↓
JSON
```

---

## 6. Menú

Indique qué debe hacer cada opción:

### Opción 1 — Registrar transaccion

1.  Pide nombre_titular, valor, hora, pais, dispositivo_conocido
2.  Se le asigna id
3.  Se guarda en la clase

### Opción 2 — Listar transacciones

1.  Muestra las transacciones
2.  Muestra el puntaje y la clasificacion en base al puntaje

### Opción 3 — Salir

Acción:

--- Sale del programa

## Nota

Este archivo debe completarse durante los primeros 15 minutos del parcial, antes de comenzar la implementación.