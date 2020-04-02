dic = {
    "cardboard": 403,
    "glass": 501,
    "metal": 410,
    "paper": 594,
    "plastic": 482,
    "trash": 137
}

with open("../../data.csv", "a") as f:
    for k in dic:
        for i in range(1, dic[k] + 1):
            f.write("gs://recycler-7dc49-vcm/dataset-resized/{}/{}{}.jpg,{}\n".format(k, k, i, k))
