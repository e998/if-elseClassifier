import numpy

a = numpy.zeros((3,3))

colA = a[:,0]
colB = a[:,1]
colC = a[:,2]
row1 = a[0,:]
row2 = a[1,:]
row3 = a[2,:]


# # Example Test of 0
# colA[0] = 1
# colA[1] = 1
# colA[2] = 1
# colC[0] = 1
# colC[1] = 1
# colC[2] = 1
# colB[0] = 1
# colB[2] = 1

# Example Test of 1
# colB[0] = 1
# colB[1] = 1
# colB[2] = 1

# Example Test of 4
colC[0] = 1
colC[1] = 1
colC[2] = 1
colA[0] = 1
colA[1] = 1
colB[1] = 1


pos1A = colA[0]
pos2A = colA[1]
pos3A = colA[2]

pos1B = colB[0]
pos2B = colB[1]
pos3B = colB[2]

pos1C = colC[0]
pos2C = colC[1]
pos3C = colC[2]


print a


# Is this a 1?
if numpy.sum(colA) == 3 and numpy.sum(a) == 3 or numpy.sum(colB) == 3 and numpy.sum(a) == 3 or numpy.sum(colC) == 3 and numpy.sum(a) == 3:
	print "This is a 1."
# Is this a 0?
elif pos2B == 0:
	if numpy.sum(a) == 8:
		print "This is a 0."

	elif pos1B + pos1C + pos3B + pos2A == 4 and pos1A + pos1C + pos3A + pos3C == 0:
		print "This is a 0."

	elif pos1A + pos1C + pos3C + pos3A == 4 and numpy.sum(a) == 4:
		print "This is a 0."
# Is this a 4?
elif numpy.sum(colC) == 3:
	if pos1B + pos2B == 2 and numpy.sum(a) == 5:
		print "This is a 4."
	elif pos1A + pos2A + pos2B == 3 and numpy.sum(a) == 6:
		print "This is a 4."
elif numpy.sum(colB) == 3 and pos1A + pos2A == 2 and numpy.sum(a) == 5:
	print "This is a 4."
else:
	print "This is not 0, 1, or 4. Please try again."


