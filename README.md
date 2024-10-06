# Job Application Tracker

**A Python-based tool to automate job application emails and log recruiter details for tracking purposes.**

## Overview

This tool helps job seekers automate the process of sending job application emails to recruiters and keeps track of important details like recruiter names, email addresses, and the dates emails were sent. All tracking data is saved in an Excel file, providing a simple and organized way to manage your job search efforts.

## Features

- **Automated Email Sending**: Send personalized job application emails to multiple recruiters at once.
- **Recruiter Tracking**: Log recruiter names, emails, and the dates on which emails were sent in an Excel file.
- **Bulk Email Support**: Send emails to multiple recruiters at the same time.
- **Simple Setup**: Easy to configure with minimal dependencies.

## Requirements

- Python 3.x
- Required Python libraries:
  - `smtplib` (for sending emails)
  - `openpyxl` (for working with Excel files)
  - `email.mime` (for constructing emails)
  - `datetime` (for logging dates)

Install the required packages:
```bash
pip install openpyxl
# 1. Usage
git clone https://github.com/hacker6171/job-application-tracker.git
cd job-application-tracker

# 2. Configure Email Credentials:
- Open the send_emails function and replace the placeholder email (your_email@example.com) and password with your own email credentials.
- Set up your SMTP server information (e.g., smtp.example.com).

# 3. Prepare the Recruiter List:
- Add recruiter details (name and email) to the recruiters list in the script.

# 4. Run the Script:
python application_tracker.py
- The script will send emails to the listed recruiters and log the details into the application_tracking.xlsx file.



