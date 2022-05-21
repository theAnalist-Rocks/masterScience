import numpy as np
from typing import Union


class SimpleRegressionNeuron:
    weights = 1

    def __init__(self, sample: Union[np.array, np.array], metadata: Union[int, int]):
        self.samples, self.sample_output, self.metadata = *sample, metadata
        self.b = np.random.normal(0.0, 1, None)
        self.model = lambda x: self.weights * x + self.b

    def gradient(self, weighted=True, **kwargs):
        if weighted:
            return kwargs['a'] - kwargs['alpha'] * np.sum(
                self.samples * (self.weights * self.samples + self.b - self.sample_output)) / self.metadata
        return kwargs['b'] - kwargs['alpha'] * np.sum(
            self.weights * self.samples + self.b - self.sample_output) / self.metadata

    def train(self, learning_rate: float, time=500):
        cpt = 0
        while cpt != time:
            self.weights = self.gradient(a=self.weights, alpha=learning_rate)
            self.b = self.gradient(weighted=False, b=self.b, alpha=learning_rate)
            if (self.model(self.samples[1]) - self.sample_output[1]) ** 2 == 0:
                break
            cpt += 1

    def think(self, inputed: float):
        self.train(0.1, 100000)
        return self.model(inputed)


brain = SimpleRegressionNeuron(sample=[np.array([2, 3, 4, 5, 6]),
                      np.array([6, 8, 10, 12, 14]),
                      ],
              metadata=5
              )
x = brain.think(0)
print("Predicted Value: ", x)
