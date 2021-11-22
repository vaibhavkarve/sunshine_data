#! usr/env/bin python3.9
"""Module for """
import csv 


def selection_criterion(line: list[str]) -> bool:
    return None


DATA = []
with open("abc.csv", "r") as readfile:   # Context manager
    reader = csv.reader(readfile, delimiter=",", quotechar='"')
    header = reader.readline()
    line: List[str]
    for line in reader.readline():
        if selection_criterion(line):
            DATA.append(line)

with open("new.csv", "w") as writefile:
    writer = csv.writer(writefile, delimiter=",", quotechar='"')
    writefile.writerow(header)
    writefile.writerows(DATA)
