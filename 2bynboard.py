"""
2 x n board
 _ _ _ _ ... n
[			  ]
[_ _ _ _ ... _]

Tile with Dominos (2 x 1)
Or trominos (L shape)

Count number of ways to tile each board
-----------------------------------------
2 x 1 -- 1

A
A		Base block		 Vert 1

2 x 2 -- 2

A A
B B 	Base block		Horz 2

A B
A B		Compound block

2 x 3 -- 5

A A B	A B C	A B B	
C C B	A B C	A C C	

A A B	
A B B	Base Block	- L over R

A B B	
A A B	Base Block - R over L

2 X 4 -- 9

A A B D 	A B C D 	A B B D 	A A B D 	A B B D
C C B D 	A B C D 	A C C D 	A B B D 	A A B D 

						D A B B		D A A B		D A B B
						D A C C		D A B B		D A A B

A A B B
C C D D

2 x 5

v1,v1,v1,v1,v1 ---- 5 choose 0

h2,v1,v1,v1
v1,h2,v1,v1 ---- 4 choose 1
v1,v1,h2,v1
v1,v1,v1,h2

v1,h2,h2
h2,v1,h2 ---- 3 choose 2
h2,h2,v1

v1,v1,rol
v1,rol,v1 ---- 3 Choose 1
rol,v1,v1

v1,v1,lor
v1,lor,v1 ---- 3 Choose 2
lor,v1,v1

h2,rol
h2,lor
rol,h2
lor,h2 

1,2,5,9,18,27,

1
1

2
2
1,1

3
3
1,1,1
2,1

4
3,1
1,1,1,1
2,1,1
2,2

5
3,1,1
1,1,1,1,1
2,1,1,1
2,2,1
3,2

6
3,3
3,2,1
2,2,2
3,1,1,1
2,2,1,1
2,1,1,1,1
1,1,1,1,1,1


7
3,3,1
3,2,1,1
2,2,2,1
3,1,1,1,1
3,2,2
2,2,1,1,1
2,1,1,1,1,1
1,1,1,1,1,1,1

8
3,3,1,1
3,2,1,1,1
2,2,2,1,1
3,1,1,1,1,1
3,2,2,1
2,2,1,1,1,1
2,1,1,1,1,1,1
1,1,1,1,1,1,1,1
3,3,2
2,2,2,2



"""


def countways(n):
	if n == 1:
		return 1
	else:
		thisblocktotal = 0
		if n > 3: # can place matching blocks.
			thisblocktotal += 2 * countways(n - 3)
		if n > 2:
			thisblocktotal += countways(n - 2)
		return thisblocktotal + countways(n - 1)
		
print(countways(1))