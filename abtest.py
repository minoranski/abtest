# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 11:20:43 2022

@author: User
"""
'''
class Client:
    ID = 0
    Group = 0
    
    def __init__(self, ID, Group):
        self.ID = ID
        self.Group = Group
    
class Group:
    Num = 0
    Clients = 0
    
    def __init__(self, Num, Clients):
        self.Num = Num
        self.Client = Clients
        
def numOfCustomers(n_customers):
    for Num in Groups.keys():
        for ID in Clients.keys():
            if Clients[ID] == Num:
                Groups[Num] += 1
    print(Groups)
            
        
#clientIDs = [7412567, 4563782, 8967223, 1421216, 3564517]
Clients = {7412567 : 0, 4563782 : 0, 8967223 : 0, 1421216 : 0, 3564517 : 0}
Groups = {}
Sum = 0
for ID in Clients.keys():
    saveID = ID
    while ID > 0:
        Sum += ID % 10
        ID //= 10
    if (Sum not in Groups.keys()):
        Groups[Sum] = 0
        Clients[saveID] = Sum

numOfCustomers(1)
'''

import matplotlib.pyplot as plt #Импорт графической библиотеки
import collections

def customerGroup(ID): #Вычислить группу клиента
    Sum = 0
    while ID > 0:
        Sum += ID % 10
        ID //= 10
    return Sum

def drawFigure(clients, groups): #Нарисовать график (группы и клиенты)
    fig, ax = plt.subplots()

    ax.plot(clients, groups)
    ax.grid()
    
    #  Добавляем подписи к осям:
    ax.set_xlabel(' Группы    ',
                  fontsize = 15,    #  размер шрифта
                  color = 'red',    #  цвет шрифта
                  #  параметры области с текстом
                  bbox = {'boxstyle': 'rarrow',    #  вид области
                          'pad': 0.1,     #  отступы вокруг текста
                          'facecolor': 'white',    #  цвет области
                          'edgecolor': 'red',    #  цвет крайней линии
                          'linewidth': 3})     #  ширина крайней линии
    ax.set_ylabel(' Клиенты   ',
                  fontsize = 15,
                  color = 'red',
                  bbox = {'boxstyle': 'rarrow',
                          'pad': 0.1,
                          'facecolor': 'white',
                          'edgecolor': 'red',
                          'linewidth': 3})
    
'''
ID состоит из 5-7 цифр и может принимать значение от 00001 до 9999999.
Номер группы клиента (сумма чисел ID) с ID, например, 00235 и 235 одинаков,
поэтому не имеет смысла учитывать незначащие нули в начале  таких чисел.
'''
def numOfCustomersInEachGroup(n_customers): 
    '''
    Функция, которая подсчитывает число покупателей, попадающих в каждую группу,
    если нумерация ID сквозная и начинается с 0. На вход функция получает целое
    число n_customers (количество клиентов).
    '''
    print('\n=== ID начинается с 0 ===')
    if (n_customers >= 10000000): #Верхнее ограничение ID
        print('ERROR: Слишком много клиентов! Верхний предел ID – 9999999.')
        return -1
    setOfIDs = range(0, n_customers) #Массив ID клиентов по порядку
    Groups = {} #Словарь групп в формате – Номер группы : Количество клиентов
    for ID in setOfIDs: #Для каждого ID
        groupNum = customerGroup(ID) #Вычислить группу
        if groupNum not in Groups.keys(): #Если группы еще нет в списке
            Groups[groupNum] = 0 #Добавить ее
        Groups[groupNum] += 1 #Инкрементировать количество клиентов в соотв. группе
    for groupNum in Groups.keys(): #Для каждой группы
        print('Группа №', groupNum, ': ', Groups[groupNum], ' клиентов') #Вывести информацию о количестве клиентов
    drawFigure(Groups.keys(), Groups.values()) #Нарисовать график
    
def numOfCustomersInEachGroup2(n_customers, n_first_id):
    '''
    Функция, аналогичная первой, если ID начинается с произвольного числа.
    На вход функция получает целые числа: n_customers (количество клиентов)
    и n_first_id (первый ID в последовательности).
    '''
    print('\n=== ID начинается с ', n_first_id, ' ===')
    if (n_customers >= 10000000): #Верхнее ограничение ID
        print('ERROR: Слишком много клиентов! Верхний предел ID – 9999999.')
        return -1
    if (n_first_id >= n_customers):
        print('ERROR: Первый ID не может быть больше количества клиентов.')
        return -1
    setOfIDs = range(n_first_id, n_customers) #Массив ID клиентов по порядку, начиная с n_first_id
    Groups = {} #Словарь групп в формате – Номер группы : Количество клиентов
    for ID in setOfIDs: #Для каждого ID
        groupNum = customerGroup(ID) #Вычислить группу
        if groupNum not in Groups.keys(): #Если группы еще нет в списке
            Groups[groupNum] = 0 #Добавить ее
        Groups[groupNum] += 1 #Инкрементировать количество клиентов в соотв. группе
    sortedGroups = collections.OrderedDict(sorted(Groups.items())) #Сортировка групп по номерам
    for groupNum in sortedGroups.keys(): #Для каждой группы
        print('Группа №', groupNum, ': ', sortedGroups[groupNum], ' клиентов') #Вывести информацию о количестве клиентов
    drawFigure(sortedGroups.keys(), sortedGroups.values()) #Нарисовать график

#Ввод данных
numOfClients1 = int(input('Введите число клиентов для 1-й функции: '))
numOfClients2 = int(input('Введите число клиентов для 2-й функции: '))
firstID = int(input('Введите 1-й ID для 2-й функции: '))

# RUN
numOfCustomersInEachGroup(numOfClients1)
numOfCustomersInEachGroup2(numOfClients2, firstID)