import csv
import pandas as pd
import tempfile
def back_and_forth():
    my_dict = {"Title": ["1984", "Animal Farm", "Brave New World"], "Author": ["George Orwell", "George Orwell", "Aldous Huxley"], "ISBN13": ["978-0451524935", "978-04515266342", "978-0060929879"], "Pages": [268, 144, 288]}
    df = pd.DataFrame(my_dict)
    tf = tempfile.NamedTemporaryFile()
    df.to_csv(tf.name, sep=',', index = False)
    with open(tf.name, 'r') as f:
        for line in f:
            print(line)
    new_dict = {"Title":[],"Author":[],"ISBN13":[],"Pages":[]}
    reader = csv.DictReader(open(tf.name))
    for row in reader:
      new_dict['Title'].append(row["Title"])
      new_dict['Author'].append(row["Author"])
      new_dict['ISBN13'].append(row["ISBN13"])
      new_dict['Pages'].append(row["Pages"])
    print(new_dict)

back_and_forth()
#https://stackoverflow.com/questions/39983886/python-writing-and-reading-from-a-temporary-file
