import csv
import time

def eclat(prefix, items):
        while items:
            i,itids = items.pop()
            isupp = len(itids)
            if isupp >= minsup:
              print(sorted(prefix+[i]), ':', isupp)  # Output all frequent pairs
              suffix = [] 
              for j, ojtids in items:
                  jtids = itids & ojtids
                  if len(jtids) >= minsup:
                      suffix.append((j,jtids))
              eclat(prefix+[i], sorted(suffix, key=lambda item: len(item[1]), reverse=True))

if __name__ == '__main__':
    #initialize parameters
    data = {}
    minsup   = 130
    trans = 0
    filename = '2019-Dec.csv'
    #start time for program
    timestart = time.time()
    item_def = row.split(',')[2]
    transaction_def = row.split(',')[7]


    f = open('2019-Dec.csv', mode='r')
    for row in f:
        trans = transaction_def  # User ID
        item =  item_def   # 3th column is the one with the itemID
        if item not in data:
            data[item] = set()
        data[item].add(trans)   # add does not add an element to the set if it is already in the set
    f.close()
    eclat([], sorted(data.items(), key=lambda item: len(item[1]), reverse=True))
    timestop = time.time()
    duration = timestop - timestart
    print(duration)
