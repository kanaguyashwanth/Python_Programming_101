# EXERCISE - Treasure Map

'''
   1	 2		3
   
['⬜️', '⬜️', '⬜️']   1

['⬜️', '⬜️', '⬜️']   2

['⬜️', '⬜️', '⬜️']   3


row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
print (f'{row1}\n{row2}\n{row3}')

INPUT: (Column, Row)
Where do you want to put the treasure? 31

OUTPUT:
row1 = ['⬜️', '⬜️', 'x']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

'''




# CODE:
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]

position = input ('Where do you want to put the treasure? ')

col = int(position[0])
row = int(position[1])

map[row-1][col-1] = 'X'

# print (map)
print (f'{row1}\n{row2}\n{row3}')