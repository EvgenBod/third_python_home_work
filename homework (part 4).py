# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов.
# Вам необходимо написать программу, которая позволит составить список гостей.
# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Customers:
    def __init__(self,first_name,last_name,city,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"«{self.first_name} {self.last_name}. {self.city}. Баланс: {self.balance} руб.»"

    def get_guest(self):
        return f'{self.first_name} {self.last_name}, г.{self.city}'

guest_1 = Customers('Иван','Петров','Москва',50)
guest_2 = Customers('Владимир','Зайцев','Кострома',50)
guest_3 = Customers('Олеся','Янина','Новосибирск',50)

guest_list = [guest_1, guest_2, guest_3]

for guest in guest_list:
    print(guest.get_guest())