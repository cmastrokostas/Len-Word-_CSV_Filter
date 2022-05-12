from Handling.Greek_Word_Dataset_Handler import read_and_filter, write_new, convert
from Handling.config import origin_file, n, file_to_convert

def main():

    write_new(convert(read_and_filter(origin_file), mode = 'upper-clean'))
    return

if __name__ == '__main__': main()
