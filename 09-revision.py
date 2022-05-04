# ## Multiplacation table 

# def multiplacation_table(start,end,step_start ,step_end):
#     for mn in range(start,end+1):
#         for x in range(step_start,step_end+1):
#             print(f"{mn} X {x} = {mn*x}")

#         print("-------")    


# multiplacation_table(2,8,5,10)


# # ## remove duplacated char
# word = input("Enter a word: ")
# chars = []
# for ch in word:
#     if ch not in chars:
#         print(ch, end="")
#         chars.append(ch)


# Game : oop

class Game:
    def __init__(self):
        while True:
            print('''
    Welcome In Our game
    Choose one of our games
            1 : Multiplacation Table
            2 : Remove Duplacate
            Press X to exit''')

            user_choice = input("Enter Game Number : ")
            if user_choice == "X":
                print("^-^")
                break
            else:
                if int(user_choice) == 1:
                    start = int(input("Enter start : "))
                    end = int(input("Enter End : "))
                    step_start = int(input("Enter Step_Start : "))
                    step_end = int(input("Enter Step_End : "))
                    self.multiplacation_table(start,end,step_start ,step_end)
                
                elif int(user_choice) == 2:
                    self.remove_duplacate()   



    def multiplacation_table(self,start,end,step_start ,step_end):
        for mn in range(start,end+1):
            for x in range(step_start,step_end+1):
                print(f"{mn} X {x} = {mn*x}")

            print("----------------")    

    def remove_duplacate(self):
        word = input("Enter a word: ")
        chars = []
        for ch in word:
            if ch not in chars:
                print(ch, end="")
                chars.append(ch)



g1 = Game()
