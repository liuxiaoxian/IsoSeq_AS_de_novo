#!/usr/bin/env python

#hsp_test_1st"

Usage="""NAME.py INPUT OUTPUT"""
import sys



InFileName = sys.argv[1]
OutFileName = sys.argv[2]

WriteOutFile = True

InFile =open(InFileName, 'r')

HeaderLine = 'QName\tQLength\tSName\tSLength\tQueryIdentityPercent\tHspLength\tQhspStart\tQhspEnd\tShspStart\tShspEnd\tDiffSLen'


if WriteOutFile:
        	OutFile = open(OutFileName, 'w')
        	OutFile.write(HeaderLine + '\n')
        
LineNumber = 0

for Line in InFile:
		if LineNumber > 0: 
			Line=Line.strip('\n')
			ElementList = Line.split('\t')
			queryName = ElementList[0]
			queryLength = ElementList[1]
			subjectName = ElementList[2]
			subjectLength =ElementList[3]
			queryIDPercent = ElementList[4]
			hspLength = ElementList[5]
			Qhstart = ElementList[6]
			QhEnd = ElementList[7]
			ShStart = ElementList[8]
			ShEnd = ElementList[9]
			Delta_S_Len = int(ElementList[9]) - int(ElementList[8])
			outList =[str(queryName), str(queryLength), str(subjectName), str(subjectLength),str(queryIDPercent), str(hspLength), str(Qhstart), str(QhEnd), str(ShStart), str(ShEnd), str(Delta_S_Len)]
			if WriteOutFile:
				OutFile.write("\t".join(outList)+"\n")
		LineNumber += 1

InFile.close()
if WriteOutFile:
        	OutFile.close()

