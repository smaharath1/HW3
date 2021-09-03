import csv
import pandas as pd
def toCSV():
    my_dict = {"Title": ["1984", "Animal Farm", "Brave New World"], "Author": ["George Orwell", "George Orwell", "Aldous Huxley"], "ISBN13": ["978-0451524935", "978-04515266342", "978-0060929879"], "Pages": [268, 144, 288]}
    df = pd.DataFrame(my_dict)
    df.to_csv('test.csv', sep = ',', index = False)

toCSV()
