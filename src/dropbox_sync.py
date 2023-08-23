import os
import dropbox
from dotenv import load_dotenv

load_dotenv()


class DropboxSync:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(access_token)

    def upload_file(self, local_path, remote_path)-> str:
        """Upload a local file to Dropbox."""
        try:
            with open(local_path, 'rb') as f:
                self.dbx.files_upload(f.read(), remote_path)
            return '\nUpload Success!'
        except Exception as e:
            print(f"Error uploading file: {e}")
            return '\nUpload Failed!'

    def download_file(self, remote_path, local_path)-> str:
        """Download a file from Dropbox."""
        try:
            metadata, response = self.dbx.files_download(remote_path)
            with open(local_path, 'wb') as f:
                f.write(response.content)
            return '\nDownload Success!'
        except Exception as e:
            print(f"Exception while downloading file: {e}")
            return '\nDownload Failed!'

