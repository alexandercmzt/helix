numList = [1,2,3,200, 2, 400, 6, 2000, 300, 600]

def removeOutliers(numList):
	numList.sort()
	removeList = []
	j = 0

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
			removeList.append(numList[i])
			print removeList
		if(i == len(numList)-1):
			break
	for word in removeList:
		numList.remove(word)
	print numList

	
removeOutliers(numList)