def palindromo(palabra):
    a = list(palabra)
    b = a.reverse()
    print(a)
    print(b)
    return False

if __name__ == "__main__":
    print(palindromo("trini"))
