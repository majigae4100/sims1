import logging
from logexample import CustomLog

class Tester:
    def __init__(self, digit1:int, digit2:int, operation:str, result):
        self.Digit1 = digit1
        self.Digit2 = digit2
        self.Operation = operation
        self.Result = result
        logger = CustomLog('logs.log', logging.ERROR)
        logger.SetUpConfig()
    def CheckCalculate(self):
        try:
            if (self.Operation.lower() == '+'):
                assert self.Digit1 + self.Digit2 == self.Result, f"{self.Digit1}{self.Operation}{self.Digit2} != {self.Result} wrong answer"
            elif (self.Operation.lower() == '-'):
                assert self.Digit1 - self.Digit2 == self.Result, f"{self.Digit1}{self.Operation}{self.Digit2} != {self.Result} wrong answer"
            elif (self.Operation.lower() == '//'):
                assert self.Digit1 / self.Digit2 == self.Result, f"{self.Digit1}{self.Operation}{self.Digit2} != {self.Result} wrong answer"
            elif (self.Operation.lower() == '*'):
                assert self.Digit1 * self.Digit2 == self.Result, f"{self.Digit1}{self.Operation}{self.Digit2} != {self.Result} wrong answer"
        except AssertionError as ae:
            logging.error(ae)