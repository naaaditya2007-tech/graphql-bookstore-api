import unittest
from resolver import resolve_book_query

class TestGraphQL(unittest.TestCase):
    def test_resolver(self):
        res = resolve_book_query("1", ["title"])
        self.assertEqual(list(res.keys()), ["title"])

if __name__ == "__main__":
    unittest.main()
