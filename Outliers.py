numList = [1,2,3,4,5,6,200,7,8,300,50,40,100,1]
def removeOutliers(numList):
	print len(numList)
	removed = 0
	for i in range(0, len(numList)):			
		numSum = 0
		average = 0
		percentError = 0
		for j in range(0, len(numList)):
			print(i,j)
			if(numList[i] == numList[j]):
				pass
			else:
				numSum+=numList[j]
		average = numSum/(len(numList)-1)
		
		percentError = float((average - numList[i]))/average * 100
		print percentError
		if(percentError < 80):
			numList.remove(numList[i])
			i-=1
			print numList
		if(i == len(numList)-1):
			break

removeOutliers(numList)