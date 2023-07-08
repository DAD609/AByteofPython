def readadrbook():
    with open("adressbook.txt", "r") as R:
        for lines in R:
            print(lines, end = '\n')

def appendadrbook( a):
    
    with open("adressbook.txt", "a") as ap:
        ap.write(a)

a = input("имя введи")
appendadrbook(a)
readadrbook()