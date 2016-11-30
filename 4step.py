#!/usr/bin/env python
#blast_parser_filter_hsp100#

Usage="""NAME.py INPUT OUTPUT"""

import sys

InFileName = sys.argv[1]
OutFileName = sys.argv[2]

WriteOutFile = True

InFile =open(InFileName, 'r')

HeaderLine = 'QueryName\tSubjectName\tQIdentity\tQhspStart1\tQhspEnd1\tQhspStart2\tQhspEnd2\tShspStart1\tShspEnd1\tShspStart2\tShspEnd2'

if WriteOutFile:
	OutFile = open(OutFileName, 'w')
	OutFile.write(HeaderLine + '\n')
	
LineNumber = 0

for Line in InFile:
	if LineNumber > 0: 
		Line=Line.strip('\n')
		ElementList = Line.split('\t')
		QName = ElementList[0]
		QLength = ElementList[1]
		SName = ElementList[2]
		Slength = ElementList[3]
		QIdentity = float(ElementList[4])
		Hsp_Length_I = int(ElementList[5])
		Qhsp_Start_I = ElementList[6]
		Qhsp_End_I = ElementList[7]
		Shsp_Start_I = ElementList[8]
		Shsp_End_I = ElementList[9]
		Diff_SLen_I = ElementList[10]
		Hsp_Length_II = int(ElementList[11])
		Qhsp_Start_II = ElementList[12]
                Qhsp_End_II = ElementList[13]
                Shsp_Start_II = ElementList[14]
                Shsp_End_II= ElementList[15]
                Diff_SLen_II = ElementList[16]
		if QIdentity >= 95 and QIdentity <=100.5:
			if Hsp_Length_I >=100 and Hsp_Length_II >= 100:
				outList = [str(QName),str(SName),str(QIdentity),str(Qhsp_Start_I),str(Qhsp_End_I),str(Qhsp_Start_II),str(Qhsp_End_II),str(Shsp_Start_I),str(Shsp_End_I),str(Shsp_Start_II),str(Shsp_End_II)]
				OutFile.write("\t".join(outList)+"\n")
	LineNumber += 1

InFile.close()
if WriteOutFile:
	OutFile.close()

