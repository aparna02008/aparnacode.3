import numpy as np
sales=np.random.randint(0,100,size=35)
product=np.array(["milk","rice","bread","egg","fruit"])
day=np.array(["Day1","Day2","Day3","Day4","Day5","Day6","Day7"])
data=sales.reshape(7,5)
print(data)
total=data.sum(axis=0)
print("Total weekly sales per product:",total)
max_index=np.argmax(total)
p_max=product[max_index]
print("Best-selling product of the week",p_max)
d_total=data.sum(axis=1)
d_index=np.argmax(d_total)
day_max=day[d_index]
print("Day with the highest overall sales:",day_max)
d_avg=data.mean(axis=0)
print("Average sales per day:",d_avg)
p_avg=data.mean(axis=1)
print("Average sales per product:",p_avg)
sum_total=data.sum()
percentage=(data/sum_total)*100
print("Normalize the sales data to percentage",percentage)
sales=np.sort(data,axis=1)
print("Sales per day:",sales)