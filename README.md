# ENGChallengeTestingCIv2
[![Build Status](https://travis-ci.org/ruvinbsu/ENGChallengeTestingCIv2.svg?branch=master)](https://travis-ci.org/ruvinbsu/ENGChallengeTestingCIv2)

## How to connect a repository to Travis CI:
1. Go to the Travis [website](https://travis-ci.org/).
2. Sing in using GitHub account.
3. Wait for repositories sync to complete.
4. Go to your profile (in the top right corner).
5. Enable required repository (i.e. the one you want to connect to Travis).
6. Look into .travis.yml and check whether configs specified there match your desired system requirements.

From now if anything gets pushed (i.e. using git commit & push), Travis will automatically run all tests defined in the codebase.

For more information on Travis please visit this [page](https://docs.travis-ci.com/user/languages/python/).

## Install steps for an user who wants to develop the repo (Running Locally):
1. Fork the repository
2. Clone or download the app
3. Install required modules specified in the requirements.txt (in the root folder of the app). It can be done by running the following command:
```sh
pip install -r requirements.txt
```
4. Now you can simply run image_upload.py module using:
```sh
python image_upload.py
```
or you can make use of gunicorn (WSGI server) that we installed in previous step: 
```sh
web: gunicorn image_upload:app --log-file=-
``


#### Application has been deployed to heroku and can be accessed from [here](https://desolate-inlet-44457.herokuapp.com/).

