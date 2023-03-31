def hanoi(n, de, a, par):
        if n > 0:
            hanoi(n-1, de, par, a)
            print(str(de), "-->", str(a))

            hanoi(n-1, par, a, de)


print ("""
jeu de hanoi
il s'agit de deplacer des disques
de la tour 1 vers la tour 2
""")
n = input("donner le nombre de disques : ")
hanoi(int(n), 1, 2, 3)
