import unittest
from Handling.Greek_Word_Dataset_Handler import remove_duplicates, convert, strip_accents

class TestGrHandler(unittest.TestCase):
    def test_remove_duplicates(self):
        distinct = remove_duplicates(['a','a','a','b','b','c'])
        self.assertEqual(['a','b','c'], distinct)

        distinct = remove_duplicates(['ένα','Δύο','Δύο',3,3,3])
        self.assertEqual(['ένα','Δύο',3], distinct)
    
    def  test_strip_accents(self):
        converted = strip_accents('Έλα')
        self.assertEqual(converted, 'Ελα')

        converted = strip_accents('Ταΰγετος')
        self.assertEqual(converted, 'Ταυγετος')

        converted = strip_accents('χαϊδεύοντάς')
        self.assertEqual(converted,'χαιδευοντας')

    def test_convert(self):
        converted = convert(['πέντε', 'έξι','επτά','οκτώ','εννέα'], word_len = 5 )
        self.assertEqual(converted,['πέντε','εννέα'])

        converted = convert(['πέντε','πέντε','έξι','επτά','οκτώ','εννέα'], distinct = True, word_len = 5 )
        self.assertEqual(converted,['πέντε','εννέα'])

        converted = convert(['πέντε', 'έξι','επτά','οκτώ','εννέα'], mode = 'plain-clean', word_len = 5 )
        self.assertEqual(converted,['πεντε','εννεα'])

        converted = convert(['πέντε', 'έξι','επτά','οκτώ','εννέα'], mode = 'upper', word_len = 5 )
        self.assertEqual(converted,['ΠΈΝΤΕ','ΕΝΝΈΑ'])

        converted = convert(['πέντε', 'έξι','επτά','οκτώ','εννέα'], mode = 'upper-clean', word_len = 5 )
        self.assertEqual(converted,['ΠΕΝΤΕ','ΕΝΝΕΑ'])