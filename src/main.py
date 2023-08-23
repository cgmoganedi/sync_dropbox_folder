import os
from dotenv import load_dotenv
from dropbox_sync import DropboxSync

WELCOME = '\n📦 Welcome to Dropbox Scoped App file downloader/uploader! 🚀\n'

# Load environment variables from .env file
load_dotenv()


def main():
    access_token = os.getenv('DROPBOX_ACCESS_TOKEN')
    if not access_token:
        raise ValueError('Dropbox access token not provided in .env file')

    dropbox_sync = DropboxSync(access_token)
    print(WELCOME)

    upload = input('\nWould you like to upload a file 📄 ? (yes/no) : ').lower()

    if upload == 'yes' or upload == 'y':
        file_relative_path = input(
            '\nWhat is the relative path (with extention) of the local file? : ./')

        completion = dropbox_sync.upload_file(file_relative_path)
        print(completion)

    download = input(
        '\nWould you now like to download a file 📄 ? (yes/no) : ').lower()
    if download == 'yes' or download == 'y':
        file_relative_path = '/' + input(
            '\nWhat is the relative path (with extention) of the remote file in the scoped app? : /')

        completion = dropbox_sync.download_file(file_relative_path)
        print(completion)

    print('... Bye! 👋\n')


if __name__ == '__main__':
    main()
