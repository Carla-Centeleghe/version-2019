import random
def generador (min,max):
    return random.randint(min,max)


if __name__=="__main__":
    print(generador(1,20))