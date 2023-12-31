import os
import pytest
from src.dropbox_sync import DropboxSync


@pytest.fixture
def dropbox_sync():
    access_token = os.getenv("DROPBOX_ACCESS_TOKEN_TEST")
    return DropboxSync(access_token)


def test_upload_file(dropbox_sync, mocker):
    mock_files_upload = mocker.patch.object(dropbox_sync.dbx.files, 'upload')
    dropbox_sync.upload_file("assets/test_file_11.txt")
    mock_files_upload.assert_called_once()


def test_download_file(dropbox_sync, mocker):
    mock_files_download = mocker.patch.object(dropbox_sync.dbx.files, 'download')
    dropbox_sync.download_file("assets/test_file_1.txt")
    mock_files_download.assert_called_once()
