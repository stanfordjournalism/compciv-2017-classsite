import csv
import requests

SRC_URL = 'http://stash.compciv.org/2017/helloworld.csv'

def foo_1():
    """
    in helloworld.csv
    return the 'status' value in the file's "metadata"

    expected:
    'SUPER!'

    """
    resp = requests.get(SRC_URL)
    txt = resp.text
    lines = txt.splitlines()
    # look through each line
    for line in lines:
        if 'status:' in line:
            keyvalpair = line.split(':')
            return keyvalpair[1]


def foo_2():
    """
    in helloworld.csv
    return the number of records

    expected:
    5
    """
    resp = requests.get(SRC_URL)
    lines = resp.text.splitlines()
    # headers are on line 4, i.e. index 3
    datalines = lines[3:]
    records = list(csv.DictReader(datalines))

    return len(records)



def foo_3():
    """
    in helloworld.csv
    return an alphabetized list of 'inventory' item names

    expected:
    ['apples', 'cats', 'dogs', 'kiwis', 'zebras']
    """
    resp = requests.get(SRC_URL)
    datalines = resp.text.splitlines()[3:]
    records = list(csv.DictReader(datalines))

    nameslist = []
    for item in records:
        itemname = item['name']
        nameslist.append(itemname)
    sortednames = sorted(nameslist)

    return sortednames



def foo_4():
    """
    in helloworld.csv
    return the sum of inventory counts

    expected:
    607
    """
    resp = requests.get(SRC_URL)
    datalines = resp.text.splitlines()[3:]
    records = list(csv.DictReader(datalines))

    thesum = 0
    for item in records:
        c = int(item['count'])
        thesum += c
    return thesum


def foo_5():
    """
    from helloworld.csv
    filter inventory for just animals
    return a list of lists, with each sublist containing animal name and count (as integer)
        and sorted in descending order of count

    expected:
    [['zebras', 180], ['dogs', 42], ['cats', 9]]

    """
    resp = requests.get(SRC_URL)
    records = list(csv.DictReader(resp.text.splitlines()[3:]))

    def sorter(thing):
        return thing[1]

    thelist = []
    for item in records:
        if item['type'] == 'animal':
            n = item['name']
            c = int(item['count'])
            thelist.append([n, c])

    return sorted(thelist, key=sorter, reverse=True)



def foo_6():
    """
    from helloworld.csv
    filter inventory for just fruits
    return a list of dicts, with each sublist containing fruit name and count (as integer)
        and sorted in ascending order of count

    expected:
    [{'count': 76, 'name': 'kiwis'}, {'count': 300, 'name': 'apples'}]
    """
    resp = requests.get(SRC_URL)
    records = list(csv.DictReader(resp.text.splitlines()[3:]))

    def sorter(thing):
        return thing['count']

    thelist = []
    for item in records:
        if item['type'] == 'fruit':
            d = {}
            d['name'] = item['name']
            d['count'] = int(item['count'])
            thelist.append(d)

    return sorted(thelist, key=sorter, reverse=False)



def foo_7():
    """
    from helloworld.csv
    do a group count of the 'inventory' by 'type', and get a count how many unique items there are by name
    return a dictionary with each key-value pair consisting of the 'type' and count of unique item names

    expected:
    {'animal': 3, 'fruit': 2}
    """
    resp = requests.get(SRC_URL)
    records = list(csv.DictReader(resp.text.splitlines()[3:]))

    thedict = {}
    for item in records:
        itype = item['type']
        if thedict.get(itype):
            thedict[itype] += 1
        else:
            thedict[itype] = 1
    return thedict



def foo_8():
    """
    from helloworld.csv
    do a group count of the 'inventory' by 'type', summing up the counts of each item for every given type
    return a dictionary with each key-value pair consisting of the 'type' and sum of item counts

    expected:
    {'animal': 231, 'fruit': 376}
    """
    resp = requests.get(SRC_URL)
    records = list(csv.DictReader(resp.text.splitlines()[3:]))

    thedict = {}
    for item in records:
        itype = item['type']
        if thedict.get(itype):
            thedict[itype] += int(item['count'])
        else:
            thedict[itype] = int(item['count'])
    return thedict
