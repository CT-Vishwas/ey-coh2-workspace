import os

FILE_PATH = r"C:\Users\VishwasKSingh\Workspace\ey-coh2-workspace\data\house_prices_india.csv"

# Check if the path exists
# if not os.path.exists(FILE_PATH):
#     print("The File does not exist")

# fh = open(FILE_PATH)
# data = fh.readlines()
# for line in data:
#     print(line, end="")
# # print(data)

# fh.close()

## Reading using context manager
try:
    with open(FILE_PATH, "rt") as fh:
        data = fh.readlines()
        for line in data:
            print(line,end="")
except FileNotFoundError:
    print("File Does not exist")

