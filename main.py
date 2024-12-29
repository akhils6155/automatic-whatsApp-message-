from twilio.rest import Client
from datetime import datetime, timedelta
import time
import os

# Step 1: Twilio Setup
account_sid = ''  # Replace with your SID
auth_token = ''  # Replace with your Auth Token
client = Client(account_sid, auth_token)

# Step 2: Define the function to send the WhatsApp message
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # Replace with your Twilio WhatsApp number
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print("Message sent successfully!")
    except Exception as e:
        print("Error while sending message:", str(e))

# Step 3: User input and scheduling
try:
    # Collect inputs
    name = input("Enter the recipient's name: ")
    recipient_number = input("Enter the recipient's WhatsApp number with country code: ").strip()
    message_body = input("Enter the message body: ").strip()
    date_str = input("Enter the date to send the message in YYYY-MM-DD format: ").strip()
    time_str = input("Enter the time to send the message in HH:MM format: ").strip()

    # Convert the date and time strings to a datetime object
    datetime_obj = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
    current_datetime = datetime.now()

    # Calculate the difference between the current time and the scheduled time
    time_diff = datetime_obj - current_datetime
    delay_seconds = time_diff.total_seconds()

    # Check if the scheduled time is in the future
    if delay_seconds <= 0:
        print(f"We cannot send the message at {datetime_obj} because it is in the past.")
    else:
        # Schedule the message
        print(f"Message scheduled to {recipient_number} at {datetime_obj}. Please wait...")
        time.sleep(delay_seconds)  # Wait until the scheduled time
        send_whatsapp_message(recipient_number, message_body)  # Send the message
except ValueError as ve:
    print("Invalid date or time format. Please use YYYY-MM-DD for the date and HH:MM for the time.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
