#   ----------------------------------------------------------------------------
#   "THE BEER-WARE LICENSE" (Revision 42):
#   Daniel Kratzert <dkratzert@gmx.de> wrote this file.  As long as you retain
#   this notice you can do whatever you want with this stuff. If we meet some day,
#   and you think this stuff is worth it, you can buy me a beer in return.
#   ----------------------------------------------------------------------------
import unittest

import gemmi

from cif.text import quote, utf8_to_str, retranslate_delimiter, delimit_string, charcters


class TestText(unittest.TestCase):

    def setUp(self) -> None:
        d = gemmi.cif.Document()
        self.block: gemmi.cif.Block = d.add_new_block('new-block')

    def test_quote_short(self):
        q = quote('Hello this is a test for a quoted text')
        self.assertEqual("'Hello this is a test for a quoted text'", q)

    def test_quote_long(self):
        q = quote('This is a moch longer text, because I want to see what this method does with text over 80 '
                  'characters wide. Let\'s add also some special characters; ?!"§$%&/()=`? Oh yeah!#++-_.,:;')
        quoted = (";\n"
                  "This is a moch longer text, because I want to see what this method does with\n"
                  "text over 80 characters wide. Let's add also some special characters;\n"
                  "?!\"§$%&/()=`? Oh yeah!#++-_.,:;\n"
                  ";")
        self.assertEqual(quoted, q)

    def test_set_pair_delimited_empty(self):
        self.block.set_pair('_foobar', delimit_string(''))
        self.assertEqual(['_foobar', ''], self.block.find_pair('_foobar'))

    def test_set_pair_delimited_question(self):
        self.block.set_pair('_foobar', delimit_string('?'))
        self.assertEqual(['_foobar', '?'], self.block.find_pair('_foobar'))

    def test_set_pair_delimited_number(self):
        self.block.set_pair('_foobar', delimit_string('1.123'))
        self.assertEqual(['_foobar', '1.123'], self.block.find_pair('_foobar'))

    def test_set_pair_delimited_with_newline(self):
        self.block.set_pair('_foobar', delimit_string('abc\ndef foo'))
        self.assertEqual(['_foobar', 'abc\ndef foo'], self.block.find_pair('_foobar'))

    def test_delimit_ut8_to_cif_str(self):
        s = utf8_to_str('100 °C')
        self.assertEqual(r'100 \%C', s)

    def test_cif_str_to_utf8(self):
        r = retranslate_delimiter(r'100 \%C')
        self.assertEqual('100 °C', r)

    def test_retranslate_sentence(self):
        r = retranslate_delimiter("Crystals were grown from thf at -20 \%C.")
        self.assertEqual('Crystals were grown from thf at -20 °C.', r)

    def test_delimit_umlaut(self):
        self.assertEqual(r'a\"o\"u\"\,c', delimit_string('äöüç'))

    def test__backwards_delimit_umlaut(self):
        self.assertEqual('äöüç', retranslate_delimiter(r'a\"o\"u\"\,c'))

    def test_retranslate_all(self):
        for char in charcters:
            if char in ('Å', 'Å'):
                continue
            self.assertEqual(char, retranslate_delimiter(delimit_string(char)))