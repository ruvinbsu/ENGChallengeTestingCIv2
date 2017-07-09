import unittest
from image_upload import app
import io


class FlaskTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        # open imgs
        cls.test_image_pass = open('sample_image_for_upload_success.png', 'rb')
        cls.test_image_fail = open('sample_image_for_upload_failure.jpg', 'rb')

    def test_image_upload_equal(self):
        # value of the first img we read (in a bytes string format)
        test_image_bin_str = self.test_image_pass.read()
        # making offset = 0 (from start of file)
        self.test_image_pass.seek(0)
        # preparing suitable format of the first img for http post request
        test_image_bytes = io.BytesIO(self.test_image_pass.read())
        # make a post request to upload the first img
        resp = self.client.post('/image_upload/',
                           content_type='multipart/form-data',
                           data={'image': (test_image_bytes, 'sample_image_for_upload_success')})

        # test if content of the img sent via POST request is equal to the content of the img in response body
        self.assertEqual(test_image_bin_str, resp.data, "Something went wrong! Images should match.")

    def test_image_upload_not_equal(self):
        # value of the second img we read (in a bytes string format)
        test_image_bin_str = self.test_image_fail.read()
        # preparing suitable format of the first img for http post request
        test_image_bytes = io.BytesIO(self.test_image_pass.read())
        # make a post request to upload the first img
        resp = self.client.post('/image_upload/',
                           content_type='multipart/form-data',
                           data={'image': (test_image_bytes, 'sample_image_for_upload_success')})

        # testing/verifying that two images aren't equal
        self.assertNotEqual(test_image_bin_str, resp.data, "Something went wrong! Images shouldn't match.")

    @classmethod
    def tearDownClass(cls):
        # close opened imgs
        if not cls.test_image_pass.closed:
            cls.test_image_pass.close()
        if not cls.test_image_fail.closed:
            cls.test_image_fail.close()

if __name__ == '__main__':
    unittest.main()
