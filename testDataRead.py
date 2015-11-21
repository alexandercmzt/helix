import re
import time
import string
import sys

def main():
	for np in readAndParse():
		hospital = readAndParseGEOIUHGFQE()
		# print hospital
		hospitalSurvivalData = getImportantData(hospital)
		reduction(hospital,np)
		weightedPatients = returnSimilar(hospital,np)
		hospital = readAndParseGEOIUHGFQE()
		weightedAverages(weightedPatients,hospitalSurvivalData)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def returnSimilar(hospitalData, testPatientData, threshold = 0.33):
	solutionSet = []
	for patient in hospitalData:
		similarityPoints=0
		for j in range(1,len(patient)-5):
			#compare current value with testPatientData[i]

			if is_number(patient[j]) and is_number(testPatientData[j]):
				if ((float(patient[j])+float(testPatientData[j])) != 0):
					if (abs(((float(patient[j]) - float(testPatientData[j]))/(0.5*(float(patient[j])+float(testPatientData[j])))))<threshold):
						if (j == 169 or j==170 or j==142):
							similarityPoints += 5
						else:
							similarityPoints+=1
			else:
				if (patient[j] == testPatientData[j]):
					similarityPoints += 1
		ptnumber = int(re.sub("\D", "", patient[0]))
		solutionSet.append([similarityPoints,ptnumber])
	solutionSet.sort()
	return solutionSet[-30:]

def reduction(hospitalData, testPatientData):
	for patient in hospitalData:
			if patient[1] != testPatientData[1]:
				del patient
			elif patient[10] != testPatientData[10]:
				del patient

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
	print "days_of_survival:",removeOutliers(days_of_survival)

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
	numList.sort()
	removeList = []
	j = 0
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
			removeList.append(numList[i])
		if(i == len(numList)-1):
			break
	for word in removeList:
		numList.remove(word)
	return sum(numList)

def readAndParseGEOIUHGFQE():
	# f = sys.stdin.read()
	f = open("trainingData.in","r")
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

def readAndParse():
	f = sys.stdin.read()
	# f = open("trainingData.txt","r")
	pattern = re.compile("train_id_\d\d\d")
	# raw = f.read()
	# f.close()
	parsed = []
	tempParsed = []
	for word in f.split():
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
	main()