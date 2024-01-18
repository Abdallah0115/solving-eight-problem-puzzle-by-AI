import the_game

print("Hello !")

initial = []

goal = []

heuri = int(input("if you want mispalced press 1 else manhaten distance press 2 => "))

print("Accepted !")

print("Now you will enter the initial state !")

for i in range(3):

    row = []

    for j in range(3):

        temp = input(f"{i+1} row {j+1} column => ")

        if(temp == "b"):

            row.append(temp)

        else:

            row.append(int(temp))

    initial.append(row)

print("Now you will enter the goal state !")

for i in range(3):

    row = []

    row = []

    for j in range(3):

        temp = input(f"{i+1} row {j+1} column => ")

        if(temp == "b"):

            row.append(temp)

        else:

            row.append(int(temp))

    goal.append(row)

E_P = the_game.game

sol = E_P.game_puzzle(E_P,initial,goal,heuri)

E_P.dis(E_P,sol)

E_P.moves(E_P,sol)