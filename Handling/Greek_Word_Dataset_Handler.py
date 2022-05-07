import csv
from config import origin_file, destination_file, n

def filter_len():
    
    # Read Origin File.
    with open(origin_file, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    
    # Create filtered list.
    new_data = [[word[0]] for word in data if ( len(word[0]) == n ) ]
    
    # Write New File.
    with open(f'el_GR_n_{n}.csv', 'w', newline='',encoding = "utf-8-sig") as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerows(new_data)

    return