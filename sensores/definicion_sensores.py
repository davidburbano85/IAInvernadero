# Definición central de sensores del sistema


SENSORES = {

    "pH": {
        "nombre": "Sensor de pH",
        "unidad": "",
        "minimo": 4.5,
        "maximo": 9.0,
        "activo": True
    },


    "Humedad": {
        "nombre": "Sensor de humedad del suelo",
        "unidad": "%",
        "minimo": 10,
        "maximo": 80,
        "activo": True
    },


    "Conductividad": {
        "nombre": "Sensor de conductividad eléctrica",
        "unidad": "mS/cm",
        "minimo": 0.1,
        "maximo": 5.0,
        "activo": True
    },


    "Temperatura": {
        "nombre": "Sensor de temperatura del suelo",
        "unidad": "°C",
        "minimo": 0,
        "maximo": 50,
        "activo": True
    },


    "Nitrogeno": {
        "nombre": "Sensor de nitrógeno",
        "unidad": "ppm",
        "minimo": 0,
        "maximo": 100,
        "activo": True
    },


    "Fosforo": {
        "nombre": "Sensor de fósforo",
        "unidad": "ppm",
        "minimo": 0,
        "maximo": 100,
        "activo": True
    },


    "Potasio": {
        "nombre": "Sensor de potasio",
        "unidad": "ppm",
        "minimo": 0,
        "maximo": 200,
        "activo": True
    }

}