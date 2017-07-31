import os
import csv
import datetime
from datetime import date,timedelta
from pandas_datareader import data

def header(message):
    print ("\n")
    print (message)
    print ("\n")

def symbol_input(symbol_list):
    while True:
        symbols = input ("Please enter the stock symbol you'd like to look up, one at a time. If you are finished listing symbols, type 'DONE': ")
        symbols = symbols.upper()
        if symbols == "DONE":
            break
        else:
            symbol_list.append(str(symbols))
        header("Here is a list of the stocks you picked: " + str(symbol_list))

def source_input():
    while True:
        data_source = input ("Please input the data source you'd like to use - enter either Google or Yahoo: ")
        data_source = data_source.title()
        if data_source == "Google":
            data_source = 'google'
        elif data_source == "Yahoo":
            data_source = 'yahoo'
        else:
            print ("Unrecognized Answer. Please try again. ")
        return data_source

def date_input():
    while True:
        date_type = input ("Do you have a specific date range you'd like to see? Enter Y or N: ")
        date_type = date_type.title()
        if date_type == "Y":
            start_input_year = input ("What is the beginning of the range you'd like to see? Enter the year in YYYY format. ")
            start_input_month = input ("What is the beginning of the range you'd like to see? Enter the month in the MM format. ")
            start_input_day = input ("What is the beginning of the range you'd like to see? Enter the day in the DD format. ")
            end_input_year = input ("What is the end of the range you'd like to see? Enter the year in the YYYY format. ")
            end_input_month = input ("What is the end of the range you'd like to see? Enter the month in the MM format. ")
            end_input_day = input ("What is the end of the range you'd like to see? Enter the day in the DD format. ")

            start = datetime.datetime(int(start_input_year), int(start_input_month), int(start_input_day))
            end = datetime.datetime(int(end_input_year), int(end_input_month), int(end_input_day))

        elif date_type == "N":
            days_back = input ("How many days of history would you like to see? ")
            days_back = int(days_back)

            start = str(date.today() - timedelta(days=days_back))
            end = str(date.today())

        else:
            "Error. Response not recognized. Please try again. "
        return start, end

def info_input(response):
    while True:
        info_type = input ("Please select the information you'd like to see - enter one of the following: Close Price, Open Price, Volume: ")
        info_type = info_type.lower()
        if info_type == "close price":
            app_output = response.ix["Close"]
        elif info_type == "open price":
            app_output = response.ix["Open"]
        elif info_type == "volume":
            app_output = response.ix["Volume"]
        else:
            "Error. Response not recognized. Please try again."
        return app_output

# -----------------------Application--------------------------------------
def run():
    header("Hey " + os.getlogin() + "!")
    header("Welcome to the Stock Price Finder!")

    symbol_list = []

    symbol_input(symbol_list)
    start,end = date_input()
    data_source = source_input()

    response = data.DataReader(symbol_list, data_source, start, end)

    app_output = info_input(response)

    csv_file_path = "data/stock_price_output.csv"

    app_output.to_csv(csv_file_path)

    print (str(app_output))

if __name__ == "__main__":
    run()
