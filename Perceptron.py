import random
from utility import sign


class Perceptron:
    def __init__(self, n):
        # Learning rate used in training
        self.lr = 0.005
        self.n = n
        # Initialise weights randomly
        self.weights = [0]*n
        for i in range(n):
            self.weights[i] = random.uniform(-1, 1)

    def guess(self, inputs):
        total = 0
        for i in range(self.n):
            total += self.weights[i] * inputs[i]
        return sign(total)

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        for i in range(self.n):
            self.weights[i] += error * inputs[i] * self.lr

    def guess_y(self, x):
        w0 = self.weights[0]
        w1 = self.weights[1]
        w2 = self.weights[2]

        return ((w2/w1) + (w0/w1) * x) * -1

