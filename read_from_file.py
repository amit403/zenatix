import csv
data_list = []
def read():
    with open("dataset.csv","r") as myfile:
        data = csv.DictReader(myfile)
        for row in data:
            data_list.append(row)
    return(data_list)