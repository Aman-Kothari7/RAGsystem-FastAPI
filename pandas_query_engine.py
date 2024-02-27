#Necessary imports to create pandas query engine 
from llama_index.core.query_engine import PandasQueryEngine
import pandas as pd 

rbi_notifications_data = pd.read_csv("data/notifications_data_small.csv")
#Defining the PandasQueryEngine
rbi_notifications_query_engine = PandasQueryEngine(
    df=rbi_notifications_data, verbose=True,
)