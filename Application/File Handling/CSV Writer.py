import csv

with open("Data_2.csv","w") as f:
    csv_writer=csv.writer(f)
    data=("2023","Area 51","3000")
    csv_writer.writerow(data)

