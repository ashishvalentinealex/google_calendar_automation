# Google Calendar Event Automation

This Python script allows you to create Google Calendar events programmatically by reading a list of email addresses from a CSV file. The event is created in your primary calendar and invites the users from the CSV file.

## Features
- Reads emails from a CSV file
- Creates a Google Calendar event
- Sends invitations to listed attendees
- Supports setting event details like time, location, and description
- Configures event recurrence (optional)

## Prerequisites
Before you can run the script, ensure you have the following:

- Python 3.6+ installed
- Google Calendar API credentials (OAuth 2.0 credentials)

### 1. Install Python and Dependencies

First, make sure you have Python 3.6 or higher installed. You can download it from [here](https://www.python.org/downloads/).

Then, install the required libraries using `pip`. Run the following commands in your terminal:

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 2. Set Up Google Calendar API

Follow these steps to set up the Google Calendar API:

1. Go to the [Google Developer Console](https://console.developers.google.com/).
2. Create a new project (or select an existing one).
3. Enable the **Google Calendar API** for your project.
4. Create **OAuth 2.0 credentials** (you'll get a `credentials.json` file).
5. Download the `credentials.json` file to the project directory.

### 3. Prepare CSV File for Attendees

Create a CSV file named `emails.csv` containing the email addresses of attendees. The CSV file should look like this:

```csv
email
email1@example.com
email2@example.com
email3@example.com
```

### 4. Token Storage

When you first run the script, it will prompt you to authenticate your Google account and save the credentials as `token.json`. This file will be used for subsequent requests to the Google Calendar API. You only need to authenticate once, and after that, `token.json` will store your access token and refresh token, so you don't have to authenticate again in the future.

## Running the Script

1. Clone or download the repository to your local machine.
2. Place the `credentials.json` and `emails.csv` files in the project directory.
3. Run the script using the following command:

```bash
python main.py
```

## Contributing

Feel free to fork this project, submit issues, or open pull requests. Contributions are welcome!

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](./LICENSE) file for details.

