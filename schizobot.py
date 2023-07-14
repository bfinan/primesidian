# schizobot.py
# forms a connection between two unrelated nodes
# it's all connected brother
# 0_0 2

"""
Core design can be summed up by the google results for "graph connection between two nodes"
see ~/pale-fire/meta/schizobot for design details
"""

import random
from myosotis import *


# strings
jokes = [
    "kind of reminds me of",
    "is similar to",
    ": a lot of people try this and encounter ",
]

# config
VERSION = 2.13
DRY_RUN = True

journal_name = "pale-fire"

if is_wangblows():
    PF_PATH = f"C:\\Users\\brendanfinan\\{journal_name}\\"
else:
    PF_PATH = f"/home/you/{journal_name}/"

pf_notes = find_every_instance_of_note(PF_PATH, fullpath=False)

# TODO move this function to Myosotis and add distinction between daily note and topic note
for i in range(100):
    for pf_note in pf_notes:
        if is_dailynote(pf_note):
            # remove the note
            pf_notes.remove(pf_note)

# TODO: Figure out why the count goes down after each run
print(f"Found {len(pf_notes)} notes after automated removal")

note1 = random.choice(pf_notes)
note2 = random.choice(pf_notes)

joke = random.choice(jokes)

# warning: this will fuck up your knowledge base
DRY_RUN = True
if DRY_RUN:
    note1 = random.choice(pf_notes)
    note2 = random.choice(pf_notes)
    joke = random.choice(jokes)
    print(f"DRY RUN: {note1} {joke} {note2}")
    if not DRY_RUN:
        form_connection(note1, note2, joke)

sampleselection = []
for i in range(0, 20):
    sample = random.choice(pf_notes)
    sample = sample.replace(".md", "")
    sample = sample.replace("-", " ")
    print(f"{sample}, ", end="")
    sampleselection.append(sample)

# writes the list of notes to a file
def printer():
    odd = True
    with open("all_pf_notes.txt", "w") as f:
        for pf_notie in pf_notes:
            pf_notie = pf_notie.replace(".md", "")
            of_notie = pf_notie.replace("-", " ")
            if odd:
                f.write(pf_notie + "\n")
                odd = False
            else:
                f.write(of_notie + "         ")
                odd = True
        f.close()


printer()
