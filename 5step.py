#!/usr/bin/env python
#blast_parser_filter_hspoverlap#

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
		SName = ElementList[1]
		Qhsp_Start_I = ElementList[3]
		Qhsp_End_I = ElementList[4]
		Qhsp_Start_II = ElementList[5]
		Qhsp_End_II = ElementList[6]
		Shsp_Start_I = ElementList[7]
                Shsp_End_I = ElementList[8]
                Shsp_Start_II = ElementList[9]
                Shsp_End_II= ElementList[10]

		if not (Qhsp_Start_II > Qhsp_Start_I and Qhsp_End_II < Qhsp_End_I) and not (Qhsp_Start_II < Qhsp_Start_I and Qhsp_End_II > Qhsp_End_I):
			if WriteOutFile:
                                        OutFile.write(Line + '\n')

				
	LineNumber += 1

InFile.close()
if WriteOutFile:
	OutFile.close()

