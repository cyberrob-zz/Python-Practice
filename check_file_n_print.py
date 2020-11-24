import time
import os
import pandas

file_path = "files/temps_today.csv"#"files/fruit.txt"

while True:
    if os.path.exists(file_path):
        #with open(file_path) as file:
        #    print(file.read())
        data = pandas.read_csv(file_path)
        print(data.mean()['st1'])
    else:
        print(f"File {file_path} not found")
    time.sleep(10)
