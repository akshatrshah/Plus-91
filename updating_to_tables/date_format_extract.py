import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# # CONVERTTING ALL ROW DATES TO A DEFINED FORMAT
# input_date_formats = ['%m/%d/%Y', '%Y-%m-%d', '%d-%m-%Y', '%d-%b-%Y', '%d-%B-%Y', '%d-%b-%y', '%d-%B-%y',
#                       '%d-%B-%Y', '%d %B %Y', '%d-%b-%Y', '%d %b %Y', '%d %B %Y', '%dth %b %Y', '%dst %b %Y', '%dnd %b %Y', '%drd %b %Y']
# output_date_format = '%d-%m-%Y'

# # Open the input CSV file in read mode
# with open("input.csv", 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     rows = []

#     # Loop through each row in the input CSV file
#     for row in csvreader:
#         # Convert the date column to the desired format
#         date_str = row[1]  # Assumes that the date column is the first column
#         for input_date_format in input_date_formats:
#             try:
#                 date_obj = datetime.strptime(date_str, input_date_format)
#                 # Replace the original date column with the formatted date
#                 row[1] = date_obj.strftime(output_date_format)
#                 break
#             except ValueError:
#                 pass

#         rows.append(row)

# # Overwrite the input CSV file with the updated rows
# with open("input.csv", 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerows(rows)


def date_formatter(date_string):
    date_object = datetime.strptime(date_string, '%d-%b-%Y')
    new_date_string = date_object.strftime('%Y-%m-%d')
    return new_date_string
