import unittest
from my_module.person import Person


class TestPerson(unittest.TestCase):
    def test_hello(self):
        p = Person("Alice", 30)
        self.assertEqual(p.hello(), "Hello, my name is Alice.")

    def test_have_birthday(self):
        p = Person("Bob", 25)
        p.have_birthday()
        self.assertEqual(p.age, 26)


if __name__ == "__main__":
    unittest.main()
