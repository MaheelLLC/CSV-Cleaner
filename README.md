## CSV-Cleaner

### What the Application Does
This app makes a csv file with clean people data. It takes raw contacts from data/raw_contacts.csv and transforms and stores it into data/clean_contacts.csv. First, it loads all contacts. Then, it cleans each contact based on certain formatting rules. If a contact breaks a rule or is a duplicate, it is considered invalid and skipped. The remaining, valid contacts are stored into a new clean csv file.

### Requirements
- Python 3.12+ and pip installed
- An installed Python venv

### Installation Instructions
1. Make a local copy of this repository.
2. Move into the repository's directory. (ex. cd csv_cleaner/)
3. Enter in your terminal `python3 -m venv venv`
4. Enter in your terminal 
    - Linux/macOS: `source venv/bin/activate`
    - Windows Powershell: `.\venv\Scripts\Activate.ps1`
5. Enter in your terminal `python3 main.py`