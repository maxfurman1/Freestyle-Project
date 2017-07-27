def run():
    import os
    import csv
    import datetime
    from pandas_datareader import data

    print ("\n")
    print ("Hey " + os.getlogin() + "!")
    print ("\n")
    print ("Welcome to the Stock Price Downloading Application!")
    print ("\n")

    symbol_list = []

#    symbols = input ("Please enter the stock symbol you'd like to look up, one at a time. If you are finished listing symbols, type 'DONE'")
    while True:
        symbols = input ("Please enter the stock symbol you'd like to look up, one at a time. If you are finished listing symbols, type 'DONE':")
        symbols = symbols.upper()
        if symbols == "DONE":
            break
        else:
            symbol_list.append(str(symbols))
    print (symbol_list)

    data_source = input ("Please input the data source you'd like to use - enter either Google or Yahoo:")
    data_source = data_source.title()

    if data_source == "Google":
        data_source = 'google'
    elif data_source == "Yahoo":
        data_source = 'yahoo'
    else:
        print ("Unrecognized Answer. Please try again.")

    date_type = input ("Do you have a specific date range you'd like to see? Enter Y or N:")
    date_type = date_type.title()
    if date_type == "Y":
        start_input_year = input ("What is the beginning of the range you'd like to see? Enter the year in YYYY format.")
        start_input_month = input ("What is the beginning of the range you'd like to see? Enter the month in the MM format.")
        start_input_day = input ("What is the beginning of the range you'd like to see? Enter the day in the DD format.")
        end_input_year = input ("What is the end of the range you'd like to see? Enter the year in the YYYY format.")
        end_input_month = input ("What is the end of the range you'd like to see? Enter the month in the MM format.")
        end_input_day = input ("What is the end of the range you'd like to see? Enter the day in the DD format.")

        start = datetime.datetime(int(start_input_year), int(start_input_month), int(start_input_day))
        end = datetime.datetime(int(end_input_year), int(end_input_month), int(end_input_day))

    elif date_type == "N":
        days_back = input ("How many days of history would you like to see?")
        days_back = int(days_back)

        start = str(date.today() - timedelta(days=days_back))#.format(days_back) #> '2017-07-09'
        end = str(date.today()) #> '2017-07-24'
    else:
        "Error. Response not recognized. Please try again."

    response = data.DataReader(symbol_list, data_source, start, end)

# PARSE RESPONSE
    
    daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function

    #stock_prices = []
    csv_file_path = "data/stock_price_output.csv"
    daily_closing_prices.to_csv(csv_file_path)
    #with open(csv_file_path, "w") as csv_file:
    #        writer = csv.DictWriter(csv_file, fieldnames=["date","open","high","low","close","volume"])
    #        writer.writeheader()
    #        for stock_price in stock_prices:
    #            writer.writerow(stock_price)

    print (str(daily_closing_prices))

if __name__ == "__main__":
    run ()
