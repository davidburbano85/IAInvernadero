from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def evaluar(
    modelo,
    x_prueba,
    y_prueba
):

    predicciones = modelo.predict(x_prueba)

    return {
        "accuracy": round(
            accuracy_score(y_prueba, predicciones),
            4
        ),
        "precision": round(
            precision_score(y_prueba, predicciones),
            4
        ),
        "recall": round(
            recall_score(y_prueba, predicciones),
            4
        ),
        "f1": round(
            f1_score(y_prueba, predicciones),
            4
        )
    }