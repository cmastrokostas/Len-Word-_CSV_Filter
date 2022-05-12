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

def convert(data,mode = 'plain', distinct = True):
    
    if mode == 'upper' : # Convert to UpperCase
        new_data = [word.upper().join() for word in data if (len(word) == n )]  
    elif mode == 'upper-clean': # Convert to UpperCase without Accentation
        new_data = [strip_accents(word.upper()) for word in data if ( len(word) == n )]
    elif mode == 'plain':
        new_data = [word for word in data if ( len(word) == n ) ]
    elif mode == 'plain-clean': # Remove Accentation
        new_data = [[strip_accents(word)] for word in data if ( len(word) == n )]
    else : 
        raise ValueError("Invalid Parameter")
    new_data = remove_duplicates(new_data) if distinct == True else new_data

    return new_data


def write_new(new_data):

    # Write New File.
    with open(f'el_GR_n_{n}.csv', 'w', newline='',encoding = "utf-8-sig") as file:
        writer = csv.writer(file, dialect='excel')
        for word in new_data:
            writer.writerow([word])

    return

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) 
            if unicodedata.category(c) != 'Mn')