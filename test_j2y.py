import unittest
import j2y
import os


class TestJSONtoYAML(unittest.TestCase):

    # Test getting the yaml file name from absolute path for json file
    def test_get_yaml_file_name(self):
        starting_file = "/Users/Bob/projects/zcw_python/splitting_files/testy.json"
        expected = 'testy.yaml'
        actual = j2y.get_yaml_file_name(starting_file)
        self.assertEqual(expected, actual)  # add assertion here

    # Test getting the yaml file name from relative json file path is working
    def test_get_yaml_file_name2(self):
        starting_file = "ricky.json"
        expected = 'ricky.yaml'
        actual = j2y.get_yaml_file_name(starting_file)
        self.assertEqual(expected, actual)  # add assertion here

    # Test that converting json to yaml is working (Enhance with setup/tear down to remove the file)
    def test_convert_file_to_json(self):
        starting_file = "donuts.json"
        output_file = "donuts.yaml"
        j2y.convert_file_to_yaml(starting_file, output_file)
        expected = True
        actual = os.path.exists(output_file)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
