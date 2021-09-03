from atm_card import AtmCard

class Customer:
    def __init__(self, id, custPin, custBalance):
        self.id = id
        self.pin = custPin
        self.balance = custBalance

    def checkId(self):
        return self.id

    def checkPin(self):
        return self.pin

    def changePin(self, newPin):
        self.pin = newPin

    def checkBalance(self):
        return self.balance

    def withdrawBalance(self, nominal):
        self.balance -= nominal
    
    def depositBalance(self, nominal):
        self.balance += nominal