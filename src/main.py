import os
from dropbox_sync import DropboxSync

def main():
    access_token = os.getenv("DROPBOX_ACCESS_TOKEN")
    if not access_token:
        raise ValueError("Dropbox access token not provided in .env file")

    dropbox_sync = DropboxSync(access_token)

    local_file_path = "local_folder/file.txt"
    remote_file_path = "/remote_folder/file.txt"

    dropbox_sync.upload_file(local_file_path, remote_file_path)
    dropbox_sync.download_file(remote_file_path, "downloaded_file.txt")

if __name__ == "__main__":
    main()
