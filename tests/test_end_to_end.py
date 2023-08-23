from src import main
from unittest.mock import patch
import pytest

"""
    Let's start by creating test cases for the main() function that cover three basic scenarios:

    a. Uploading a file with valid input.
    b. Uploading a file with invalid input and then selecting not to download.
    c. Downloading a file with valid input.
    (Add more tests scenarios to get more code coverage)

    For each scenario, we'll simulate user input and check whether the expected behavior occurs in response.
"""

#--------------------------------------------------------------------------------------


@pytest.mark.parametrize("inputs", [
    ['yes', 'assets/test_file_11.txt', 'no'],      # Scenario A
    ['invalid', 'no'],                # Scenario B
    ['no', 'yes', 'level-3.png']  # Scenario C
])
def test_main_function(inputs, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.main()
