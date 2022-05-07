# from tkinter import *

# class Testing:
#     def __init__(self, pro):
#         self.pro = pro
#         self.pro.geometry('600x600')
#         self.pro.title('my')



# pro = Tk()
# ob = Testing(pro)
# pro.mainloop()
# ==============================================================================
# EDABIT=======
# def stutter(word):
# 		return (word[0:2]+"..."+" "+word[0:2]+"..."+" "+word+"?")

# x = stutter("manhal")
# print(x)



# DISCOUNT
# def dis(price, discount):
# 	return (price - ((price)*(discount / 100)))

# x = dis(150, 45)
# print(x)



# # CURZON
# def is_curzon(num):
#     N = 2**num + 1
#     A = 2*num + 1
#     if N % A == 0:
#         return True
#     else:
#         return False
# c = is_curzon(870)
# print(c)
# -------------

# ==========================================
# =========finding missing letter===========
# ==========================================

import string

# print(string.ascii_lowercase)
# print(dir(string))

def find_missing_letter_in(givenLetters):
    alpha = string.ascii_lowercase
    start = alpha.index(givenLetters[0])
    for letter in alpha[start:] :
        if letter not in givenLetters :
            return letter
    return f"No Missing Letter In Sequence"



print(find_missing_letter_in("opqs"))  #r
print(find_missing_letter_in("defgi")) #h
print(find_missing_letter_in("xyz"))  # No Missing Letter In Sequence