import pandas as pd

data = open("nameListTxt.txt").readlines()
seat_num = []
name = []
mothers_name = []
prn = []


def reArrange():
    for info in range(4, len(data[4:]), 4):
        seat_num.append(data[info].strip("\n"))
        name.append(data[info + 1].strip("\n"))
        mothers_name.append(data[info + 2].strip("\n"))
        prn.append(data[info + 3].strip("\n"))

    df = pd.DataFrame({"Seat_num": seat_num, "Name": name, "Mothers_name": mothers_name, "PRN": prn})
    df.to_csv("nameListCsv.csv", index=False)


reArrange()
