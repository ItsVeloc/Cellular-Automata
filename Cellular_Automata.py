import graphics
from graphics import *

def run():
	binaryLength = int(input('How long do you want it? '))
	loops = int(input('How many times do you want it to loop? '))
	squareLength = 1500 / (binaryLength)
	height = loops * squareLength
	binary = []
	if binaryLength %2 == 0:
		binaryLength += 1
	for i in range(binaryLength):
		if i == (binaryLength+1)/2:
			binary.append(1)
		else:
			binary.append(0)
	recursiveList = []
	win = GraphWin('picture', 1500, height)
	y = 0
	for i in range(loops):
		y += 1
		num = 0
		prev = 0
		recursiveList = []
		for i in binary:
		#First Gen
			#defining variables present throughout
			x = num*squareLength
			#drawing + filling based on binary list
			pixel = Rectangle(Point((x+squareLength), y*squareLength), Point(x, (y+1)*squareLength))
			if i == 1:
				pixel.setFill('black')
			else:
				pixel.setFill('white')
			pixel.draw(win)
		#Second Gen/Iterative Gen
			#finding neighbours and calculating nextGen
			if num < len(binary)-1:
				after = binary[num+1 or  0]
			else:
				after = 0
			if prev and after == 1:
				nextGen = 0
			elif prev or after == 1:
				nextGen = 1
			else:
				nextGen = 0
			recursiveList.append(nextGen)
			num += 1
			prev = i
		binary = recursiveList

ifPlay = input('Do you want to run?')
if ifPlay == 'yes':
	run()