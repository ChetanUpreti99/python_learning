import pandas as pd
from pathlib import Path

class DataExtraction:
    def __init__(self, file_path:Path):
        self.file_path = file_path

    def fetch_text(self,separator:str):
        df = pd.read_csv(self.file_path, sep=separator)
        print(df.head())

    def fetch_json(self):
        df = pd.read_json(self.file_path)
        print(df)

    def fetch_parquet(self):
        df = pd.read_parquet(self.file_path)   
        print(df.head())

BASE_DIR = Path(__file__).resolve().parent
obj = DataExtraction(BASE_DIR/"files"/"orders.tsv")
obj.fetch_text("\t")

        

