# Sync Dropbox Folder

Sync Dropbox Folder is a Python application that allows you to synchronize a local folder with Dropbox using the Dropbox API V2. It provides a user-friendly way to upload and download files from your Dropbox account while adhering to industry-standard coding practices.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Assumptions](#assumptions)
- [Future Features](#future-features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   `git clone https://github.com/cgmoganedi/sync-dropbox-folder.git && cd sync_dropbox_folder`

2. Set up a virtual environment:
    `python -m venv venv && source venv/bin/activate` or `python -m venv venv && ./venv/bin/activate` depending on the terminal used.

3. Install the required packages:
    `pip install -r requirements.txt` or manually like so: `pip install dropbox python-dotenv pytest pytest-cov pytest-html`

4. Create a `.env` file in the project root and add your Dropbox access token :
    `touch .env`
    and add in it:
    DROPBOX_ACCESS_TOKEN=<your_access_token_here>

## Usage

1. Modify the `local_file_path` and `remote_file_path` variables in `src/main.py` to specify the paths for your local and remote files in Dropbox.

2. Run the application:
    `python src/main.py`
    The application will upload the specified local file to Dropbox and then download it as "downloaded_file.txt".

3. Test Reports and Coverage:
    To generate test reports and coverage for your tests, follow these steps:

    a. Run tests with coverage: `pytest --cov=src --cov-report=html`
        This command will run your tests and generate both a terminal report and an HTML coverage report. The HTML coverage report will be located in the htmlcov directory.
    b. View HTML Coverage Report
        Open the generated HTML report in a web browser to view the coverage details: `open htmlcov/index.html`
    c. Test Reports:
        You can also generate HTML test reports using pytest-html: `pytest --html=report.html`
        This command will generate an HTML report named report.html in your current directory. Open the HTML report in a web browser to view the detailed test results.

    Explanation, in addition to unit tests:
        ◉ Integration Test: The `test_integration_upload_and_download` function tests the interaction between the `upload_file` and `download_file` methods of the DropboxSync class. It simulates uploading a test file, then downloading it and checks if the methods were called appropriately.

        ◉ End-to-End Test: The `test_end_to_end_integration` function runs the `main.py` script as a subprocess, which simulates the end-to-end behavior of your program. It checks if the downloaded file exists after running the script.

        By including integration and end-to-end tests, you ensure that the program's components work together as expected and that the entire workflow is functioning correctly. The coverage report helps you identify which parts of the codebase are being tested and which might need more testing. Test reports provide clear visibility into the test results and coverage, making it easier to track and address any issues in the code.


## Assumptions

◉ This application assumes that you have a valid Dropbox access token obtained from the Dropbox App Console.
◉ The application currently supports uploading and downloading single files to and from Dropbox.

## Future Features

◉ Directory synchronization: Enhance the application to support synchronizing entire directories between local and remote.
◉ Batch processing: Implement the ability to upload/download multiple files in one operation.
◉ User-friendly interface: Develop a graphical user interface (GUI) to provide a more intuitive experience for users.
◉ Error handling improvement: Implement more robust error handling and logging mechanisms.
◉ Encryption: Add an option to encrypt files before uploading them to Dropbox for enhanced security.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

    1. Fork the repository.
    2. Create a new branch for your feature or bug fix.
    3. Make your changes and test thoroughly.
    4. Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Please replace placeholders (`<your_access_token_here>`, `your-username`, etc.) with your actual information. The README.md file provides an overview of your application, how to set it up, use it, and future enhancements that can be made. It's a great way to communicate the purpose and functionality of your project to potential users and contributors.

## Additional explanation (Optional)

Software Design Patterns and Principles Applied:
    ◉ Singleton Pattern: The DropboxSync class follows the Singleton pattern, ensuring that only one instance of the Dropbox API is created and reused throughout the program.
    ◉ Dependency Injection: The DropboxSync class's dependency (access token) is injected through its constructor, promoting loose coupling and easier testing.
    ◉ Single Responsibility Principle (SRP): Each method in the DropboxSync class has a single responsibility, either uploading or downloading files from Dropbox.
    ◉ Exception Handling: Proper exception handling using try-except blocks is implemented to handle Dropbox API errors and provide meaningful error messages.
    ◉ Separation of Concerns: The code is structured with separation between Dropbox synchronization logic (DropboxSync class) and the main script (main.py).
    ◉ Configuration Management: The .env file is used to store sensitive configuration data, promoting security and separation of configuration from code.
    ◉ Unit Testing: Unit tests are written using the Pytest framework to ensure the functionality and robustness of the DropboxSync class methods.

Remember, this is a basic example to showcase the key concepts requested. In a real-world scenario, you would likely implement more comprehensive error handling, logging, and possibly additional design patterns and principles based on the complexity and requirements of the project.