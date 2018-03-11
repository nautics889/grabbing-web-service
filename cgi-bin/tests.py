from htmlgrabbing import WebHTMLParser

import unittest
import re

class NewTestCase(unittest.TestCase):
    def test_searching(self):
        wp = WebHTMLParser('http://lucid-dijkstra-317bc1.bitballoon.com/')
        self.assertEqual(wp.get_links(), 'https://www.google.com')
        self.assertEqual(wp.get_phones(), '+38 (012) 345-67-89')
        self.assertEqual(wp.get_mails(), 'test@test.test')

    def test_searching_empty(self):
        wp = WebHTMLParser('http://lucid-dijkstra-317bc1.bitballoon.com/')
        wp.links = []
        wp.numbersRegex = re.compile(r'Test regular expression 1')
        wp.mailsRegex = re.compile(r'Test regular expression 2')
        self.assertEqual(wp.get_links(), 'No links was found.')
        self.assertEqual(wp.get_phones(), 'No numbers was found.')
        self.assertEqual(wp.get_mails(), 'No e-mails was found.')

if __name__ == '__main__':
    unittest.main()
