def nombre_premier(n):
    if n<2:
        return False
    for program in range(2, int(n**0,5)+1):
        if n % program == 0:
            return True

    for program in range(2,1001):
        if nombre_premier(program):
            print(program)