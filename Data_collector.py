import selenium.webdriver as w
import time
web=w.Chrome()
#product=[]
web.get("https://www.amazon.in/s?i=electronics&rh=n%3A6612025031&fs=true&page=1&qid=1730994607&ref=sr_pg_2")
time.sleep(2)
data=open("Data.csv","w")
data.write("Product,Price,Rating")
def remove(st:str)->str:
     st=st.replace("\n"," ")
     return st.replace("\"","inch")
for ii in range(1,101):
    nok=0
    web.get("https://www.amazon.in/s?i=electronics&rh=n%3A6612025031&fs=true&page="+str(ii)+"&qid=1730994607&ref=sr_pg_2")
    #print(ii)
    #time.sleep(2)
    #input(":::")
    progress=web.find_element("id","twotabsearchtextbox")
    progress.send_keys("#"*((ii-1)//5))
    k=web.find_elements("css selector","div.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16")
    for i in k[2:-1]:
         try:
            n='"'+i.find_element("tag name","h2").text+'"'
            p="\""+i.find_element("class name","a-price").text+"\""
            #"span.a-icon-alt")[0].innerText.split(" ")[0]
            temp=i.find_element("css selector",".a-row.a-size-small")
            r=temp.find_element("tag name","span").get_dom_attribute("aria-label").split(" ")[0]
            #i.find_element("css selector","span.a-icon-alt").text.split(" ")[0]
            data.write("\n")
            data.write(remove(n)+","+remove(p)+","+remove(r))
            nok+=1
         except:
               pass
               #print(nok)
         #print("#",end=" ")
data.close()
web.close()
print("Complete..")
#print(product)
#https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar
#https://www.amazon.in/s?i=electronics&rh=n%3A6612025031&fs=true&page=2&qid=1730994607&ref=sr_pg_2