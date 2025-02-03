# import torch
# import torch.nn as nn
# import torch.optim as optim

# class CNN(nn.Module):
#     def __init__(self):
#         super(CNN, self).__init__()
#         self.fc1 = nn.Linear(10, 50)
#         self.fc2 = nn.Linear(50, 1)
    
#     def forward(self, x):
#         x = torch.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x

# model = CNN()

# class Car:
#     def __init__(self, mark: str, model: str, year: int):
#         self.mark = mark
#         self.model = model
#         self.year = year

#     def info(self):
#         print(f'My car is {self.mark} {self.model} and {self.year} year')

# some_car = Car('Opel', 'Antara', 2010)
# some_car.info()

# class Animal:
#     def speak(self):
#         return 'some_voice'

# class Dog(Animal):
#     def speak(self):
#         return 'Woof'

# class Cat(Animal):
#     def speak(self):
#         return 'Myaaa'

# dog = Dog()
# cat = Cat()

# print(dog.speak())
# print(cat.speak())

# class BankAccount:
#     def __init__(self, initial_balance: float):
#         self._balance = initial_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount

#     def withdraw(self, take):
#         if self._balance > 0 and self._balance >= take:
#             self._balance -= take

#     def check_balance(self):
#         return self._balance

# sum_of_money = BankAccount(100)
# # sum_of_money.deposit(50)
# sum_of_money.withdraw(200)
# print(sum_of_money.check_balance())

# class MySet:
#     def __init__(self, set):
#         self._setik = set

#     def __len__(self):
#         return len(self._setik)

# anything = MySet({1, 2, 3, 4})
# print(len(anything))

import torch

# sx = torch.tensor([[1, 5, 6], [2, 3, 4]], dtype=torch.float64)

# print(torch.cpu.is_available())
# print(torch.cuda.is_available())

sx = torch.tensor([[1, 5, 6], [2, 3, 4]], dtype=torch.float64, requires_grad=True)
# sx.to('cuda')
device = 'cuda' if torch.cuda.is_available() else 'cpu'
new_tensor = sx.to(device).detach()
print(new_tensor)