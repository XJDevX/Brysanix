#<<---Data Generator for ML Training--->>#
import pandas as pd
from datetime import datetime, timedelta
import random

def generate_products(prod_num):
    category = ['Electronics', 'Clothing', 'Books', 'Toys', 'Home']
    prod_list = {}
    for prod in range(0, prod_num):
        start_date = datetime.today() - timedelta(days=365)
        random_date = start_date + timedelta(days=random.randint(0, 365))
        format_date = random_date.strftime('%d/%m/%y')

        trend_factor = random.uniform(0.8, 1.2)
        if random_date.month in [11, 12]:
            trend_factor *= 1.5

        prod_list[f"Product #{prod+1}"] = {
            "Sold": int(round(random.randint(5, 25) * trend_factor)), 
            "Score": random.randint(1, 5), 
            "Price": round(random.gauss(15, 5)),
            "Category": random.choice(category),
            "Start Date": format_date}
    return prod_list

n_prod = 100
print(f"Number of products: {n_prod}")
products_info = generate_products(n_prod)
data = pd.DataFrame.from_dict(products_info)
print(data)