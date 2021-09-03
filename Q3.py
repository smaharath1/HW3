import csv
import pandas as pd
def toCSV():
    my_dict = {"Title": ["1984", "Animal Farm", "Brave New World"], "Author": ["George Orwell", "George Orwell", "Aldous Huxley"], "ISBN13": ["978-0451524935", "978-04515266342", "978-0060929879"], "Pages": [268, 144, 288]}
    df = pd.DataFrame(my_dict)
    df.to_csv('test.csv', sep = ',', index = False)

toCSV()
#https://www.w3schools.com/python/python_dictionaries.asp
#https://stackoverflow.com/questions/50151228/write-list-of-dict-to-csv-with-custom-delimiter
#https://stackoverflow.com/questions/56515400/why-does-pandas-add-numbers-at-beginning-of-csv-file-after-converting
