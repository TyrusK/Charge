import codecs
import csv
import time
import sys
from datetime import date
from charge import charge

dd = csv.list_dialects()

if len(sys.argv) < 3 :
    print("Usage: amazon.py <mint-file-name>")
    exit(1)
print("sys.argv=",sys.argv)

mint_count = 0
mint_t_list = []
mint_file_name = sys.argv[1]
def create_mint_list(file_name) :
    global mint_count
    global mint_t_list
    with codecs.open(file_name,"r","utf-8") as mint_transactions:
        reader = csv.reader(mint_transactions,dialect=csv.get_dialect('excel'))
        for row in reader:
            if len(row) > 8 and mint_count > 0 and row[1] == "Amazon" :
                mint_cost = row[3]
                mint_date = time.strptime(row[0],"%m/%d/%Y")
                dcpair = charge(mint_date,mint_cost)
                mint_t_list.append(dcpair)
            mint_count += 1
create_mint_list(mint_file_name)

amazon_t_list = []
def create_amazon_list(file_name) :
    with codecs.open(file_name,"r","utf-8") as amazon_transactions:
        amazon_count = 0
        global amazon_t_list
        reader = csv.reader(amazon_transactions)
        print(amazon_count)
        for row in reader:
            if amazon_count > 0 :
                amazon_cost = row[29].lstrip("$")
                amazon_date = time.strptime(row[0],"%x")
                dcpair = charge(amazon_date,amazon_cost)
                amazon_t_list.append(dcpair)
            amazon_count += 1
for n in range(2,len(sys.argv)) :
    create_amazon_list(sys.argv[n])

def print_charge(a_charge_list,m_charge) :
    if len(a_charge_list) == 1 :
        print("An Amazon transaction on ",a_charge_list[0].date," ($",a_charge_list[0].cost,")"," corresponds to a Mint charge on ",m_charge.date," ($",m_charge.cost,").",sep="")
    elif len(a_charge_list) == 2 :
        print("Amazon transactions on ",a_charge_list[0].date," ($",a_charge_list[0].cost,") and ",a_charge_list[1].date," ($",a_charge_list[1].cost,")"," correspond to a Mint charge on ",m_charge.date," ($",m_charge.cost,").",sep="")
    else :
        print("Amazon transactions on ",end="")
        for n in range(len(a_charge_list) - 1) :
            a = a_charge_list[n]
            print(a.date," ($",a.cost,"), ",sep="",end="")
            if n == len(a_charge_list) - 1 :
                print("and ",a.date," ($",a.cost,"), ",sep="",end="")
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
