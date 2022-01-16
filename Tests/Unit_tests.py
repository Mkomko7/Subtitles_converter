import unittest
from _Subs_Converter import Processor


class MyTestCase(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     Processor()

    def test_check_input_int(self):
        result = Processor.check_input("5")
        self.assertEqual(5, result)  # add assertion here

    def test_check_input_float(self):
        result = Processor.check_input("5.4")
        self.assertEqual(5.4, result)  # add assertion here

    def test_check_input_str_fail(self):
        with self.assertRaises(ValueError):
            Processor.check_input("asdf")

    def test_check_input_empty(self):
        with self.assertRaises(ValueError):
            Processor.check_input("")

    def test_list_sub_files_match(self):
        files_list = ["subs.txt"]
        extensions = (".txt", ".ass")
        out_list = Processor.list_sub_files(files_list, extensions)
        self.assertListEqual(files_list, out_list)

    @unittest.expectedFailure
    def test_list_sub_files_no_match(self):
        files_list = ["subs.shp"]
        extensions = (".txt", ".ass", ".srt")
        out_list = Processor.list_sub_files(files_list, extensions)
        self.assertListEqual(files_list, out_list)


if __name__ == '__main__':
    unittest.main()
