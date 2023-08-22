import os
from dropbox_sync import DropboxSync

WELCOME = '\n📦 Welcome to Dropbox Scoped App file downloader/uploader! 🚀\n'
def main():
    access_token = os.getenv('DROPBOX_ACCESS_TOKEN')
    if not access_token:
        raise ValueError('Dropbox access token not provided in .env file')

    dropbox_sync = DropboxSync(access_token)
    print(WELCOME)

    upload = input('\nWould you like to upload a file 📄 ? (yes/no) : ')
    if upload == 'yes':
        file_name = '/' + input(
            '\nWhat is the name (with extention) of the file in the current working director? : ./')
        completion = dropbox_sync.upload_file(file_name, file_name)
        print(completion)

    download = input('\nWould you now like to download a file 📄 ? (yes/no) : ')
    if download == 'yes':
        file_name = '/' + input(
            '\nWhat is the path (with extention) of the remote file in the scoped app? : /')
        completion = dropbox_sync.download_file(file_name, file_name)
        print(completion)

    print('... Bye! 👋\n')

if __name__ == '__main__':
    main()
