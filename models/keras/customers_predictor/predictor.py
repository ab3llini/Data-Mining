import keras as k
import numpy as np
import os

class CustomerPredictor:

    def __init__(self, n, name=""):
        self.models = []
        self.n = n
        _dir = os.path.dirname(os.path.abspath(__file__))
        for i in range(n):
            self.models.append(k.models.load_model(os.path.join(_dir, "mod" + name + str(i) + ".h5")))

    def predict(self, x):
        preds = np.zeros(len(x))
        for i in range(self.n):
            p = self.models[i].predict(x).squeeze()
            preds += p
        preds[preds < 0] = 0
        return preds
