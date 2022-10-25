list_alpha=[i for i in range(10)]


def change():
    def inner():
        for i in list_alpha:
            print(i)
    
    inner()
change()
# change(list_par=list_alpha) 