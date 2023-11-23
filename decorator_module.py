def deneme():
    print("abc")


print(deneme())
f = deneme
print(f())



def deneme():
    print("deneme fonksiyonu calisiyor")



def test():
    print("test fonksiyonu calisiyor")


print(test())
print(deneme())

def deneme():
    print("deneme fonksiyonu calisiyor")



    def test():
         return "test fonksiyonu calisiyor"

    return test


deneme()
f = deneme()
print(f())
def deneme():
    return "deneme fonksiyonu calisiyor"
def ikinci(f):
    print("ikinci fonksiyon calisiyor")
    print(f())

print(ikinci(deneme))
def deco(f):

    def wrapper():
        print("baslangic")

        f()

        print("bitis")

    return wrapper

def yazdir():
    print("yazdir")

yazdir = deco(yazdir)

print(yazdir())
@deco
def toplama(a, b):
    print(a+b)

def deco(f):

    def wrapper(*args):
        print("baslangic")

        f(*args)

        print("bitis")

    return wrapper

@deco
def toplama(a, b):
    print(a+b)

print(toplama(4, 5))
def deco(msg1, msg2):
    def ara_katman(f):
        def wrapper(*args):
            print(msg1)

            f(*args)

            print(msg2)

    return wrapper
    return ara_katman



import time

print(time.time())


baslangic = print(time.time())
f()
bitis = print(time.time())
bitis = baslangic

def sure_olc(f):
    def wrapper(*args):
        baslangic = print(time.time())
        print("baslangic zamani:\t{}".format(baslangic))


        f(*args)

        bitis = print(time.time())
        print("bitis zamani:\t{}".format(bitis))
        print("gecen zaman:\t{}".format(bitis-baslangic))
    return wrapper

def faktoryel(sayi ):
    pass
    toplam = 1
    while sayi > 1:
        toplam = toplam *  sayi
        sayi = sayi - 1

    print(toplam)

    print(faktoryel(5))
    


















