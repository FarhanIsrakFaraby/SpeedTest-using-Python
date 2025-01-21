# Internet Speed Test Program

This Python program measures your internet download and upload speeds. It allows you to choose a server location from Bangladesh, India, Singapore, USA, or the UK, or it can select the best available server automatically.

## Requirements

- Python 3.6+
- `speedtest-cli` library

The program requires a Python virtual environment to ensure isolation and correct installation of all dependencies.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/speedtest-program.git
   cd speedtest-program
   ```

2. **Create a Virtual Environment**:
   In the project directory, run the following command to create a virtual environment:
   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   With the virtual environment activated, run:
   ```bash
   pip install speedtest-cli
   ```

## How to Run the Code

1. Ensure the virtual environment is activated.
2. Run the Python script:
   ```bash
   python test.py
   ```

   When prompted, choose a server location:
   - `BD` for Bangladesh
   - `IND` for India
   - `SG` for Singapore
   - `USA` for the United States
   - `UK` for the United Kingdom

   If you want to select automatic server then type 'AUTO', it will select the best server for you.

## Example Usage

```text
Welcome to the Speed Test Program!
Choose a server location: BD, IND, SG, USA, UK
Enter your choice: BD
Speed test is running...
Your download speed is: 35.78 Mbps
Your upload speed is: 20.45 Mbps
```
