# x_9_2
#
# 「assertFalse()」のテストを追加してください。

import unittest


def is_adult(age):
    return age >= 20


class TestMethods(unittest.TestCase):

    def test_is_adult_true(self):
        self.assertTrue(is_adult(20))

    def test_is_adult_false(self):
        self.assertFalse(is_adult(19))


if __name__ == '__main__':
    unittest.main()
