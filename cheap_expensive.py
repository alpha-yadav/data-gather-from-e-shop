file=open("Dat.csv","r")
file.readline()
prices=[]
mrps=[]
product=[]
while True:
    data=file.readline()
    if(data==""):
        break
    p_m=data.split('","')
    product.append(p_m[0])
    prices.append(float(p_m[2].replace(",","_")))
    mrps.append(float(p_m[3].replace(",","_")))
#print(mrps,prices)
p_m=[max(prices),min(prices)]
p_r=[max(mrps),min(mrps)]
print("Most expensive and Cheapest Product by Price have ",product[prices.index(p_m[0])],"\" with ",p_m[0]," and ",product[prices.index(p_m[1])],"\" with ",p_m[1]," respectively\
      \nMost expensive and Cheapest Product by MRP have ",product[mrps.index(p_r[0])],"\" with ",p_r[0]," and ",product[mrps.index(p_r[1])],"\" with ",p_r[1]," respectively")