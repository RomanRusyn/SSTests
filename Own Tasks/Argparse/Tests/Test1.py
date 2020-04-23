import filecmp
import unittest



class MyTestCase(unittest.TestCase):

    def test_parser(self, ):
        self.assertTrue(filecmp.cmp("../out.txt",
                                    "out2.txt"))


if __name__ == '__main__':
    unittest.main()
