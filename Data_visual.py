import matplotlib.pyplot as plt
import sys
no_product_brand=dict()
file=open("Dat.csv","r")
file.readline()
brands=[]
while True:
    data=file.readline()
    if(data==""):
        break
    data=data.split('","')[1]
    try:
        no_product_brand[data]+=1
    except KeyError:
        no_product_brand[data]=1
        brands.append(data)
frequency=[]
for i in brands:
    frequency.append(no_product_brand[i])
print("Brands :",brands,"\nfrequency : ",frequency)
for j in range(len(brands)):
    print(brands[j],end="=")
    index=chr(65+j)
    if(65+j>90):
        index="A"+chr(65+j%26)
    brands[j]=index
    print(index)
file.close()
p=plt.bar(brands,frequency)
plt.title("Number of Products from Each brand")
plt.xlabel("Index Name of Brand")
plt.ylabel("Number of Products")
plt.show()
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()