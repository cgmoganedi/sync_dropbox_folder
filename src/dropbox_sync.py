import os
import dropbox
from dotenv import load_dotenv

load_dotenv()


class DropboxSync:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(access_token)

    def upload_file(self, local_path, remote_path):
        """Upload a local file to Dropbox."""
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

    def sync_directories(self, directory_one, directory_two, count=0):
        """Sync all contents of a local directory with Dropbox."""
        if count == 2:
            return 'Success!'

        try:
            for root, _, files in os.walk(directory_one):
                for file in files:
                    local_path = os.path.join(root, file)
                    relative_path = os.path.relpath(local_path, directory_one)
                    remote_path = os.path.join(directory_two, relative_path)
                    if count == 0:
                        self.upload_file(local_path, remote_path)
                    elif count == 1:
                        self.download_file(local_path, remote_path)

            return self.sync_directory(self, directory_two, directory_one, count+1)
        except Exception as e:
            print(
                f'Problem syncing {directory_one} with {directory_two} on count={count}: ', str(e))
