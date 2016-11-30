#! /usr/bin/env python

#blast_parser_hsp_2_1000bp_SE"

#Usage="""NAME.py INPUT OUTPUT"""#

import sys
from Bio.Blast import NCBIXML

def identity_query_alignment_obj(alignmentObj,e_value_thresh=1000000):

    this_matches = 0

    for hsp in alignmentObj.hsps:
        if hsp.expect <= e_value_thresh:
            this_query = blast_record.query_length
            this_matches += hsp.identities
    if this_matches >0:
        this_percent =  (this_matches * 100. )/ this_query

    return this_percent


inPutFile=sys.argv[1]
outPutFile = sys.argv[2]

result_handle = open(inPutFile,"r")
out_handle = open(outPutFile, "w")
Blast_records = NCBIXML.parse(result_handle)

header = ['QueryName', 'QueryLength', 'SubjectName', 'SubjectLength', 'QueryIdentityPercent', 'HspLength', 'QhStart', 'QhEnd', 'ShStart', 'ShEnd',  'HspNum']

out_handle.write("\t".join(header)+"\n")

for blast_record in Blast_records:
	queryName = blast_record.query
	queryLength = int(blast_record.query_length)
	subjectName = ""
	subjectLength = ""
	queryIdentityPercent = 0
	for alignment, description in zip(blast_record.alignments,blast_record.descriptions):
        	hspNum = int(len(alignment.hsps))
		subjectName = alignment.title
		subjectLength = int(alignment.length)
		queryIdentityPercent = identity_query_alignment_obj(alignment)
		if queryName != subjectName and hspNum == 2:
			if queryLength >= 1000 and subjectLength >= queryLength:
				for hsp in alignment.hsps:
					hspLength = hsp.align_length
					qhStart = hsp.query_start
					qhEnd = hsp.query_end
					shStart = hsp.sbjct_start
					shEnd = hsp.sbjct_end
					outList =[queryName, str(queryLength), subjectName, str(subjectLength), str(round(queryIdentityPercent,2)), str(hspLength), str(qhStart), str(qhEnd), str(shStart), str(shEnd), str(hspNum)]	
					out_handle.write("\t".join(outList)+"\n")


result_handle.close()
out_handle.close()
