import unittest
from hello import greet


class TestGreeting(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(
            greet("Jenkins"),
            "Hello, Jenkins!"
        )


if __name__ == "__main__":
    unittest.main()
