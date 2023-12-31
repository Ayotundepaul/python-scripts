---

# Python Utility Scripts

A collection of Python scripts to aid in various tasks, from file management to data processing.

## Table of Contents

- [Installation](#installation)
- [Scripts Overview](#scripts-overview)
  - [Rename Files in Directory](#rename-files-in-directory)
  - [Find Duplicate Files](#find-duplicate-files)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository:
   ```bash
   git clone [URL_TO_THIS_GITHUB_REPO]
   ```
2. Navigate to the cloned directory:
   ```bash
   cd path_to_cloned_directory
   ```

## Scripts Overview

### Rename Files in Directory

**Script Name:** `rename_files.py`

**Purpose:** Renames all files in a directory by appending a given prefix.

**Usage:**
```bash
python3 rename_files.py <directory> <prefix>
```

### Find Duplicate Files

**Script Name:** `find_duplicates.py`

**Purpose:** Finds duplicate files based on content in a specified directory.

**Usage:**
```bash
python3 find_duplicates.py <directory>
```

## Usage

Each script is standalone and can be executed using Python 3. After navigating to the script's directory, run:

```bash
python3 script_name.py [arguments...]
```

Check System Health
Script Name: system_health_check.py

Purpose: Retrieves and prints various system health metrics like CPU usage, memory usage, and disk space.

Bulk Rename Files with Pattern
Script Name: bulk_rename.py

Purpose: Renames files in a directory that match a specific pattern.

Parse and Analyze Logs
Script Name: log_analyzer.py

Purpose: Parses a log file to count occurrences of error messages.

Simple Server Status Checker
Script Name: server_status_checker.py

Purpose: Pings a list of servers and checks their availability.

🌐 **Network Speed Tester**: 
    - Measures the upload and download speeds of the current internet connection.
    - Usage: `python network_speed_tester.py`
    - Dependencies: `speedtest-cli`

📦 **Automated Git Repository Cloner**: 
    - Clones a list of git repositories to the local machine.
    - Usage: `python git_repo_cloner.py`

---

Refer to the individual script's "Usage" section above for specific arguments.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please submit a pull request or create an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file in the repository for more details.

---

This README provides a basic overview and usage instructions for the scripts. Depending on the complexity and the audience of your scripts, you might want to expand certain sections, add more details, or include additional sections like "Dependencies," "Known Issues," or "Changelog."


Remember to install any required dependencies before running the scripts.