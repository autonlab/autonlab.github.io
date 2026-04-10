import bibtexparser
import json
from bibtexparser.customization import convert_to_unicode
import re
import sys
import glob

count = 0
scount = 0
entry_re = re.compile('^@')

worker = None
old = None

bibs = []
seen_titles = set()

err = open('data/bibtexerrors.txt','w')

def normalize_title(entry):
    title = entry.get('title')
    if not title:
        return None

    title = re.sub(r'[{}]', '', title)
    title = re.sub(r'\\[a-zA-Z]+', '', title)

    title = title.lower()
    title = re.sub(r'[^a-z0-9]', ' ', title)
    title = re.sub(r'\s+', ' ', title).strip()

    return title

for f in glob.glob('publications/*.bib'):
    with open(f) as bf:
        parser = bibtexparser.bparser.BibTexParser()
        parser.customization = convert_to_unicode

        for line in bf:
            if entry_re.match(line):
                count += 1
                old = worker
                worker = line
                if old:
                    bdict = bibtexparser.loads(old)
                    if bdict.entries:
                        scount += 1
                        ent = bdict.entries[0]
                        key = normalize_title(ent)

                        if key:
                            if key not in seen_titles:
                                seen_titles.add(key)
                                bibs.append(ent)
                            else:
                                err.write(f"Duplicate title skipped in file: {f}\n")
                                err.write(ent.get('title', 'UNKNOWN TITLE') + '\n')
                        else:
                            bibs.append(ent)
                    else:
                        err.write("Failure in file: " + f + '\n')
                        err.write(old + '\n')
            else:
                if worker:
                    worker = worker + line

if worker:
    bdict = bibtexparser.loads(worker)
    if bdict.entries:
        scount += 1
        ent = bdict.entries[0]
        key = normalize_title(ent)

        if key:
            if key not in seen_titles:
                seen_titles.add(key)
                bibs.append(ent)
            else:
                err.write(f"Duplicate title skipped in file: {f}\n")
                err.write(ent.get('title', 'UNKNOWN TITLE') + '\n')
        else:
            bibs.append(ent)
    else:
        err.write("Failure in file: " + f + '\n')
        err.write(worker + '\n')

if count != scount:
    print("Failed: " + str(count) + " entries and " + str(scount) + " parsed.")
    sys.exit(count - scount)

with open('data/pubs.json','w') as jd:
    json.dump(bibs, jd)

sys.exit(0)
