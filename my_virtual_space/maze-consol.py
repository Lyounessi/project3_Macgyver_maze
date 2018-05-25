""" Welcome to Macgyver game, in this part You'll play
the Macgyver gameas consol Mode """

#-----------------------------------
#Read the map and put it into a list
#-----------------------------------

maze = list(list())

with open("my-map.txt", "r") as file_r:
    for line in file_r:
        maze.append([char for char in line if char !="\n"])


#----------------------------
#Print the map in consol mode
#----------------------------

"""Here we will print the map in the consol mode
as the structure wanted"""
    
for i, line in enumerate(maze):
    for j, char in enumerate(line):
        print(maze[i][j], end="")
    print("")

    
# ----------------------------------------------------------
# Find the position of the letter "M" in the list self.carte
# ----------------------------------------------------------

"""In this phase we will try to find the position of
letter M (line and column)"""

m_line = 0

m_col = 0

for i, line in enumerate(maze):
    for j, char in enumerate(line):
        if char == "M":
            m_line = i
            m_col = j
#print(" m_line : " + str(m_line))
#print(" m_col : " + str(m_col))




#-------------------------
#Collect inputs from usres
#-------------------------

"""After finding the position of the letter M in our list maze,
now we will move it inside the list"""

test = True

while test:
    answer = input("Choisissez une lettre pour déplacer le joueur? (N'nord',S'sud',E'est',W'west') ou Q pour quitter")
    if answer == "Q":
        test = False
    elif answer == "N":
        if maze[m_line - 1][m_col] == "-":
            maze[m_line - 1][m_col] = "M"
            maze[m_line][m_col] = "-"
            m_line -= 1
        else:
            print("Le mouvement n'est pas possible car il y a un mur!")
    elif answer == "S":
        if maze[m_line + 1][m_col] == "-":
            maze[m_line + 1][m_col] = "M"
            maze[m_line][m_col] = "-"
            m_line += 1
        else:
            print("Le mouvement n'est pas possible car il y a un mur!")
    elif answer == "E":
        if maze[m_line][m_col + 1] == "-":
            maze[m_line][m_col + 1] = "M"
            maze[m_line][m_col] = "-"
            m_col += 1
        else:
            print("Le mouvement n'est pas possible car il y a un mur!")
    elif answer == "W":
        if maze[m_line][m_col - 1] == "-":
            maze[m_line][m_col - 1] = "M"
            maze[m_line][m_col] = "-"
            m_col -= 1
        else:
            print("Le mouvement n'est pas possible car il y a un mur!")
    else:
        print("Réponse non correcte")

    # ------------------------
    # Reprint the map in console
    # ------------------------
    for i, line in enumerate(maze):
        for j, char in enumerate(line):
            print(maze[i][j], end="")
        print("")
