from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

josaa = 'https://josaa.admissions.nic.in/Applicant/seatallotmentresult/currentorcr.aspx'

params = {
    "ctl00$ContentPlaceHolder1$ddlInstype":"ALL",
    "ctl00$ContentPlaceHolder1$ddlInstitute":"ALL",
    "ctl00$ContentPlaceHolder1$ddlBranch":"ALL",
    "ctl00$ContentPlaceHolder1$ddlSeattype":"ALL",
    "ctl00$ContentPlaceHolder1$btnSubmit":"Submit"
}

#years = ["2022","2021","2020","2019","2018","2017","2016"]
rounds = ["1","2","3","4","5","6"]

def josaa_data(round):
    with requests.Session() as req:
        site_data = req.get(josaa)
        data = {}
       # data.update({tag['name']:tag['value'] for tag in BeautifulSoup(site_data.content,'lxml').select('input[name^=__]')})
       # data["ctl00$ContentPlaceHolder1$ddlYear"] = year
       # site_data = req.post(josaa,data=data)
        
        data.update({tag['name']:tag['value'] for tag in BeautifulSoup(site_data.content,'lxml').select('input[name^=__]')})
        data["ctl00$ContentPlaceHolder1$ddlroundno"] = round
        site_data = req.post(josaa,data=data)
        
        for key,value in params.items():
            data.update({tag['name']:tag['value'] for tag in BeautifulSoup(site_data.content,'lxml').select('input[name^=__]')})
            data[key] = value
            site_data = req.post(josaa,data=data)
            
            
    ranks = BeautifulSoup(site_data.text,'lxml')
    table = ranks.find(id="ctl00_ContentPlaceHolder1_GridView1")
    
    df = pd.read_html(table.prettify())[0]
    df.dropna(inplace = True,how = "all")
    #df["Year"] = '2023'
    df["Round"] = round
    df["Opening Rank"] = pd.to_numeric(df["Opening Rank"], errors='coerce')
    df["Closing Rank"] = pd.to_numeric(df["Closing Rank"], errors='coerce')
    df.dropna(subset=["Opening Rank", "Closing Rank"], inplace=True)
    df["Opening Rank"] = df["Opening Rank"].astype(int)
    df["Closing Rank"] = df["Closing Rank"].astype(int)
    
    return df

#for year in years:
for round in rounds:
    final_data = josaa_data(round)
    file_name = f"2023-{round}.csv"
    print(f"Saving data for 2023 , round {round} to {file_name}")
    final_data.to_csv(file_name,index = False)
        

print(f"Done")
        
        
        
    
            
    