import unittest
from scanner import Scanner

class TestScanner(unittest.TestCase):
    def test_localhost_alive(self):
        scanner = Scanner()
        result = scanner.scan_ip("127.0.0.1")
        self.assertTrue(result.is_alive)

    def test_invalid_ip(self):
        scanner = Scanner()
        result = scanner.scan_ip("10.255.255.1")  # unlikely to exist
        self.assertFalse(result.is_alive)

if __name__ == '__main__':
    unittest.main()