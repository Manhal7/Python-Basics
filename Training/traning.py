# name1 ="Ahmad"
# name2 ="hasan"
# print(name1+" "+name2)
# ----------------------------------
# x = "manhal\"tamr\""
# print(x)
# z = """manhal
# khairo
# altamr


# """
# print(z)
# ______________________________________________________
# name = "manhal"
# print(name[0:3])
# ======================================================
# name = "manhal"
# print(name.upper())
# print(name.lower())
# print(name.isupper())
# print(name.islower())
# print(name.capitalize())
# print(name.title())
# ======================================================
# program_lan = "html css php javascript python"
# print(program_lan.split())

# program_lan1 = "html_css_php_javascript_python"
# print(program_lan1.split("_",3))
# print(program_lan1.rsplit("_",3))
# ======================================================
# x = "html css php js python"
# print(x.index("php"))

# print(len(x))
# ======================================================

# num1 = input("enter number: ")
# num2 = input("enter number: ")
# result1 = int(num1) + int(num2)
# print(result1)
# result2 = float(num1) + float(num2)
# print(result2)
# result3 = complex(num1) + complex(num2)
# print(result3)
# =======================================================
# x = input("enter your lan: ") 
# print("i love " + x)
# =================Lists=================================
# lista = ["Ahmad", 1, True, False, 10.5, [1,2,3,[1,2,3]]]
# print(lista[5][3][0])
     
# lista [3] = "M"
# print(lista)
# =======================================================
# x = [1,2,3]
# x.append(4)
# print(x)
# # ---
# x.insert(1,"AA")
# print(x)
# # ---
# m = [1,2,3]
# b = [4,5,6]
# m.extend(b)
# print(m)
# ------
# from re import T


# h = [2,5,3,7,8,1]
# h.sort()
# print(h)
# p = ["ali","mohammad","omar"]
# p.sort(reverse=True)
# print(p)
# # -----
# p.remove("ali")
# print(p)
# # -----
# p.clear
# print(p)
# ========================TUPLES=============================
# هي نفس القوائم ولكن لا يمكنك إجراء التغيير عليها
# =========================DICTIONARY========================
# info = {
# "name":"ahmad",
# "age":25,
# "country":"egypt",
# }
# print(info["age"])
# print(info.get("id","not found"))
# ==========================SET==============================
# from os import remove


# mySet = {"ahmad","ali","hassan"}
# print(mySet)
# إنها غير مرتبة في كل مرة تعطي ترتيبا مختلفا
# لا تستطيع إحضار اندكس أو سلايس منها
# لا تستطيع كتابة قائمة أو قاموس بداخلهاولكن يمكن كتابة توبل بداخلها
# ----------     set methods:
#   union()--------add()-------remove()------discard()------clear()
# a = {1,2,3}
# b = {4,5,6}
# print(a.union(b))
# print(a|b)  

# a.add(4)
# a.add(7)
# print(a)

# a.remove(2)
# print(a)

# a.discard(88)
# print(a)
# ============================functions================================
# def f_function(name,age):
#     print("my name is "+name+ "my age is "+str(age))
# f_function("manhal \n",28)
# ========    return function:
# def calc(num1,num2):
#     return num1+num2
# print(calc(12.5,8))
# =============================if======================================

# email = "x@gmail.com"
# password = 1234
# if email == "x@gmail.com" and password == 1234:
#     print("wellcome")
# elif email == "x@gmail.com" and password != 1234:
#     print("invalid password")
# elif email != "x@gmail.com" and password == 1234:
#     print("invalid email")
# else:
#     print("invalid email and password")
    
# =======================================================================

# def names(ahmed,hassan,ali):
#     if ahmed > hassan and ahmed > ali:
#         return ahmed
#     elif hassan > ahmed and hassan > ali:
#         return hassan
#     else :
#         return ali         
# print(names(23,79,42))
# ======================while loop=========
# i = 1
# while i <= 10:
#     i += 1
#     if i == 8:
#         continue
#     if i == 10:
#         break
#     print(i)