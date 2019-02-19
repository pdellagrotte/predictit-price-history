import datetime
import ctypes
from utilities import database_utilities
from get_pi_data import get_data


def main(append=True):  # append records or drop tables, re-create tables, and load records
    table_parameters_dict = {"price_history": "30d", "price_hourly": "24h"}
    if not append:
        database_utilities.create_database()  # Creates the database
        database_utilities.drop_tables()
    for table_name in table_parameters_dict:
        market_list = get_data.get_list_of_markets()
        for market in market_list:
            data = get_data.get_json_data(get_data.build_url(str(market), table_parameters_dict[table_name],
                                                             max_contracts="6", show_hidden="true"))
            # print(data)
            i = 0  # count records inserted
            for d in data:
                i += 1
                print("Writing " + str(market) + " to database ...")
                if database_utilities.count_records_in_database(
                        table_name,
                        str(d['marketId']),
                        str(d['contractId']),
                        "'" + str(d['date']) + "'")[0][0] == 0:  # add 'r' to string so it is treated as a raw string
                    db_row = [str(datetime.datetime.now()), d['marketId'], d['contractId'], d['contractName'],
                              d['date'], d['dateString'], d['openSharePrice'], d['highSharePrice'],
                              d['lowSharePrice'], d['closeSharePrice'], d['tradeVolume']]
                    database_utilities.insert_into_database(db_row, table_name=table_name)
    print(str(i) + " records saved to database")


if __name__ == "__main__":
    main()
    print("End of program")
    ctypes.windll.user32.MessageBoxW(0, "Prices saved to database", "PredictIt Data", 1)
