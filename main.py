from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# cmd-shift-p to reload vscode window
from pretty_html_table import build_table
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import yaml
import os
from dotenv import load_dotenv
import pandas as pd
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
from driver import Driver

# import yaml file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# loading .env file
load_dotenv()


def make_email(body):
    msg = MIMEMultipart()

    from_email = os.environ['FROM_EMAIL']
    to_email = os.environ['TO_EMAIL']

    msg['Subject'] = 'Your Weekly Job Report'
    msg['From'] = from_email
    msg['To'] = to_email

    body_content = body
    msg.attach(MIMEText(body_content, "html"))
    msg_body = msg.as_string()

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    password = os.environ['GOOGLE_EMAIL_APP_PASSOWRD']
    s.login(from_email, password)
    s.sendmail(from_email, to_email, msg_body)
    s.quit()


def format_data(matching_jobs: list):
    data = pd.DataFrame(matching_jobs, columns=[
                        "Job Title", 'Company Name', 'Link'])
    return data


if __name__ == "__main__":
    matching_jobs = list()
    for company in config['companies']:
        driver = Driver(company['keywords'], company['name'],
                        company['url'], company['job-posting-tag'], company['job-board-type'])
        driver.open_chrome()
        driver.load_page()

        if company['job-board-type'] == 'lever':
            matching_jobs.extend(driver.handle_lever())
        elif company['job-board-type'] == 'greenhouse':
            matching_jobs.extend(driver.handle_greenhouse())
        elif company['job-board-type'] == 'custom':
            matching_jobs.extend(driver.handle_url_mutation())

    # print(matching_jobs)
    driver.quit()

    data = format_data(matching_jobs)
    output = build_table(data, 'grey_dark')
    make_email(output)
