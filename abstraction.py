from abc import ABC, abstractmethod
class phone(ABC):
    def phoneBill(self, amount):
        print("Your bill total: ",amount)

    @abstractmethod
    def charge(self, amount):
        pass

class CardPayment(phone):
    def charge(self, amount):
        print("You now owe an amount of {}  since you exceeded your monthly data limit ".format(amount))

obj = CardPayment()
obj.phoneBill("$350")
obj.charge("$350")
