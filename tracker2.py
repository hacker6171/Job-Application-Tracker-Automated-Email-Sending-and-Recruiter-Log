import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import os
import pandas as pd
from datetime import datetime

# Path to the Excel file
excel_file_path = r"C:\Users\durga\OneDrive\Desktop\Projects\Job-Application-Tracker-Automated-Email-Sending-and-Recruiter-Log\reclog.xlsx"

# Function to send emails with attachments
def send_email_with_attachment(to_email, recruiter_name, attachment_path):
    # Email content (HTML format)
    subject = "Job Application"
    body_html = f"""
    <html>
    <body>
        <p>Dear {recruiter_name},</p>
        <p>I hope this message finds you well. I am writing to express my interest in potential job opportunities.</p>
        <p>Please find my resume attached.</p>
        <p>Best regards,<br>Manda</p>
    </body>
    </html>
    """

    # Set up the email server for Yahoo
    smtp_server = "smtp.mail.yahoo.com"
    smtp_port = 587
    sender_email = "mymail@rocketmail.com"
    sender_password = "passcode"  # Use your email's app password

    # Create the email
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    # Attach the HTML body to the email
    msg.attach(MIMEText(body_html, 'html'))

    # Attach the file
    try:
        file_extension = os.path.splitext(attachment_path)[1]
        mime_type, _ = {
            '.pdf': ('application', 'octet-stream'),
            '.docx': ('application', 'vnd.openxmlformats-officedocument.wordprocessingml.document'),
            '.txt': ('text', 'plain')
        }.get(file_extension, ('application', 'octet-stream'))

        with open(attachment_path, "rb") as attachment:
            part = MIMEBase(mime_type, _)
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(attachment_path)}"
        )
        msg.attach(part)

    except Exception as e:
        print(f"Failed to attach file: {e}")

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print(f"Email with attachment sent to {recruiter_name} ({to_email})")
        log_recruiter_details(recruiter_name, to_email)
    except Exception as e:
        print(f"Failed to send email to {recruiter_name} ({to_email}): {e}")

# Function to log recruiter details in Excel
def log_recruiter_details(recruiter_name, email):
    try:
        df = pd.read_excel(excel_file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Recruiter Name", "Email", "Date Sent"])

    new_data = pd.DataFrame({
        "Recruiter Name": [recruiter_name],
        "Email": [email],
        "Date Sent": [datetime.now().strftime('%Y-%m-%d')]
    })

    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel(excel_file_path, index=False)

# List of recruiters with emails
recruiters = [
    {'name': 'cnumani', 'email': 'email1@outlook.com'},
    {'name': 'binary', 'email': 'email2@gmail.com'},
    {'name': 'indumanthi', 'email': 'email3@gmail.com'},
    # Add more recruiters here
]

# Resume file path (or any other attachment)
attachment_path = r"paste your own path here"

# Sending bulk emails to recruiters
for recruiter in recruiters:
    send_email_with_attachment(recruiter['email'], recruiter['name'], attachment_path)