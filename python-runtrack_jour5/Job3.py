ligne = 13

for i in range(ligne):
    if i == 0 or i == 12:
        print('+----------+')
    else:
        print('|', end="")
    if i == 0 or i == 11:
        print('')
        print('|', end="")
