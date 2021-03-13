import csv
import time

def eclat(prefix, items):
        while items:
            i,itids = items.pop()
            isupp = len(itids)
            if isupp >= minsup:
              total = prefix+[i]
              countp = 0
              countv = 0
              doubles = set()
              for m in total:
                if m[1] == 'cart' or m[1] == 'remove_from_cart':
                  index = total.index(m)
                  total[index] = (m[0], m[1])

                elif m[1] == 'purchase':
                  countp = countp + 1
                  doubles.add(m[0])
                  if countp == 1:
                    index = total.index(m)
                    total[index] = m[2]
                  else: 
                    index = total.index(m)
                    total[index] = (m[0], m[1])

              for m in total:
                if len(m) == 3:
                  if m[1] == 'view':
                    if m[0] not in doubles:
                      countv = countv + 1
                  index = total.index(m)
                  total[index] = (m[0], m[1])

              if countp >= 2:
                if countv >= 1:
                  print(total, ':', isupp)  # Output all frequent pairs
              suffix = [] 
              for j, ojtids in items:
                  jtids = itids & ojtids
                  if len(jtids) >= minsup:
                      suffix.append((j,jtids))
              eclat(prefix+[i], sorted(suffix, key=lambda item: len(item[1]), reverse=True))

if __name__ == '__main__':
    #initialize parameters
    data = {}
    minsup   = 40
    trans = 0
    filename = '2019-Dec.csv'
    #start time for program
    timestart = time.time()
    item_def = 2  # column ITEM ID
    transaction_def = 7  # TRANSACTION = USER ID
    
    f = open('2019-Dec.csv', mode='r')
    for row in f:
        trans = row.split(',')[transaction_def]  
        item = (row.split(',')[item_def], row.split(',')[1], row.split(',')[3]) # (itemID, type of transaction, category of item)

        if item not in data:
            data[item] = set()
        data[item].add(trans)   # add does not add an element to the set key if it is already in the set
        #print(data[item]) 

    f.close()
    eclat([], sorted(data.items(), key=lambda item: len(item[1]), reverse=True))
    timestop = time.time()
    duration = timestop - timestart
    print(duration)
