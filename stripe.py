'''
SD-GAL-05 SD-TA-007 Exercise 014
Author: Mary Ronan
Last Modified: 28/01/2026
A Stripe Payment System with OOP Python and Unit Tests
'''

# Required imports
from abc import ABC, abstractmethod
import datetime
import unittest


# Parent Class
class PaymentMethod(ABC):

    # Class Instance
    def __init__(self, custName, amount):
        self.custName = custName
        self.amount = amount

    # Class Getter Functions
    def getCustName(self):
        return self.custName

    def getAmount(self):
         return self.amount

    # Class Methods

    # Display Welcome Message
    def displayWelcomeMessage():
        print("-".ljust(55, "-"))
        print("Welcome to the Stripe Payment System".center(50))
        print("-".ljust(55, "-"))

    # Display Exit Message
    def displayExitMessage():
        print("-".ljust(55, "-"))
        print("Thank you for using the Stripe Payment System".center(50))
        print("-".ljust(55, "-"))

    # Generate Timestamp
    def getTimeStamp(self):
        return datetime.datetime.now().strftime("%c")

    # Abstract Methods
    @abstractmethod
    def printDetails(self):
        print("*".ljust(55, "*"))
        print("Stripe Payment".center(50))
        print("*".ljust(55, "*"))
        print("Customer Name".ljust(25),": ", self.getCustName())
        print("Amount".ljust(25),":  €", self.getAmount())

# Child Class
class CreditCard(PaymentMethod):

    # Class Instance
    def __init__(self, custName, amount):
        super().__init__(custName, amount)

    # Class Setter Functions
    def setCardNumber(self):
        self.cardNumber = input("Enter Credit Card Number: ")

    def setExpiryDate(self):
        self.expiryDate = input("Enter Credit Card Expiry Date[MM/YY]: ")

    def setCardName(self):
        nameOnCard = input(f"Is the Name on the Credit Card {self.getCustName()} [Y/N]: ").upper()
        if nameOnCard == "Y":
            self.cardName = self.getCustName()
        else:
            self.cardName = input("Enter Name on Credit Card: ")

    # Class Getter Functions
    def getCardNumber(self):
        return "*****" + self.cardNumber[-4:]

    def getExpiryDate(self):
        return self.expiryDate

    def getCardName(self):
        return self.cardName

    # Display Payment Details
    def printDetails(self):
        super().printDetails()
        print("Payment Type:".ljust(25),":  Credit Card")
        print("Credit Card Number: ".ljust(25),": ", self.getCardNumber())
        print("Credit Card Name: ".ljust(25),": ", self.getCardName())        
        print("Credit Card Expiry Date: ".ljust(25),": ", self.getExpiryDate())
        print("Transaction Date".ljust(25),": ", self.getTimeStamp())
        print("*".ljust(55, "*"))

# Child Class
class Paypal(PaymentMethod):

    # Class Instance
    def __init__(self, custName, amount):
        super().__init__(custName, amount)

    # Class Setter Functions
    def setEmail(self):
        self.email = input("Enter Email Address: ")

    # Class Getter Functions
    def getEmail(self):
        return self.email


    # Display Payment Details
    def printDetails(self):
        super().printDetails()
        print("Payment Type:".ljust(25),":  PayPal")
        print("PayPal account: ".ljust(25),": ", self.getEmail())
        print("Transaction Date".ljust(25),": ", self.getTimeStamp())
        print("*".ljust(55, "*"))

# MAIN PROGRAM

# Display Greeting
PaymentMethod.displayWelcomeMessage()

#Get User Input
paymentMethod = input("Enter Payment Type [C] for Credit Card or [P] for PayPal ").upper()
custName = input("Enter Customer Name: ")
amount = float(input("Enter Payment Amount: €"))

# Get Transaction Type
if paymentMethod == "C":
    payment = CreditCard(custName, amount)
    payment.setCardNumber()
    payment.setExpiryDate()
    payment.setCardName()
else:
    payment = Paypal(custName, amount)
    payment.setEmail()

# Display Transaction
payment.printDetails()

# Display Exit Message
PaymentMethod.displayExitMessage()

# Unit Testing
class unittests(unittest.TestCase):

    # Test 001 - Check that amount is greater than 0.00
    def test001(self):
        assert payment.getAmount() > 0.0

    # Test 002 - Check Payment is CreditCard object
    def test002(self):
        if paymentMethod == "C":
            self.assertIsInstance(payment, CreditCard)

    # Test 003 - Check Payment is CreditCard object
    def test003(self):
        if paymentMethod == "P":
            self.assertIsInstance(payment, Paypal)

    # Test 004 - Check Paypal email not blank
    def test004(self):
        if paymentMethod == "P":
            assert payment.getEmail() != ""

        
unittest.main()
        
        
