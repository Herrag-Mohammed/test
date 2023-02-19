#import modules
import rpa as r
import pandas as pd
import streamlit as st
from pathlib import Path
from PIL import Image
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
file = current_dir / "../challenge.xlsx"
#read the excel file and store in dataframe variable df
def run():
    if st.button('Run >'):
        df = pd.read_excel('./challenge.xlsx',sheet_name='Sheet1')
       

        #start the tagUI process
        r.init()

        #open the website
        r.url('http://www.rpachallenge.com/')
        r.wait(10)
        #click on start button
        r.click('//button[text()="Start"]')

        #data entry operations
        for index,row in df.iterrows():
            r.type('//input[@ng-reflect-name="labelFirstName"]',row['First Name'])
            r.type('//input[@ng-reflect-name="labelLastName"]',row['Last Name '])
            r.type('//input[@ng-reflect-name="labelCompanyName"]',row['Company Name'])
            r.type('//input[@ng-reflect-name="labelRole"]',row['Role in Company'])
            r.type('//input[@ng-reflect-name="labelAddress"]',row['Address'])
            r.type('//input[@ng-reflect-name="labelEmail"]',row['Email'])
            r.type('//input[@ng-reflect-name="labelPhone"]',str(row['Phone Number']))
            r.click('//input[@value="Submit"]')

        #screenshot of webpage

        r.snap('/html/body/app-root/div[2]','results.png')
        

        image = Image.open('results.png')

        st.image(image, caption='Sunrise by the mountains')

        #stop the tagui process
        r.close()
if __name__ == '__main__':
    run()