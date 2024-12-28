#<<---Creating the Main IA-Assistant--->>#
import pandas as pd
import os
import prod_revenue

def convert_data(csv):
    if os.path.exists(csv):
        return pd.read_csv(csv)
    else:
        print(f"Error: The file {csv} does not exist")
        return None

def run():
    data = convert_data('./data/prod_data.csv')
    print(f"Data: \n{data}")
    # prod_revenue.revenue()

if __name__ == "__main__":
    run()