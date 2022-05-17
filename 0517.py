#!/usr/bin/env python
# coding: utf-8

# In[1]:


temp = float(input("請輸入你的體溫"))
if temp >= 37.5:
    print("體溫過高！")
elif temp >= 37 and temp < 37.4:
    print("體溫略高！")
elif temp >= 34 and temp < 36.9:
    print("體溫正常！")
else:
    print("體溫異常，請重新測量！")


# In[2]:


money = int(input("請輸入購物金額:"))
if (money >= 10000):
    if(money >= 100000):
        print("八折", money * 0.8, end = "元\n" )
else:
    print("沒打折", money, end = "元\n") 
    


# In[4]:


score = int(input("請輸入您的成績:"))
if score >= 90:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
else:
    score < 60
    print("E")


# In[7]:


month = int(input("請輸入月份:"))
if month == 3 or month == 4 or month == 5:
    print(str(month) + "月是春天")
elif month == 6 or month == 7 or month == 8:
    print(str(month) + "月是夏天")
elif month == 9 or month == 10 or month == 11:
    print(str(month) + "月是秋天")
elif month == 12 or month == 1 or month == 2:
    print(str(month) + "月是冬天")
else:
    print("月份不在範圍內！")


# In[8]:


income = int(input("請輸入今年收入淨額："))
if income >= 2000000:
    print("付稅金額:", income * 0.3, end = "元\n")
elif income >= 1000000:
    print("付稅金額:", income * 0.21, end = "元\n")
elif income >= 600000:
    print("付稅金額:", income * 0.13, end = "元\n")
else:
    income >= 300000
    print("付稅金額:", income * 0.06, end = "元\n")


# In[ ]:




