import unittest
from StringIO import StringIO
from image_upload import app


class FlaskTestCase(unittest.TestCase):
    def test_image_upload(self):
        # open img
        test_image = open('sample_image_for_upload.png', 'r')
        if test_image:
            test_image_binary = test_image.read()
            test_image_bin_string = StringIO(test_image_binary)
            client = app.test_client()

            # make a post request to upload an img
            resp = client.post('/image_upload/',
                               content_type='multipart/form-data',
                               data={'image': (test_image_bin_string, 'sample_image_for_upload')})

            # test if content of an img sent via POST request is equal to the content of the img in response body
            # self.assertEqual(test_image_binary, resp.data)
            self.assertEqual(1, 2)

        # close opened img
        test_image.close()

if __name__ == '__main__':
    unittest.main()
