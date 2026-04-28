import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent


def pandas_decorator(fx):
    def main_func(*args):
        response  = fx(*args)
        response.to_parquet(BASE_DIR/"files"/"temp.parquet")
        return response
    return main_func

@pandas_decorator
def csv_to_parquet(file_path:str):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df

response = csv_to_parquet(BASE_DIR/"files"/"orders.csv")
print(response.head())