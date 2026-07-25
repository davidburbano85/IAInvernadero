from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from config.configuracion import SEMILLA


def entrenar(datos):

    entrenamiento, prueba = train_test_split(
        datos,
        test_size=0.2,
        random_state=SEMILLA
    )

    y_entrenamiento = entrenamiento["Clase"]
    y_prueba = prueba["Clase"]

    x_entrenamiento = entrenamiento.drop(
        columns=[
            "Clase",
            "magnitud",
        ]
    )

    x_prueba = prueba.drop(
        columns=[
            "Clase",
            "magnitud",
        ]
    )

    modelo = RandomForestClassifier(
        n_estimators=100,
        random_state=SEMILLA
    )

    modelo.fit(
        x_entrenamiento,
        y_entrenamiento
    )

    return modelo, x_prueba, y_prueba, prueba