#!/usr/bin/env python

#blast_parser_filter_RF#

Usage="""NAME.py INPUT OUTPUT"""

import sys

InFileName = sys.argv[1]
OutFileName = sys.argv[2]

WriteOutFile = True

InFile =open(InFileName, 'r')

HeaderLine = 'QueryName\tQueryLength\tSubjectName\tSubjectLength\tQueryIdentity\tHspLength1\tQhspStart1\tQhspEnd1\tShspStart1\tShspEnd1\tDiffSLen1\tHspLength2\tQhspStart2\tQhspEnd2\tShspStart2\tShspEnd2\tDiffSLen2'


if WriteOutFile:
	OutFile = open(OutFileName, 'w')
	OutFile.write(HeaderLine + '\n')
	
LineNumber = 0

for Line in InFile:
	if LineNumber > 0: 
		Line=Line.strip('\n')
		ElementList = Line.split('\t')
		DiffLen1 = int(ElementList[10])
		DiffLen2 = int(ElementList[16])
		if (DiffLen1 < 0 and DiffLen2 < 0) or (DiffLen1 > 0 and DiffLen2 > 0): 
				if WriteOutFile:
					OutFile.write(Line + '\n')
	LineNumber += 1

InFile.close()
if WriteOutFile:
	OutFile.close()

