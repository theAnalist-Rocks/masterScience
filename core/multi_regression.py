from typing import Union, List

import numpy as np
from numpy import ndarray


class MultiRegressionNeuron:
    weights = []

    def __init__(self, sample: List[Union[ndarray, list]], metadata: Union[int, int]):
        self.samples, self.sample_output, self.metadata = *sample, metadata
        self.b = np.random.normal(0.0, 1, None)
        self.weights = np.array([np.random.normal(0.0, 1, None) for i in range(self.metadata)])
        self.model = lambda x: self.weights * x
        self.error = 0.0
        if np.linalg.det(self.samples) == 0:
            raise "Single Matrix"

    def lsq(self, X: ndarray, Y: ndarray):
        try:
            params = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
            return params
        except:
            raise "Inversion is impossible"

    def train(self, time=100, tol=0.01):
        cpt = 0
        while cpt != time:
            if ((self.sample_output - self.model(self.samples))**2 < tol).all() or \
                    ((self.sample_output - self.model(self.samples))**2 == 0).all():
                break
            self.weights = self.lsq(self.samples, self.sample_output)
            cpt += 1

    def predict(self, x: ndarray):
        return self.model(x).sum()

    def think(self, x: ndarray):
        self.train()
        return self.predict(x)


brain = MultiRegressionNeuron([np.array([[2, 4, 6], [1, 10, 3], [1, 4, 7]]), np.array([12, 22, 10])], 3)
x = brain.think(np.array([3, 10, 1]))
print(x)