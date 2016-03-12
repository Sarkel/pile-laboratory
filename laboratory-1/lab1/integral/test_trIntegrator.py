from unittest import TestCase
from lab1.integral.TrIntegrator import TrIntegrator
from lab1.integral.testhelper import TestHelper

__author__ = 'Sebastian Kubalski'


class TestTrIntegrator(TestCase):
    def test_integrate(self):
        inputData = [
            TestHelper.createInputData(-1, 1),
            TestHelper.createInputData(0, 1),
            TestHelper.createInputData(2, 3),
            TestHelper.createInputData(0, 20)
        ]
        expectedResults = [0, 0.5, 2.5, 200]

        for index, result in enumerate([TrIntegrator(x).integrate() for x in inputData]):
            self.assertAlmostEquals(expectedResults[index], result)
