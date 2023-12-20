# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):
    
    ### YOUR CODE HERE
    def basicinfo(self):
        print('This is a generic')
        return 'Generic bank: 0'
        
    @abstractmethod
    def withdraw():
        pass

# Class Swiss
class Swiss(Bank):
    
    ### YOUR CODE HERE
    def __init__(self):
        self.bal = 1000

    def basicinfo(self):
        print("This is the Swiss Bank")
        return "Swiss Bank: " + str(self.bal)

    def withdraw(self, amount):
        if amount > self.bal:
            print("Insufficient funds")
            return self.bal
        self.bal = self.bal - amount

        print("Withdrawn amount: {}".format(amount))
        print("New Balance: {}".format(self.bal))
        return self.bal

# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()
