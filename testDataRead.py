import re
import time

def main():
	weightedPatients = [[38, 109], [38, 120], [38, 123], [38, 142], [39, 19], [39, 34], [39, 93], [40, 47], [40, 86], [41, 50], [41, 72], [41, 108], [42, 17], [42, 25], [42, 37], [42, 40], [42, 60], [42, 62], [42, 78], [42, 144], [43, 6], [43, 15], [43, 49], [43, 116], [44, 89], [44, 92], [47, 65], [48, 76], [48, 90], [50, 110]]
	hospital = readAndParse()
	# print hospital[0]
	hospitalSurvival = getImportantData(hospital)
	weightedAverages(weightedPatients,hospitalSurvival)

def weightedAverages(patientWeights,hospital):
	weightDivisor = 0
	chance_of_remission = []
	days_of_remission = []
	days_of_survival = []

	for patient in patientWeights:
		weightDivisor += patient[0]

	for patient in patientWeights:
		if hospital[patient[1]-1][1] == 'complete_remission':
			chance_of_remission.append((float(patient[0])/float(weightDivisor)))
		if hospital[patient[1]-1][1] == 'resistant':
			chance_of_remission.append((-1)*(float(patient[0])/float(weightDivisor)))
		if not hospital[patient[1]-1][2] == 'na':
			# print (float(patient[0])/float(weightDivisor))*float(hospital[patient[1]-1][2])
			days_of_remission.append((float(patient[0])/float(weightDivisor))*float(hospital[patient[1]-1][2]))
		# print float(hospital[patient[1]-1][3])
		days_of_survival.append((float(patient[0])/float(weightDivisor))*float(hospital[patient[1]-1][3]))
	
	print "chance_of_remission:", removeOutliers(chance_of_remission)
	print "days_of_remission:",removeOutliers(days_of_remission)
	# print "days_of_survival:",removeOutliers(days_of_survival)

def getImportantData(patientData):
	ifTheyDiedOrNot = []
	for patients in patientData:
		temp = []
		if patients:
			temp.append(patients[0])
			temp.append(patients[266])
			temp.append(patients[267])
			temp.append(patients[268])
		ifTheyDiedOrNot.append(temp)
	return ifTheyDiedOrNot

def removeOutliers(numList):
	removed = 0
	for i in range(0, len(numList)):			
		numSum = 0
		average = 0
		percentError = 0
		for j in range(0, len(numList)):
			if(numList[i] == numList[j]):
				pass
			else:
				numSum+=numList[j]
		average = numSum/(len(numList)-1)
		percentError = float((average - numList[i]))/average * 100
		if(percentError < 80):
			numList.remove(numList[i])
			i-=1
			print numList
		if(i == len(numList)-1):
			break

def readAndParse():
	f = open("trainingData.txt","r")
	pattern = re.compile("train_id_\d\d\d")
	raw = f.read()
	f.close()
	parsed = []
	tempParsed = []
	for word in raw.split():
		if pattern.match(word):
			if tempParsed:
				parsed.append(tempParsed)
				tempParsed = []
			tempParsed.append(word)
		else:
			tempParsed.append(word.lower())
	parsed.append(tempParsed)
	return parsed

if __name__ == '__main__':
	# main()