import random


class Perceptron:
    def __init__(self):
        # Learning rate used in training
        self.lr = 0.1
        # Initialise weights randomly
        self.weights = [0]*2
        for i in range(2):
            self.weights[i] = random.uniform(-1, 1)

    def guess(self, inputs):
        total = 0
        for i in range(2):
            total += self.weights[i] * inputs[i]
        return sign(total)

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        for i in range(2):
            self.weights[i] += error * inputs[i] * self.lr


# Activation function
def sign(n):
    if n > 0:
        return 1
    else:
        return -1

