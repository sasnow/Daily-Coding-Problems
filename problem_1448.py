"""
A wall consists of several rows of bricks of various integer lengths and uniform height.
Your goal is to find a vertical line going from the top to the bottom of the wall that
cuts through the fewest number of bricks. If the line goes through the edge between two
bricks, this does not count as a cut.


"""
import numpy as np

def getLeastCuts(wall,intCount,width):	
	for row in wall:
		connectedlengths = []
		for brick in row:
			clen = len(connectedlengths)
			newlength = 0
			if clen == 0:
				newlength = brick
			else:
				newlength = brick + connectedlengths[clen - 1]
			if newlength < width:
				connectedlengths.append(newlength)
				intCount[newlength] += 1
	print(intCount)
	return [x for x in intCount.keys() if intCount[x] == max(intCount.values())][0]
	
def verifyWall(wall,width):
	for row in wall:
		if sum(row) != width:
			return False
	return True
	
	
	
	
wall = [[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]
 
wall2 = [[1,4,7,2,3],
		[1,2,3,11],
		[9,8],
		[1,1,1,1,1,3,4,3,2],
		[3,4,5,3,2],
		[14,1,2],
		[2,6,8,1],
		[7,2,1,5,1,1]]

walllen = sum(wall[0])
walllen2 = sum(wall2[0])
		
if verifyWall(wall,walllen):		
	intervalCounter = {x:0 for x in np.arange(1,walllen)}
	print(getLeastCuts(wall,intervalCounter,walllen))
	
if verifyWall(wall2,walllen2):		
	intervalCounter2 = {x:0 for x in np.arange(1,walllen2)}
	print(getLeastCuts(wall2,intervalCounter2,walllen2))