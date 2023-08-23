import os
import pytest
from src.dropbox_sync import DropboxSync


@pytest.fixture
def dropbox_sync():
    access_token = os.getenv("DROPBOX_ACCESS_TOKEN_TEST")
    return DropboxSync(access_token)


def test_integration_upload_and_download(dropbox_sync, mocker, tmp_path):
    local_path = tmp_path / "assets/test_file_11.txt"
    remote_path = "assets/test_file_1.txt"

    # Create a temporary test file
    with open(local_path, "w") as f:
        f.write("Test content")

    mock_files_upload = mocker.patch.object(dropbox_sync.dbx.files, "upload")
    mock_files_download = mocker.patch.object(dropbox_sync.dbx.files, "download")

    dropbox_sync.upload_file(local_path)
    dropbox_sync.download_file(remote_path)

    mock_files_upload.assert_called_once()
    mock_files_download.assert_called_once()
