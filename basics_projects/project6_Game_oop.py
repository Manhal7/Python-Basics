#  جمع كل المشاريع السابقة في لعبة بسيطه باستخدام ال OOP 
# يستطيع اللاعب اختيار أي لعبه منهم 
# بالإضافة إذا دخل اللاعب حرف ال X يتم الخروج من اللعبة
# وعند الانتهاء من اللعبة يتم سؤال اللاعب إذا كان يريد اللعب مرةأخرى
#  إذا وافق يتم طباعة جميع الألعاب له للاختيار منهم 
# واذا رفض يتم طباعة رسالة وداع والخروج من اللعبة

# def odd_even():
#     num = [31, 62, 48, 63, 4, 33, 87]
#     odd = []
#     even = []
#     for x in num:
#         if x % 2 == 0:
#             odd.append(x)
#         else:
#             even.append(x)
#     print(odd)
#     print(even)
# # ----222222----

# def words_count():
#     phrase = input("enter your phrase: ")
#     y = phrase.split(" ")
#     b = []
#     for i in y :
#         if i in b:
#             continue
#         else:
#             b.append(i)
#     print(len(b))
# # ------33333------

# def num_range():
#     x = int(input("enter number: "))
#     for i in range(x+1):
#         print(i)
# #------------444444--------
# def dividing_1():
#     x1 = int(input("enter number: "))
#     x2 = int(input("enter number: "))
#     a = []
#     for i in range(0,x1+1):
#             if i % x2 == 0:
#                 print(i)
# # ----------5555555------

# def dividing_2():
#     n1 = int(input("enter number: "))
#     n2 = int(input("enter number: "))
#     for n in range(0,101):
#         if n % n1 == 0 and n % n2 == 0:
#             print(n) 
# # ----------------


class Game():
    def __init__(self):
        while True:
            print('''
    Welcome in our game
    choose one of our games
            1 : odd_even
            2 : words_count
            3 : num_range
            4 : dividing_1
            5 : dividing_2
        Press X to exit''')
            user_choice = input("Enter game number : ")
            if user_choice == "X":
                print("hope you enjoy ^_^")
                break
            elif int(user_choice) == 1:
                self.odd_even()

            elif int(user_choice) == 2:
                self.words_count()

            elif int(user_choice) == 3:
                self.num_range()

            elif int(user_choice) == 4:
                self.dividing_1()        

            elif int(user_choice) ==5:
                self.dividing_2()

    def odd_even(self):
        num = [31, 62, 48, 63, 4, 33, 87]
        odd = []
        even = []
        for x in num:
            if x % 2 == 0:
                odd.append(x)
            else:
                even.append(x)
        print(odd)
        print(even)

    def words_count(self):
        phrase = input("enter your phrase: ")
        y = phrase.split(" ")
        b = []
        for i in y :
            if i in b:
                continue
            else:
                b.append(i)
        print(len(b))

    def num_range(self):
        x = int(input("enter number: "))
        for i in range(x+1):
            print(i)

    def dividing_1(self):
        x1 = int(input("enter number: "))
        x2 = int(input("enter number: "))
        a = []
        for i in range(0,x1+1):
                if i % x2 == 0:
                    print(i)

    def dividing_2(self):
        n1 = int(input("enter number: "))
        n2 = int(input("enter number: "))
        for n in range(0,101):
            if n % n1 == 0 and n % n2 == 0:
                print(n)

g = Game()