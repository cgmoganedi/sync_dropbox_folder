import pytest
from dropbox_sync import DropboxSync


@pytest.fixture
def dropbox_sync():
    access_token = "test_access_token"
    return DropboxSync(access_token)


def test_integration_upload_and_download(dropbox_sync, mocker, tmp_path):
    local_path = tmp_path / "test_file.txt"
    remote_path = "/test_folder/test_file.txt"

    # Create a temporary test file
    with open(local_path, "w") as f:
        f.write("Test content")

    mock_files_upload = mocker.patch.object(dropbox_sync.dbx.files, "upload")
    mock_files_download = mocker.patch.object(dropbox_sync.dbx.files, "download")

    dropbox_sync.upload_file(local_path, remote_path)
    dropbox_sync.download_file(remote_path, str(tmp_path / "downloaded_file.txt"))

    mock_files_upload.assert_called_once()
    mock_files_download.assert_called_once()
