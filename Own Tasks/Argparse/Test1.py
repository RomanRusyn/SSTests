import filecmp
import os
import unittest

from Argparse import parser, write_to_file


class MyTestCase(unittest.TestCase):
    def test_parser_little(self):
        parsing_result = parser("ten.txt", 3)
        expected_result = [
            {"url":
                 [{"raw_url": "google.com"},
                  {"raw_url": "youtube.com"},
                  {"raw_url": "facebook.com"}
                  ]},
            {"url":
                 [{"raw_url": "tmall.com"},
                  {"raw_url": "baidu.com"},
                  {"raw_url": "qq.com"}
                  ]},
            {"url":
                 [{"raw_url": "sohu.com"},
                  {"raw_url": "login.tmall.com"},
                  {"raw_url": "taobao.com"}
                  ]},
            {"url":
                 [{"raw_url": "360.cn"}
                  ]}
        ]
        self.assertEqual(parsing_result, expected_result)

    def test_parser_huge_file(self):
        self.assertTrue(filecmp.cmp("Tests/out.txt",
                                    "Tests/out2.txt"))

    def test_path_exists(self):
        self.assertTrue(os.path.exists("Tests/out.txt"))

    def test_write_file(self):
        test_string = [{"url": [{"raw_url": "360.cn"}]}]
        write_to_file(test_string, 'Tests/write_test.txt')
        self.assertTrue(filecmp.cmp("Tests/write_test.txt",
                                    "Tests/handle_write_test.txt"))

    def test_write_no_list(self):
        with self.assertRaises(FileNotFoundError):
            write_to_file('', '')

    def test_write_no_path(self):
        with self.assertRaises(TypeError):
            write_to_file('')


if __name__ == '__main__':
    unittest.main()
