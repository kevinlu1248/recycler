import os

dic = {
    "cardboard": 403,
    "glass": 501,
    "metal": 410,
    "paper": 594,
    "foods": 0,
    "plastic": 482,
    "trash": 137
}

for classification in dic:
    index = dic[classification] + 1
    with os.scandir(classification) as entries:
        for entry in entries:
            os.rename(classification + "/" + entry.name, classification + "/{}{}.jpg".format(classification, index))
            index += 1