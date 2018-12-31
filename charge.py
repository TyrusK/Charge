from datetime import date,timedelta
class charge :
    
    def __init__(self, cdate, cost) :
        self.date = date(cdate.tm_year,cdate.tm_mon,cdate.tm_mday)
        self.cost = float(cost)
        
    def date_comp(self,a_charge, target_diff) :
        return (self.date - a_charge.date) <= timedelta(target_diff,0,0) and (self.date - a_charge.date) >= timedelta(0,0,0)
            
    def sum_check(self,charge_list) :
        ls_pos = 0
        total = 0
        while (ls_pos < len(charge_list)) :
            total += charge_list[ls_pos].cost
            ls_pos += 1
        return total == self.cost
    
    def loop_check1(self,a_list) :
        for a in a_list :
            if self.date_comp(a,30) and self.sum_check([a]) :
                a_list.remove(a)
                return [a]
        return []

    def loop_check2(self,a_list) :
        n = len(a_list)
        for i in range(n) :
            a = a_list[i]
            if self.date_comp(a,30) :
                for j in range(i + 1,n) :
                    b = a_list[j]
                    if self.date_comp(b,30) and self.sum_check([a,b]) :
                        a_list.remove(a)
                        a_list.remove(b)
                        return [a,b]
        return []
        
    def loop_check3(self,a_list) :
        n = len(a_list)
        for i in range(n) :
            a = a_list[i]
            if self.date_comp(a,30) :
                for j in range(i + 1,n) :
                    b = a_list[j]
                    if self.date_comp(b,30) :
                        for k in range(i + 2,n) :
                            c = a_list[k]
                            if self.date_comp(c,30) and self.sum_check([a,b,c]) :
                                a_list.remove(a)
                                a_list.remove(b)
                                a_list.remove(c)
                                return [a,b,c]
        return []
