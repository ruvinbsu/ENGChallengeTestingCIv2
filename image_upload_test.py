import unittest
from StringIO import StringIO
from image_upload import app


class FlaskTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # open imgs
        cls.test_image_pass = open('sample_image_for_upload_success.png', 'r')
        cls.test_image_fail = open('sample_image_for_upload_failure.jpg', 'r')

    def test_image_upload(self):
        if self.test_image_pass and self.test_image_fail:
            test_image_binary_pass = self.test_image_pass.read()
            test_image_binary_fail = self.test_image_fail.read()
            test_image_bin_string_pass = StringIO(test_image_binary_pass)
            client = app.test_client()

            # make a post request to upload an img
            resp = client.post('/image_upload/',
                               content_type='multipart/form-data',
                               data={'image': (test_image_bin_string_pass, 'sample_image_for_upload_success')})

            # test if content of an img sent via POST request is equal to the content of the img in response body
            self.assertEqual(test_image_binary_pass, resp.data, 'Something went wrong! Images should match.')
            self.assertNotEqual(test_image_binary_fail, resp.data, 'Something went wrong! Images shouldn\'t match.')

    @classmethod
    def tearDownClass(cls):
        # close opened imgs
        cls.test_image_pass.close()
        cls.test_image_fail.close()

if __name__ == '__main__':
    unittest.main()
