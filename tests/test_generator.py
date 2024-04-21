import unittest
from courieruuid.generator import generate_uuid

class TestGenerateUUID(unittest.TestCase):

    def test_uuid_length(self):
        uuid = generate_uuid()
        self.assertEqual(len(str(uuid)), 36)

if __name__ == '__main__':
    unittest.main()
