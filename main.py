import os.path
import csv
import datetime as dt 
from datetime import datetime,timedelta
from time import strftime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build 

SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Function to read emails from CSV
def get_emails_from_csv(csv_file):
    emails = []
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row["email"]
            emails.append({"email": email, "optional": False})  # Add the email to the list of attendees
    return emails

def main():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json","w") as token:
            token.write(creds.to_json())
    
    try:
        service = build("calendar", "v3", credentials=creds)

        start_time = datetime(2025,1,25,20,0,0) #(yyyy,mm,dd,hr,min,sec)
        end_time = start_time + timedelta(minutes= 45)
        timeZone = 'Asia/Kolkata'

        # Read emails from CSV
        attendees = get_emails_from_csv("emails.csv")  # Pass the path of your CSV file

        event = {
            'summary': 'Lifegroup Meet',
            'location':'Zoom, Online',
            'description':'I am testing so we can use it for Online campus',
            'colorId': 5,
            'start':{
                'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone' : timeZone,
                     },
            'end':{
                'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone' : timeZone
            },

             "recurrence": [
                "RRULE:FREQ=WEEKLY;INTERVAL=1"  # Recurs weekly
            ],
            "attendees": attendees,
        }

        event = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Event created {event.get('htmlLink')}")

    except HttpError as error:
        print("An error occurred: ", error)


if __name__ == "__main__":
    main()
    