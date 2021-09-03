import csv
def toDict():
    my_dict = {"Title":[],"Author":[],"ISBN13":[],"Pages":[]}
    reader = csv.DictReader(open('todict.csv'))
    for row in reader:
        my_dict['Title'].append(row["Title"])
        my_dict['Author'].append(row["Author"])
        my_dict['ISBN13'].append(row["ISBN13"])
        my_dict['Pages'].append(row["Pages"])
    print(my_dict)
toDict()
#https://www.guru99.com/python-dictionary-append.html
