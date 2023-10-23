import pandas_gbq
import pydata_google_auth

def authenticate_google():
    SCOPES = [
        'https://www.googleapis.com/auth/cloud-platform',
        'https://www.googleapis.com/auth/drive',
    ]

    credentials = pydata_google_auth.get_user_credentials(
        SCOPES,
        # Note, this doesn't work if you're running from a notebook on a
        # remote sever, such as over SSH or with Google Colab. In those cases,
        # install the gcloud command line interface and authenticate with the
        # `gcloud auth application-default login` command and the `--no-browser`
        # option.
        auth_local_webserver=True,
    )
    return credentials

