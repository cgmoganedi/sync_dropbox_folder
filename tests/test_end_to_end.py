import os
import subprocess


def test_end_to_end_integration():
    subprocess.run(["python", "src/main.py"], check=True)
    assert os.path.exists("downloaded_file.txt")
