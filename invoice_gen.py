#!/usr/bin/python3
import os
import shutil
import sqlite3
from datetime import datetime, date, timedelta
from InvoiceGenerator.pdf import SimpleInvoice
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator

#English until I work out how to make it selectable
os.environ["INVOICE_LANG"] = "en"

# create a database for connection info and tracking earnings
conn = sqlite3.connect('program_data.db')

# defaults will be global variables
DEFAULT_DUE_DATE = 2.0


def gen_date_data(weeks_due=DEFAULT_DUE_DATE):
    today = date.today()
    due_date = today + timedelta(weeks=float(weeks_due))

    today = date.strftime(today, "%d/%m/%Y")
    due_date = date.strftime(due_date, "%d/%m/%Y")

    print(f"{today} is the date today, {weeks_due:.0f} week(s) from now the due date is {due_date}")


def initialise():
    """
    summary - address header line - name of addressee or company name
    address - line of the address with street and house number
    city - city or part of the city
    zip_code - zip code (PSČ in Czech)
    phone -
    email -
    bank_name -
    bank_account - bank account number
    bank_code -
    note - note that will be written on the invoice
    vat_id - value added tax identification number (DIČ in czech)
    abn - sole trader business number
    logo_filename - path to the image of logo of the contractor
    """
    user_data = {
        "name":"",
        "b_address":"",
        "abn":"",
        "h_phone":"",
        "m_phone":"",
        "email":""
    }



def main():
    # create invoice from user input
    gen_date_data()

if __name__ == '__main__':
    main()