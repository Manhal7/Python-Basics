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
            if i not in b:
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