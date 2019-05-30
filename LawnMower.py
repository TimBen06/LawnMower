def TurnLeft(Coordonnees):		#fonction executant le turn left
	Orientation=['E', 'N', 'W', 'S']
	Orientation_initiale = Coordonnees[2]	#recuperer l orientation initiale
	Orientation_finale = Orientation[(Orientation.index(Orientation_initiale) + 1)%4]
	Coordonnees[2] = Orientation_finale	#Nouvelle Orientation inseree
	return(Coordonnees)

()

def TurnRight(Coordonnees):		#fonction executant le turn right
	Orientation=['E', 'N', 'W', 'S']
	Orientation_initiale = Coordonnees[2]		#recuperer l orientation initiale
	Orientation_finale = Orientation[Orientation.index(Orientation_initiale) - 1]		#Nouvelle Orientation inseree
	Coordonnees[2] = Orientation_finale
	return(Coordonnees)

()

def Forward(Coordonnees,T): 	#fonction executant le forward
	if Coordonnees[2] == 'W':		#Traitement du forward Est
		if Coordonnees[0] != 0:
			Coordonnees[0] = Coordonnees[0]-1

	elif Coordonnees[2]=='N':		#Traitement du forward Nord
		if Coordonnees[1]!=T[1]:
			Coordonnees[1]=Coordonnees[1]+1

	elif Coordonnees[2]=='E':		#Traitement du forward West
		if Coordonnees[0]!=T[0]:
			Coordonnees[0]=Coordonnees[0]+1

	else:							#Traitement du forward Sud
		if Coordonnees[1]!=0:
			Coordonnees[1]=Coordonnees[1]-1
	return(Coordonnees)

()


def Calcul_Position(taille, position_initiale, Instructions):		# fonction permettant de retourner la nouvelle position d'une machine apres les instructions
	position=position_initiale
	for element in Instructions:
		if element == 'L':
			position = TurnLeft(position)		#appeler la fonction turnLeft
		elif element == 'R':
			position = TurnRight(position)		#appeler la fonction turnRight
		elif element == 'F':
			position == Forward(position,taille)		#appeler la fonction forward
	return(position)

def main():
    inputList = [line.rstrip() for line in open("text.txt")] 	#lecture du fichier input en le décomposant en ligne
    taille = [int(inputList[0][0]), int(inputList[0][1])]		#extraire la premiere composante qui est la taille
    splittedList = inputList[1:]			#nouvelle liste contenant les positions initiales ainsi que les instructions a executer
    for e in range(0, len(instr), 2):
        orientation = [int(splittedList[e][0]), int(splittedList[e][1]), splittedList[e][2]]
        instructions = splittedList[e + 1]
        orientation_finale = Calcul_Position(taille, orientation, instructions)
        print(orientation_finale)
        fileOrientation = open("result.txt", "a")
        str_o_finale = str(orientation_finale) + "\n"
        fileOrientation.write(str_o_finale)
        fileOrientation.close()
  
if __name__== "__main__":
  main()