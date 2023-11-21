import glob
import pandas as pd

file_list = glob.glob("*.csv")
print(file_list)

csv_list = []
for file in file_list:  
    csv_list.append(pd.read_csv(file))

csv_merged = pd.concat(csv_list, ignore_index=True)
csv_merged.to_csv("clients_data_report.csv", index=False)