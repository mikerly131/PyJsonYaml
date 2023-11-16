import unittest
import y2j
import os


class TestYAMLtoJSON(unittest.TestCase):

    # Test getting the json file name from absolute path
    def test_get_json_file_name(self):
        starting_file = "/Users/Bob/projects/zcw_python/splitting_files/testy.yaml"
        expected = 'testy'
        actual = y2j.get_json_file_name(starting_file)
        self.assertEqual(expected, actual)  # add assertion here

    # Test getting the json file name from relative yaml file path is working
    def test_get_JSON_file_name2(self):
        starting_file = "ricky.yaml"
        expected = 'ricky'
        actual = y2j.get_json_file_name(starting_file)
        self.assertEqual(expected, actual)  # add assertion here

    # Test that converting yaml to json is working (Enhance with setup/tear down to remove the file)
    def test_convert_file_to_json(self):
        starting_file = "xmas.yaml"
        output_file = "xmas.json"
        y2j.convert_file_to_json(starting_file, output_file)
        expected = True
        actual = os.path.exists(output_file)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
