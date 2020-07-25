import pandas as pd
import math
import xlwt
book = xlwt.Workbook()
sheet1 = book.add_sheet('Sheet1')
df = pd.read_excel("normal1.xls", sheet_name=0)

def createList(r1, r2):
    return list(range(r1, r2))
r1, r2 = 1,68
mylist1=createList(r1, r2)

k=0
col=0
for i in mylist1:
    print(col)
    header1 = 'NX{}'.format(i)
    header2 = 'NY{}'.format(i)
    list1 = list(df[header1])
    list2 = list(df[header2])
    sheet1.write(0, i-1, "Normal")
    name = "normalDistance1.xls"
    book.save(name)

    def createList(r1, r2):
        return list(range(r1, r2))


    def createList1(r3, r4):
        return list(range(r3, r4))


    r1, r2 = 0, 68
    mylist1 = createList(r1, r2)
    r3, r4 = 0, 66
    mylist2 = createList1(r3, r4)
    k = 1

    for i in mylist1:
        for j in mylist2:
            if j >= i:

                distance = math.sqrt(((list1[j + 1] - list1[i]) ** 2) + ((list2[j + 1] - list2[i]) ** 2))
                sheet1.write(k,col, distance)
                k = k + 1
    col=col+1
    name = "normalDistance1.xls"
    book.save(name)

print('End')