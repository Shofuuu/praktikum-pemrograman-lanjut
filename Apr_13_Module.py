#!/usr/bin/python3

def mean(data_list):
    data = 0
    for x in data_list: data += x
    return data/len(data_list)

def median(data_list):
    data = sorted(data_list)
    if len(data) % 2 == 0:
        return (data[len(data)//2] + data[len(data)//2 - 1])/2
    else:
        return data[len(data)//2]

def mode(data_list):
    data = sorted(data_list)
    mode_list = []
    mode_count = 0
    for x in data:
        if data.count(x) > mode_count:
            mode_count = data.count(x)
            mode_list = [x]
        elif data.count(x) == mode_count:
            mode_list.append(x)
    return mode_list