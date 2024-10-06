import smtplib
from email.mime.text import MIMEText
import pandas as pd
from datetime import datetime

# Path to the Excel file
excel_file_path = r"C:\Users\durga\OneDrive\Desktop\Projects\Job-Application-Tracker-Automated-Email-Sending-and-Recruiter-Log\reclog.xlsx"

# Function to send emails
def send_email(to_email, recruiter_name):
    # Email content
    subject = "Job Application"
    body = f"Dear {recruiter_name},\n\nI hope this message finds you well. I am writing to express my interest in potential job opportunities.\n\nBest regards,\nYour Name"

    # Set up the email server for Yahoo
    smtp_server = "smtp.mail.yahoo.com"
    smtp_port = 587  # Common port for TLS
    sender_email = "ganigan64@rocketmail.com"  # Replace with your email
    sender_password = "8888888"  # Use your password or if 2 step enable Use the app password generated from your email settings(16digit code)

    # Create the email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print(f"Email sent to {recruiter_name} ({to_email})")
        log_recruiter_details(recruiter_name, to_email)  # Log details after sending
    except Exception as e:
        print(f"Failed to send email to {recruiter_name} ({to_email}): {e}")

# Function to log recruiter details in Excel
def log_recruiter_details(recruiter_name, email):
    # Load the existing Excel file
    try:
        df = pd.read_excel(excel_file_path)
    except FileNotFoundError:
        # Create a new DataFrame if the file doesn't exist
        df = pd.DataFrame(columns=["Recruiter Name", "Email", "Date Sent"])

    # Create a new DataFrame for the new data
    new_data = pd.DataFrame({
        "Recruiter Name": [recruiter_name],
        "Email": [email],
        "Date Sent": [datetime.now().strftime('%Y-%m-%d')]
    })

    # Concatenate the new data to the existing DataFrame
    df = pd.concat([df, new_data], ignore_index=True)

    # Save the updated DataFrame back to the Excel file
    df.to_excel(excel_file_path, index=False)

# Example recruiters list
recruiters = [
    {'name': 'Vighneswara', 'email': 'vighneswara.manda@gmail.com'},
    {'name': 'Reddy', 'email': 'durgareddy86@gmail.com'}
]

# Test sending emails
for recruiter in recruiters:
    send_email(recruiter['email'], recruiter['name'])
