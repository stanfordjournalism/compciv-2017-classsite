import json
import requests

SRC_URL = 'http://stash.compciv.org/2017/helloworld.json'

def foo_1():
    """
    in helloworld.json
    return the value of the 'status' key/attribute

    expected:
    'SUPER!'
    """
    resp = requests.get(CSV_URL)
    txt = resp.text
    jdata = json.loads(txt)
    return jdata['status']


def foo_2():
    """
    in helloworld.json
    return the number of items in the 'inventory'

    expected:
    5
    """
    jdata = json.loads(requests.get(CSV_URL).text)
    inventory = jdata['inventory']
    return(len(inventory))



def foo_3():
    """
    in helloworld.json
    return an alphabetized list of 'inventory' item names

    expected:
    ['apples', 'cats', 'dogs', 'kiwis', 'zebras']
    """
    inventory = json.loads(requests.get(CSV_URL).text)['inventory']
    nameslist = []
    for item in inventory:
        itemname = item['name']
        nameslist.append(itemname)
    sortednames = sorted(nameslist)
    return sortednames



def foo_4():
    """
    in helloworld.json
    return the sum of inventory counts

    expected:
    607
    """
    thesum = 0
    for item in json.loads(requests.get(CSV_URL).text)['inventory']:
        c = item['count']
        thesum += c
    return thesum


def foo_5():
    """
    from helloworld.json
    filter inventory for just animals
    return a list of lists, with each sublist containing animal name and count (as integer)
        and sorted in descending order of count

    expected:
    [['zebras', 180], ['dogs', 42], ['cats', 9]]

    """

    def sorter(thing):
        return thing[1]


    thelist = []
    for item in json.loads(requests.get(CSV_URL).text)['inventory']:
        if item['type'] == 'animal':
            n = item['name']
            c = item['count']
            thelist.append([n, c])

    return sorted(thelist, key=sorter, reverse=True)



def foo_6():
    """
    from helloworld.json
    filter inventory for just fruits
    return a list of dicts, with each sublist containing fruit name and count (as integer)
        and sorted in ascending order of count


     [{'count': 76, 'name': 'kiwis'}, {'count': 300, 'name': 'apples'}]
    """
    def sorter(thing):
        return thing['count']

    thelist = []
    for item in json.loads(requests.get(CSV_URL).text)['inventory']:
        if item['type'] == 'fruit':
            d = {}
            d['name'] = item['name']
            d['count'] = item['count']
            thelist.append(d)

    return sorted(thelist, key=sorter, reverse=False)



def foo_7():
    """
    from helloworld.json
    do a group count of the 'inventory' by 'type', and get a count how many unique items there are by name
    return a dictionary with each key-value pair consisting of the 'type' and count of unique item names

    {'animal': 3, 'fruit': 2}
    """
    thedict = {}
    inventory = json.loads(requests.get(CSV_URL).text)['inventory']
    for item in inventory:
        itype = item['type']
        if thedict.get(itype):
            thedict[itype] += 1
        else:
            thedict[itype] = 1
    return thedict



def foo_8():
    """
    from helloworld.json
    do a group count of the 'inventory' by 'type', summing up the counts of each item for every given type
    return a dictionary with each key-value pair consisting of the 'type' and sum of item counts

    expected:
    {'animal': 231, 'fruit': 376}

    """
    thedict = {}
    inventory = json.loads(requests.get(CSV_URL).text)['inventory']
    for item in inventory:
        itype = item['type']
        if thedict.get(itype):
            thedict[itype] += item['count']
        else:
            thedict[itype] = item['count']
    return thedict
