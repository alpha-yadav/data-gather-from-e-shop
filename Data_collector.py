import selenium.webdriver as web
import time
import os,random,requests,sys,tqdm
#import random
#import requests
try:
    br=web.Firefox()
except:
   try:
      br=web.Ie()
   except:
      try:
         br=web.Chrome()
      except:
         print("BrowserFoundError:\n In this Machine has Ms Edge,Chrome or Firefox not Exist Or Protected Mode.")
         input("Press Enter Key ")
         sys.exit(1)
#br.fullscreen_window()
br.get("https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=200&page=1&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc")
div=br.find_elements("class name","sc-19767e73-1")
br.fullscreen_window()
brand_toggle=br.find_element("css selector","button.limitToggle")
brand_toggle.click()
time.sleep(1)
brand_e=br.find_elements("css selector","span.brand")
brands=[]
for i in brand_e:
   brands.append(i.text)
print(brands)
i,no_img=1,0
file=open("Dat.csv","w")
br.find_element("class name","pdeNg").click()
br.execute_script("window.scrollTo(0,0)")
file.write("Title,Brand,Price,MRP,Prefix_Img")
#os.remove("img")
sy_out=os.system("rmdir /S /Q img")
os.mkdir("img")
length=len(div)
try:
 for s in tqdm.tqdm(range(length),desc="",unit="Mb",colour="yellow",smoothing=0.9):
    sdiv=div[s]
    img=sdiv.find_elements("class name","sc-d13a0e88-1")
    img_file=""
    for j in range(4):
       img_file+=chr(random.randrange(65,91))
    for j2 in range(len(img)):
      #img[j2].screenshot("./img/"+img_file+str(j2+1)+".jpg")
      no_img+=1
      src=img[j2].get_dom_attribute("src")
      img_req=requests.get(src.split("?")[0])
      with open("./img/"+img_file+str(j2+1)+".jpg","wb") as wr:
         wr.write(img_req.content)
    product=img[0].get_dom_attribute("alt")
    for ii in brands:
      if(ii in product):
         product_name=""
         for ij in product.split(ii+" "):
            product_name+=ij
         brand=ii
         break
    price=sdiv.find_element("tag name","strong").text
    mrp=price
    try:
       mrp=sdiv.find_element("class name","oldPrice").text
    except:
       pass
    file.write('\n"'+product_name+'","'+brand+'","'+price+"\",\""+mrp+'","'+img_file+'"')
    #print(img_file,product_name,price,sep=",")
    if(i%4==1):
        br.execute_script("window.scrollBy(0,440)")
        time.sleep(0.2)
    #print(i)
    i+=1
except KeyboardInterrupt:
   print("Interrupt By User")
except Exception:
    print("InternetError:\nNeed Fast Network")
file.close()
br.close()
print("Total Product collect",i-1,"\nTotal Image collect",no_img,sep=" : ")