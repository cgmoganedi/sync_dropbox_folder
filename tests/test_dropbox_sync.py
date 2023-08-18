import pytest
from dropbox_sync import DropboxSync

@pytest.fixture
def dropbox_sync():
    access_token = "test_access_token"
    return DropboxSync(access_token)

def test_upload_file(dropbox_sync, mocker):
    mock_files_upload = mocker.patch.object(dropbox_sync.dbx.files, 'upload')
    dropbox_sync.upload_file("local_path", "remote_path")
    mock_files_upload.assert_called_once()

def test_download_file(dropbox_sync, mocker):
    mock_files_download = mocker.patch.object(dropbox_sync.dbx.files, 'download')
    dropbox_sync.download_file("remote_path", "local_path")
    mock_files_download.assert_called_once()
