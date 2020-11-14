import unittest
import sys

sys.path.insert(1, "../")
import pseudoapp
from pseudoapp import app

KEY_INPUT = "input"
KEY_EXPECTED = "expected"


class on_query_connections_check(unittest.TestCase):
    
    def mocked_request(self):
        pass
    
    def setUp(self):
        self.success_test_params = [
            {
                KEY_EXPECTED:{
                    "success": True,
                    "connections": "",
                },
            },
        ]

    def test_success(self):
        for test in self.success_test_params:
            response = pseudoapp.on_query_connection()
            expected = test[KEY_EXPECTED]

            self.assertEqual(response, expected)

class index_check(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_EXPECTED: "Hello World",
            },
        ]

    def test_success(self):
        for test in self.success_test_params:
            response = pseudoapp.index()
            expected = test[KEY_EXPECTED]

            self.assertEqual(response, expected)

if __name__ == '__main__':
    unittest.main()
