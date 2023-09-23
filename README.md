# Skip The Dishes Earnings Report Generator

This Python script allows you to fetch your earnings statements from Skip The Dishes for the year 2022, separate tips from earnings, and generate a report to help with your tax purposes. It requires your user token, app token, and user ID to access your Skip The Dishes account.

## Prerequisites

Before you can use this script, make sure you have the following:

- Python 3.x installed on your system.
- Required Python libraries installed. You can install them using `pip`:

```bash
pip install python-dotenv
```

## Usage

1. Clone this repository or download the `skip.py` script to your local machine.

2. Open the terminal and navigate to the directory where the script is located.

3. Create a `.env` file similar to `.example.env` and add in values for `USER_TOKEN`, `APP_TOKEN`, and `USER_ID` with your Skip The Dishes credentials.

4. Run the script with the following command:

```bash
python skip.py
```

4. The script will fetch your earnings statements for the year 2022, separate tips from earnings, and generate a table with total earnings in tips and total earnings without tips. The table will be displayed in the terminal.

## Example Output

```plaintext
+---------------------+---------------------+
| Total Earnings (with Tips) | Total Earnings (without Tips) |
+---------------------+---------------------+
|         $1234.56           |          $987.65            |
+---------------------+---------------------+
```

## Note

- This script relies on your Skip The Dishes credentials, so keep them confidential.

## Disclaimer

This script is provided for educational purposes and personal use only. Use it responsibly and in compliance with Skip The Dishes' terms of service and any applicable laws and regulations.
