#!/usr/bin/env python
#hsp_test_2nd"

Usage="""NAME.py INPUT OUTPUT"""

import sys

InFileName =  sys.argv[1]
OutFileName =  sys.argv[2]

WriteOutFile = True

InFile =open(InFileName, 'r')

HeaderLine = 'QName\tQLength\tSName\tSLength\tQueryIdentityPercent\tHspLength1\tQhspStart1\tQhspEnd1\tShspStart1\tShspEnd1\tDiffSLen1\tHspLength2\tQhspStart2\tQhspEnd2\tShspStart2\tShspEnd2\tDiffSLen2'

if WriteOutFile:
        OutFile = open(OutFileName, 'w')
        OutFile.write(HeaderLine + '\n')
        
LineNumber = 0
dataDict = dict()
for Line in InFile:
	if LineNumber > 0: 
			Line=Line.strip('\n')
			ElementList = Line.split('\t')
			
		
			keyName = ElementList[0]+"\t"+ElementList[1]+"\t"+ElementList[2]+"\t"+ ElementList[3]+"\t"+ElementList[4]
			
			if dataDict.has_key(keyName):
 				
 				dataDict[keyName] = dataDict[keyName] + "\t" + ElementList[5] + "\t" + ElementList[6] + "\t" + ElementList[7] + "\t" + ElementList[8] + "\t" + ElementList[9] + "\t" + ElementList[10]
 				
 			else:
				dataDict[keyName]= ElementList[5] + "\t" + ElementList[6] + "\t" + ElementList[7] + "\t" + ElementList[8] + "\t" + ElementList[9] + "\t" + ElementList[10]
			#print dataDict[keyName]+"\n"
	LineNumber += 1

for KeyName in dataDict:
	values = dataDict[KeyName]
	outList = [str(KeyName), str(values)]
	if WriteOutFile:
		OutFile.write("\t".join(outList)+"\n")
	
InFile.close()
if WriteOutFile:
        OutFile.close()


