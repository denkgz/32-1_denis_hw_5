from random import randint
from decouple import config


class Casino:
    def __init__(self):
        self.__slots = randint(1,30)
        self.__my_money = config('MY_MONEY',default = 1000,cast = int)

    @property
    def money(self):
            return self.__my_money

    @money.setter
    def money(self, value):
            self.__my_money = value

    def play_round(self):
        while True:
            print(f'\nВаш кошелек составляет - {self.money}')
            bet_money = int(input('Сколько вы желаете поставить денег?  '))
            select_slots = int(input('Выберите слоту 1-30 -  '))
            if 0 <= bet_money <= self.__my_money and 1 <= select_slots <= 30:
                if select_slots == self.__slots:
                    self.money = int(self.__my_money * 2)
                    print(f'Вы выиграли, ваша сумма увеличивается в 2 раза!!'
                          f'\nВаш кошелек {self.__my_money}')
                else:
                    self.money = int(self.money - bet_money)
                    print(f'Вы проиграли все поставленные деньги!!'
                          f'\nВаш кошелек {self.__my_money}')
            else:
                print(f'Ваша ставка не должна превышать {self.money}'
                      f'\nСлоты от 1 - 30!!!')
            if self.money <= 0:
                break
            play_or_dont = input('Желаете продолжить игру,напишите ДА или НЕТ - ').lower()
            if play_or_dont == 'нет':
                break
