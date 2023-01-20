import copy

def Measure(star,end,wide,fi):
    fi = list(map(int,fi.split()))
    data = {}
    lst = [] ; midvalue = []
    for i in range(star,end+1): #star to end ... กว้าง
        lst.append(i) 
        if len(lst) == wide: 
            if wide % 2 == 0 : 
                mid = (lst[0] + lst[-1]) / 2
                midvalue.append(mid)
            else: 
                mid = int((len(lst)+1)/2) - 1 
                midvalue.append(lst[mid])
            name = f"data {lst[0]} - {lst[-1]}" 
            data[name] = copy.deepcopy(lst)
            lst.clear()
    xifi = [x * i for x,i in zip(midvalue,fi)]
    avgdata = sum(xifi) / sum(fi)
    x = [abs(i - avgdata) for i in midvalue]
    data_MD = [fi * avg for fi,avg in zip(fi,x)]
    MD = sum(data_MD) / sum(fi)
    value = {
        "data" : data,
        "xi"   : midvalue,
        "fi"   : fi,
        "fixi" : xifi,
        "|xi-x|" : x,
        "fi|xi-xi|" : data_MD,
        "Avgdata" : avgdata,
        "MD"   : MD
    }
    return value

# def input_data(): #test
# 	s = int(input("ใส่ค่าเ ริ่มต้น : "))
# 	e = int(input("ใส่ค่าสุดท้าย : "))
# 	w = int(input("ใส่ค่าความกว้าง : "))
# 	fi = str(input("ใส่ค่าความถี่ : "))
# 	data = { 
# 				"star" :  s,
# 				"end"  :  e,
# 			 	"wide" :  w,
# 			 	"fq"   :  fi
# 	}

# 	return data

if __name__ == '__main__':
    # d = input_data()
    data = Measure(5,24,5,"2 6 12 20")
    # print(data["data"]["data5 - 9"])
   
                

    


            
