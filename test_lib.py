from main import reverse
import unittest


class TestReverse(unittest.TestCase):
    def test_emty(self):
        self.assertEquals(reverse(""), "")

    def test_correct(self):
        self.assertEquals(reverse("abcd"), "dcba")

    def test_singl(self):
        self.assertEquals(reverse("a"), "a")

    def test_polindrom(self):
        self.assertEquals(reverse("aba"), "aba")

    def test_list(self):
        with self.assertRaises(TypeError):
            reverse(['a', 'b', 'c'])

    def test_wrong_emty(self):
        with self.assertRaises(TypeError):
            reverse(42)


if __name__ == "__main__":
    unittest.main()
