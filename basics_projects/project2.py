def words_count():
    phrase = input("enter your phrase: ")
    y = phrase.split(" ")
    b = []
    for i in y :
        if i not in b:
            b.append(i)
    return print(len(b))

words_count()
