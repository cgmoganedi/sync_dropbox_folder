import os
import dropbox


class DropboxSync:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(access_token)

    def upload_file(self, file_path):
        try:
            with open(file_path, "rb") as f:
                file_content = f.read()
                self.dbx.files_upload(file_content, '/' + file_path)
            return '\nUpload to Dropbox Success!'
        except Exception as e:
            print("Error uploading to Dropbox:", e)
            return '\nUpload Failed!'

    def download_file(self, remote_path) -> str:
        """Download a file from Dropbox."""
        try:
            metadata, response = self.dbx.files_download('/' + remote_path)
            local_path = remote_path
            self.create_directories(local_path)
            with open(local_path, 'wb') as f:
                f.write(response.content)
            return '\nDownload from Dropbox Success!'
        except Exception as e:
            print("Error downloading from Dropbox:", e)
            return '\nDownload Failed!'

    def create_directories(self, path):
        # Get the directory path without the filename
        dir_path = os.path.dirname(path)

        # Create directories recursively if they don't exist
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
