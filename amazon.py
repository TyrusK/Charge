import codecs
import csv
import time
from datetime import date
from charge import charge

dd = csv.list_dialects()

mint_count = 0
mint_t_list = []
with codecs.open("/Users/tyrus/Desktop/foo.csv","r","utf-8") as mint_transactions:
    reader = csv.reader(mint_transactions,dialect=csv.get_dialect('excel'))
    for row in reader:
        if len(row) > 8 and mint_count > 0 and row[1] == "Amazon" :
            mint_cost = row[3]
            mint_date = time.strptime(row[0],"%m/%d/%Y")
            dcpair = charge(mint_date,mint_cost)
            mint_t_list.append(dcpair)
        mint_count += 1

amazon_count = 0
amazon_t_list = []
with codecs.open("/Users/tyrus/Desktop/amazon_transactions.csv","r","utf-8") as amazon_transactions:
    reader = csv.reader(amazon_transactions)
    for row in reader:
        if amazon_count > 0 :
            amazon_cost = row[29].lstrip("$")
            amazon_date = time.strptime(row[0],"%x")
            dcpair = charge(amazon_date,amazon_cost)
            amazon_t_list.append(dcpair)
        amazon_count += 1

def print_charge(a_charge_list,m_charge) :
    if len(a_charge_list) == 1 :
        print("An Amazon transaction on ",a_charge_list[0].date," ($",a_charge_list[0].cost,"),"," corresponds to a Mint charge on ",m_charge.date," ($",m_charge.cost,").",sep="")
    elif len(a_charge_list) == 2 :
        print("Amazon transactions on ",a_charge_list[0].date," ($",a_charge_list[0].cost,") and ",a_charge_list[1].date," ($",a_charge_list[1].cost,")"," correspond to a Mint charge on ",m_charge.date," ($",m_charge.cost,").",sep="")
    else :
        print("Amazon transactions on ")
        for n in range(len(a_charge_list) - 1) :
            a = a_charge_list[n]
            print(a.date," ($",a[0].cost,"), ",sep="",end="")
            if n == len(a_charge_list) - 1 :
                print("and ",a.date," ($",a[0].cost,"), ",sep="",end="")
        print("correspond to a Mint charge on ",mls.date," ($",mls.cost,").",sep="")

for mls in mint_t_list :
    a = mls.loop_check1(amazon_t_list)
    if len(a) > 0 :
        
        print_charge(a,mls)
    else :
        a = mls.loop_check2(amazon_t_list)
        if len(a) > 0 :
             print_charge(a,mls)
        else :
            a = mls.loop_check3(amazon_t_list)
            if len(a) > 0 :
                 print_charge(a,mls)
            else :
                print("I could not find any matches for the Mint charge on ",mls.date," ($",mls.cost,").",sep="")

##a_writer = open("a_list","w")
##m_writer = open("m_list","w")
##a_writer.close()
##m_writer.close()
