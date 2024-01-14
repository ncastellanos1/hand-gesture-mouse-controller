from unittest import TestCase, mock

import cv2

from utils import load_cascade


class TestLoadCascade(TestCase):

    @mock.patch('os.path.isfile')
    @mock.patch('cv2.CascadeClassifier')
    def test_load_cascade_success(self, mock_cascade_classifier, mock_isfile):
        mock_isfile.return_value = True
        file = 'some_path/haarcascade_frontalface_default.xml'

        result = load_cascade(file)

        mock_isfile.assert_called_with(file)
        mock_cascade_classifier.assert_called_with(file)
        self.assertIsNotNone(result)

    @mock.patch('os.path.isfile')
    def test_load_cascade_file_not_found(self, mock_isfile):
        mock_isfile.return_value = False
        file = 'non_existent_file.xml'

        with self.assertRaises(ValueError) as context:
            load_cascade(file)

        self.assertEqual(str(context.exception), f'Cascade classifier file not found: {file}')
