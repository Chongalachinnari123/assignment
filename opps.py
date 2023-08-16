class Bankaccount:
    def _init_(self,accountnumber,balance):
        self._acNo =  accountnumber
        self._bal = balance
    def withdraw(self,amount):
        if amount > self._bal:
            print("insufficient balance")
        else:
            self._bal = self._bal - amount     
result = Bankaccount(1643 , 3000)
print(result._bal)          