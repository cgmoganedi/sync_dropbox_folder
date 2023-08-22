import os
from dropbox_sync import DropboxSync


def main():
    access_token = os.getenv("DROPBOX_ACCESS_TOKEN")
    local_directory_path = os.getenv("LOCAL_DIRECTORY")
    remote_directory_path = os.getenv("REMOTE_DIRECTORY")

    if not access_token:
        raise ValueError("Dropbox access token not provided in .env file")

    elif not local_directory_path or not remote_directory_path:
        raise ValueError(
            "Directory paths have been not provided well in .env file")

    dropbox_sync = DropboxSync(access_token)
    success = dropbox_sync.sync_directories(
        local_directory_path, remote_directory_path)
    print(success)


if __name__ == "__main__":
    main()
