import os
import dropbox
from dotenv import load_dotenv

load_dotenv()

class DropboxSync:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(access_token)

    def upload_file(self, local_path, remote_path):
        """Upload a file to Dropbox."""
        try:
            with open(local_path, 'rb') as f:
                self.dbx.files_upload(f.read(), remote_path)
        except dropbox.exceptions.ApiError as e:
            print(f"Error uploading file: {e}")

    def download_file(self, remote_path, local_path):
        """Download a file from Dropbox."""
        try:
            metadata, response = self.dbx.files_download(remote_path)
            with open(local_path, 'wb') as f:
                f.write(response.content)
        except dropbox.exceptions.ApiError as e:
            print(f"Error downloading file: {e}")
