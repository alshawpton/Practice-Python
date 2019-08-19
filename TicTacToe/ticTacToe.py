def createTicTacToe(game):
        for i in range(3):
                print(' - '*3)
                for j in range(3):
                        print('|'+str(game[i][j])+'|',end='')
                print('')
        print(' - '*3)

def scoreTicTacToe(listLists):
        winner = 0
        for i in range(3):
                # check rows
                if listLists[i][0] == listLists[i][1] and listLists[i][0] == listLists[i][2] \
                        and listLists[i][0] != 0:
                        winner = listLists[i][0]
                # check columns
        for i in range(3):
                if listLists[0][i] == listLists[1][i] and listLists[0][i] == listLists[2][i] \
                        and listLists[0][i] != 0:
                        winner = listLists[0][i]
                # check Diagonal
        if listLists[0][0] == listLists[1][1] and listLists[0][0] == listLists[2][2] \
        or listLists[0][2] == listLists[1][1] and listLists[0][2] == listLists[2][0] \
        and listLists[1][1] != 0:
                winner = listLists[1][1]
        if winner != 0:
                return winner
        else:
                return 0

def playTicTacToe():
	move = 'x'
	game = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]
	play_again = 'y'
	x_score = 0
	y_score = 0
	while  play_again == 'y':
		game = [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]]
		move = 'x'
		while scoreTicTacToe(game) == 0:
			createTicTacToe(game)
			if move == 'x':
				select = input('Player X selects (row,col):')
				select_list = select.split(',')
				if game[int(select_list[0])-1][int(select_list[1])-1] == 'X' \
				or game[int(select_list[0])-1][int(select_list[1])-1] == 'Y':
					print('Space already selected. Choose again.')
					continue
				game[int(select_list[0])-1][int(select_list[1])-1] = 'X'
				move = 'y'
			else:
				select = input('Player Y selects (row,col):')
				select_list = select.split(',')
				if game[int(select_list[0])-1][int(select_list[1])-1] == 'X' \
				or game[int(select_list[0])-1][int(select_list[1])-1] == 'Y':
					print('Space already selected. Choose again.')
					continue
				game[int(select_list[0])-1][int(select_list[1])-1] = 'Y'
				move = 'x'
			flat_game = [values for lists in game for values in lists]
			if 0 not in flat_game:
				break

		createTicTacToe(game)

		if scoreTicTacToe(game) == 'X':
			print('X wins!')
			x_score += 1
		elif scoreTicTacToe(game) == 'Y':
			print('Y wins!')
			y_score += 1
		else:
			print('Draw')

		play_again = input('Play again?(y/n)')

	print('Final Score: X: %d  Y: %d' % (x_score,y_score))

playTicTacToe()
