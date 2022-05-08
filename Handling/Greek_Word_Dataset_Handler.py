import csv
import unicodedata
from Handling.config import origin_file, n

def read_and_filter(origin_file):
    
    # Read Origin File.
    with open(origin_file, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    # Create filtered list.
    return data


def convert(data,mode = 'plain'):
    
    if mode == 'upper' : # Convert to UpperCase
        new_data = [[word[0].upper()] for word in data if ( len(word[0]) == n )]  
    elif mode == 'upper-clean': # Convert to UpperCase without Accentation
        new_data = [[strip_accents(word[0].upper())] for word in data if ( len(word[0]) == n )]
    elif mode == 'plain':
        new_data = [[word[0]] for word in data if ( len(word[0]) == n ) ]
    elif mode == 'plain-clean': # Remove Accentation
        new_data = [[strip_accents(word[0])] for word in data if ( len(word[0]) == n )]
    else : 
        raise ValueError("Invalid Parameter")
    return new_data


def write_new(new_data):
    # Write New File.
    with open(f'el_GR_n_{n}.csv', 'w', newline='',encoding = "utf-8-sig") as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerows(new_data)

    return

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) 
            if unicodedata.category(c) != 'Mn')