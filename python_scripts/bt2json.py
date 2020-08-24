import bibtexparser
import json
from bibtexparser.customization import convert_to_unicode
import re
import sys
import glob
from os.path import join


count = 0
scount = 0
entry = re.compile('^@')

worker = None
old = None

bibs = []
bids = {}

err = open('data/bibtexerrors.txt','w')

for f in glob.glob('publications/*.bib'):
    
    with open(f) as bf:
        parser = bibtexparser.bparser.BibTexParser()
        parser.customization = convert_to_unicode

        for line in bf:
            if (entry.match(line)):
                count += 1
                old = worker
                worker = line
                if old:
                    bdict = bibtexparser.loads(old)
                    if (bdict.entries):
                        scount+=1
                        bibs.append(bdict.entries[0])
                        if (scount == count):
                            print("Mismatch at: " + str(count))
                    else:
                        err.write("Failure in file: " + f + '\n')
                        err.write(old + '\n')
            else:
                if worker:
                    worker = worker + line
    
if worker:
    bdict = bibtexparser.loads(worker)
    if (bdict.entries):
        scount+=1
        bibs.append(bdict.entries[0])
    else:
        err.write("Failure in file: " + f + '\n')
        err.write(worker + '\n')

            
if (count != scount):
    print("Failed: " + str(count) + " entries and " + str(scount) + " parsed.")
    sys.exit(count - scount)

with open ('data/pubs.json','w') as jd:
    json.dump(bibs,jd)

sys.exit(0)
