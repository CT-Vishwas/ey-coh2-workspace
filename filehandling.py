import  csv
import os
import datetime

FILE_PATH = r"C:\Users\VishwasKSingh\Workspace\ey-coh2-workspace\data\house_prices_india.csv" 
if not os.path.exists(FILE_PATH):
    print("File you are trying to read does not exist.")

fname = os.path.basename(FILE_PATH)
print(fname)

with open(FILE_PATH, "rt") as fh:
    data = csv.DictReader(fh)
    print(data.fieldnames)

    # Average price in data
    count = 0
    total = 0
    for row in data:
        total += float(row['Price'])
        count += 1
    
    avg = total/count
    print(f"Average price of all the houses is {avg: .4f}")

current_datetime = datetime.datetime.now().strftime('%a %d %b %Y, %I:%M%p')
with open("summary.log", "a+") as fw:
    fw.writelines(f"Summary of '{fname}' at {current_datetime} \n")
    fw.writelines("-"*20+"\n")
    fw.writelines(f"Number of Records: {count}\n")
    fw.writelines(f"Average price of Houses: {avg: .4f}\n")
    fw.writelines("*"*20+"\n")
