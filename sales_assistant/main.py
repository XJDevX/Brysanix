#<<---Creating the Main IA-Assistant--->>#
import pandas as pd
import prod_revenue

def convert_data(csv):
    pd.read_csv(csv)

def run():
    convert_data("data/prod_data.csv")
    prod_revenue.revenue()

if __name__ == "__main__":
    run()