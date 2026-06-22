"""Importamos todos los paquetes que vayamos a necesitar"""
import joblib #para poder guardar el archivo en un .pkl
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)#para hacer las métricas de evaluación.

"""Creamos la clase del modelo."""
class AlcoholLogisticModel():
    def __init__(self, random_state=42, max_iter=1000): #ponemos el random_state para que empiece siempre por el mismo punto y el número de iteraciones a 1000 para evitar errores de convergencia.
        self.model = LogisticRegression(random_state=random_state,max_iter=max_iter)
    
    def fit(self, x_train, y_train): #creamos este método para entrenar el modelo.
        self.model.fit(x_train, y_train)
    
    def predict(self, x_test): #este otro para realizar las predicciones.
        return self.model.predict(x_test)
    
    def evaluate(self, x_test, y_test):#y este último para obtener todas las métricas y realizar la evaluación. 
        y_pred = self.predict(x_test)#para eso primero obtenemos la predicción llamando al método anterior.
        return {
            "accuracy": accuracy_score(y_test, y_pred),#nos dice cuantas predicciones acierta, en nuestro caso no será la métrica más precisa por culpa de que hay pocos positivos en los datos.
            "precision": precision_score(y_test, y_pred, zero_division=0),#nos dice cuantas veces acierta un positivo.
            "recall": recall_score(y_test, y_pred),#nos dice cuantos positivos detecta el modelo de todos los que hay.
            "f1": f1_score(y_test, y_pred),#métrica más precisa que combina precisión y recall.
            "confusion_matrix": confusion_matrix(y_test, y_pred)
        }#y creamos un diccionario para almacenar las métricas.
    
    def save_model(self, path="alcohol_model.pkl"):#este modelo para guardaarlo en un .pkl.
        joblib.dump(self.model, path)
    
    def load_model(self, path="alcohol_model.pkl"):#y este para cargarlo.
        self.model = joblib.load(path)