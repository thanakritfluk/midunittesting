import unittest
from python.string_util import concat, remove_duplicate, duplicate, find


class TestString(unittest.TestCase):
    def test_simple_concat(self):
        a = 'fl'
        b = 'uk'
        self.assertEquals('fluk', concat(a, b))

    def test_error_concat(self):
        a = 1
        b = 2
        self.assertRaises(TypeError, concat, a, b)

    def test_borderline_concat(self):
        a = '1'
        b = '2'
        self.assertEquals('12', concat(a, b))

    def test_simple_rm_duplicate(self):
        a = 'aaabb'
        self.assertEquals('ab', remove_duplicate(a))

    def test_borderline_rm_duplicate(self):
        a = 'ab'
        self.assertEquals('ab', remove_duplicate(a))

    def test_error_rm_duplicate(self):
        a = 111
        self.assertRaises(TypeError, remove_duplicate, a)

    def test_simple_duplicate(self):
        a = 'Hello'
        b = 5
        self.assertEquals('HelloHelloHelloHelloHello', duplicate(a, b))

    def test_error_duplicate(self):
        a = 1
        b = 'a'
        self.assertRaises(TypeError, duplicate, a, b)

    def test_borderline_duplicate(self):
        a = 'ab'
        b = 1
        self.assertEquals('ab', duplicate(a, b))

    def test_simple_find(self):
        a = 'abc'
        finds = 'c'
        self.assertEquals(2, find(a, finds))

    def test_borderline_find(self):
        a = 'a'
        char = 'a'
        self.assertEquals(0, find(a, char))

    def test_error_find(self):
        a = 1
        finds = 1
        self.assertRaises(TypeError, find, a, finds)


if __name__ == '__main__':
    unittest.main()
