#Import packages and set the working directory
import os
import glob
import pandas as pd

# Define csv folder path
path = 'All_prefectures_xlsx' #os.path.join('Test_csv','Aichi.csv')

#Use glob to match the pattern ‘csv’
extension = 'xlsx'
all_filenames = [i for i in glob.glob(os.path.join(path,'*.{}'.format(extension)))]

#df = pd.read_excel(all_filenames[0])
#print(df.head())


#Combine all files in the list and export as CSV
#combine all files in the list
combined_xlsx = pd.concat([pd.read_excel(f) for f in all_filenames ])
combined_xlsx['Date'] = pd.to_datetime(combined_xlsx['Date'],format='%Y%m%d')
combined_xlsx['Date'] = combined_xlsx['Date'].dt.strftime('%Y-%m-%d')
#export to csv
combined_xlsx.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

print("I'm done with this shit")
