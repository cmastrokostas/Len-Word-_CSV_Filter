import csv
import unicodedata
from Handling.config import origin_file, n

def read_and_filter(origin_file):
    
    # Read Origin File.
    with open(origin_file, 'r') as file:
        reader = csv.reader(file)
        data = [row[0] for row in reader]
    # Create filtered list.
    return data

def remove_duplicates(mylist):
    return list(dict.fromkeys(mylist))

def convert(data, mode = 'plain', distinct = True, word_len = n):
    if mode == 'upper' : # Convert to UpperCase
        new_data = [word.upper() for word in data if (len(word) == word_len )]  
    elif mode == 'upper-clean': # Convert to UpperCase without Accentation
        new_data = [strip_accents(word.upper()) for word in data if ( len(word) == word_len)]
    elif mode == 'plain':
        new_data = [word for word in data if ( len(word) == word_len ) ]
    elif mode == 'plain-clean': # Remove Accentation
        new_data = [strip_accents(word) for word in data if ( len(word) == word_len )]
    else : 
        raise ValueError("Invalid Parameter")
    new_data = remove_duplicates(new_data) if distinct == True else new_data

    return new_data


def write_new(new_data, txt = True):
    csv_file = f'el_GR_n_{n}.csv'
    # Write New File.
    with open(csv_file, 'w', newline='',encoding = "utf-8-sig") as file:
        writer = csv.writer(file, dialect='excel')
        for word in new_data:
            writer.writerow([word])
    if txt : 
        csv_to_txt(csv_file)
    return

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) 
            if unicodedata.category(c) != 'Mn')\

def csv_to_txt(csv_file):
    txt_file = csv_file.replace("csv", "txt")

    with open(txt_file, "w", encoding = "utf-8-sig") as my_output_file:
        with open(csv_file, "r", encoding = "utf-8-sig") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()
    return