from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Client(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.category = None
        self.account = None

class Bank:
    def __init__(self,obj_client,bank_code):
        self.client = obj_client
        self.bank_code = bank_code

    def insert_client_category(self,regular = False, vip = False, premium = False):
        if regular:
            self.client.category = 'regular'
        elif vip:
            self.client.category = 'vip'
        elif premium:
            self.client.category = 'premium'

    def insert_account(self, agency, acc_number, balance, saving_acc=False, current_acc=False):
        if saving_acc:
            self.client.account = SavingAcc(agency, acc_number, balance,obj_client=self.client)
        elif current_acc:
            self.client.account = CurrentAcc(agency, acc_number, balance,obj_client=self.client)

class Acc(ABC):
    def __init__(self,agency,acc_number,balance):
        self._agency = agency
        self._acc_number = acc_number
        self._balance = balance

    @property
    def agency(self):
        return self._agency
    @property
    def acc_number(self):
        return self._acc_number
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError ('ERRO - Digite um valor válido')
        self._balance = value

    def deposit(self):
        while True:
            try:
                value = float(input('Valor do saque: '))
            except (TypeError, ValueError):
                print('ERRO - Digite um valor válido')
                continue
            else:
                break
        self._balance+=value
        print (f'Voce realizou um depósito de R$ {value:.2f} em sua conta')
        print(f'Saldo atual: {self.balance}')

    @abstractmethod
    def withdraw(self):
        pass

class SavingAcc(Acc):
    def __init__(self,agency,acc_number,balance,obj_client=None):
        super().__init__(agency,acc_number,balance)
        self.obj_client = obj_client

    def withdraw(self):
        while True:
            try:
                value = float(input('Valor do saque: '))
            except (TypeError,ValueError):
                print ('ERRO - Digite um valor válido')
                continue
            else:
                break
        if self.balance > 0 and (self.balance - value) > 0:
            self.balance-=value
            print(f'Valor retirado com sucesso!')
        else:
            print('OPS, saldo insuficiente.')
        self.detail()

    def detail(self):
        client_name = self.obj_client.name
        print (f'Nome: {client_name}\nAgência: {self.agency}\nConta{self.acc_number}\nSaldo:{self.balance}')

class CurrentAcc(Acc):
    def __init__(self,agency,acc_number,balance,obj_client=None):
        super().__init__(agency,acc_number,balance)
        self.obj_client = obj_client
        self.category = obj_client.category
        print(self.obj_client)
        if self.category == 'regular':
            self.day_limit = 10000
            self.overdraft = -800
        elif self.category == 'vip':
            self.day_limit = 50000
            self.overdraft = -5000
        elif self.category == 'premium':
            self.overdraft = -20000

    def withdraw(self):
        while True:
            try:
                value = float(input('Valor do saque: '))
            except (TypeError, ValueError):
                print('ERRO - Digite um valor válido')
                continue
            else:
                break
        if self.obj_client.category !='premium' and value > self.day_limit:
                print(f'Ops, valor de transferência acima do limite.\n'
                      f'Seu cadastro é {self.obj_client.category}\n'
                      f'limite diário: {self.day_limit}')
        if (self.balance - value) < self.overdraft:
            print(f'Ops,  seu limite de cheque espécial é {self.overdraft}\n')
        else:
            self.balance-=value
            print(f'Valor transferido com sucesso!')
        self.detail()

    def detail(self):
        client_name = self.obj_client.name
        print (f'Nome: {client_name}\nAgência: {self.agency}\nConta{self.acc_number}\nSaldo:{self.balance}')







