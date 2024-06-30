import os
import pandas as pd
import numpy as np
from analysis.models import Data

def load_data():
    directory_name = 'scraped_data/'
    
    for file in os.listdir(directory_name):
        if file.endswith('.csv'):
            file_path = os.path.join(directory_name, file)
            df = pd.read_csv(file_path)
            df.drop(columns='Gender',inplace = True)
             
            for _, row in df.iterrows():
                Data.objects.create(
                    Institue = row['Institute'],
                    Branch = row['Academic Program Name'],
                    Quota = row['Quota'],
                    Seat_Type = row['Seat Type'],
                    Opening_Rank = row['Opening Rank'],
                    Closing_Rank = row['Closing Rank'],
                    Year = row['Year'],
                    Round = row['Round']
                )
                
            print(f"Data loaded from {file} successfully")
            
if __name__ == "__main__":
    
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Josaa_project.settings')
    django.setup()

    load_data()            