__author__ = 'Sebastian Kubalski'

#Engine class for integration
class TrIntegrator:
    #constructor
    def __init__(self, inputData):
        self.rank = inputData['rank']
        self.params = list(reversed(inputData['params']))
        self.first = inputData['first']
        self.last = inputData['last']
        self.numberOfDivisions = inputData['numberOfDivisions']

    #main method which count integral
    def integrate(self):
        h = (self.last - self.first) / self.numberOfDivisions
        integral = 0
        currentValue = self.first
        for n in range(self.numberOfDivisions):
            integral += self._function(currentValue + h * n)
            integral += self._function(currentValue + h * (n + 1))
        return (h / 2) * integral

    #method to return value of polynomial
    def _function(self, value):
        counter = 0
        for x in range(self.rank + 1):
            counter += pow(value, x) * self.params[x]
        return counter
