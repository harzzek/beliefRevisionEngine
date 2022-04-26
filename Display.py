def display():
    print("Hello! Welcome to belief revision!\n")
    print("Below you find the various belief functions... Choose one! \n")
    print("________________________________\n")
    print("r: Revision (Reevaluate beliefs from given belief)\n")
    print("c: Contraction (Remove a belief, and Reevaluates)\n")
    print("e: Expansion (Add new belief)\n")
    input1 = input()
    choice(input1)


def choice(x):
    if x == 'r':
        pass
    elif x == 'c':
        pass
    elif x == 'e':
        pass
    else:
        print("Syntax error. Try again")
        choice(x)
