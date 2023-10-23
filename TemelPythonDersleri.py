#!/usr/bin/env python
# coding: utf-8

# # Python Dersleri

# ## Değişkenler

# In[57]:


x = 10
type(x)


# In[58]:


y = 10.3
type(y)


# In[59]:


z = True
type(z)


# In[60]:


a = "1"
type(a)


# In[61]:


b = '1'
type(b)


# ## Input

# In[62]:


yas = input("Yaşınızı Giriniz.")


# In[63]:


yas


# In[64]:


type(yas)


# In[65]:


inputInt = int(yas)
type(inputInt)


# ## String

# In[70]:


Name = "Burak Yılmam"
print(Name)


# In[69]:


print("Burak \n Yılmam")


# In[71]:


len(Name)


# In[83]:


type(Name)


# ## Slicing

# In[86]:


Name[0]


# In[76]:


Name[2:]


# In[80]:


Name[0:7]


# In[78]:


Name[:4]


# In[87]:


Name[-1]


# In[89]:


Name[::3]


# In[90]:


Name[::-1]


# ## String Methodları

# In[94]:


Name = "ali veli"
Name.capitalize()


# In[95]:


Name.split()


# In[96]:


Name.lower()


# In[97]:


Name.upper()


# ## Listeler

# In[123]:


list = [10,"20",True]
list[2]


# In[104]:


type(list)


# ## Liste Metodları 

# In[116]:


list.append('Deneme')
list


# In[107]:


list.clear()
list


# In[117]:


list.remove('Deneme')
list


# In[124]:


list.pop()
list


# In[126]:


list.count(10)


# In[130]:


list2 = [3,1,2]
list2.sort()
list2


# In[131]:


list2.reverse()
list2


# In[133]:


list3 = list + list2
list3


# ## Nested List

# In[172]:


list4 = [1,2,[3,[4,5]],"5",True]
list4[2]


# In[144]:


list4[2][1]


# In[145]:


list4[2][1][0]


# In[146]:


list4[2:]


# In[148]:


list4[2:3]


# In[150]:


list4[::2]


# 

# In[ ]:





# ## İf Else

# In[168]:


yas = input("Yaşınızı Giriniz.")
yas = int(yas)
if(yas < 10):
    print("Yaşınız 10dan küçük")

elif(yas > 10):
    print("Yaşınız 10dan büyük")

elif(yass == 10):
    print("Yaşınız 10")

else:
    print("Hata")


# In[169]:


yas = input("Yaşınızı Giriniz: ")
yas = int(yas)
if yas < 10:
    if yas > 5:
        print("Yaşınız 5'ten büyük")
    else:
        print("Yaşınız 5'ten küçük")
else: print("Yaşınız 10'dan büyük")


# In[177]:


Liste = [1,2,3]
if 4 in Liste:
    print("Var")
else:
    print("Yok")


# In[179]:


Name = "Burak"
if 'a' in Name:
    print("Var")
else:
    print("Yok")


# ## Döngüler

# In[182]:


Liste = [1,2,3]
for eleman in Liste:
    print(eleman)


# In[187]:


for i in range(10):
    print(i)


# In[188]:


for i in range(5,10):
    print(i)


# In[189]:


for i in range(0,10,2):
    print(i)


# In[196]:


name = "Burak"
for i in range(len(name)):
    print(name[i])


# ## While

# In[237]:


x = 0
while x < 10:
    print("Sayı",x)
    x = x+1
    if(x % 2 == 0):
        print("Çift",x)
    else:
        print("Tek",x)


# In[223]:


x = 5
while 5 <= x <= 10:
    print(x)
    x = x+1


# ## Random

# In[239]:


from random import randint


# In[243]:


randint(0,100)


# ## Fonksiyon

# In[244]:


def Topla(s1,s2):
    toplam = s1 + s2
    print(toplam)


# In[249]:


s1 = input("Sayı 1 ")
s1 = int(s1)
s2 = input("Sayı 2 ")
s2 = int(s2)
Topla(s1,s2)


# In[250]:


def Toplama(*args):
    return sum(args)


# In[251]:


Toplama(3,4,5,6)


# In[ ]:


def HesapMakinesi(s1,s2,islemtip):
    if islemtip == "+":
        toplam = s1 + s2
        print(toplam)
    if islemtip == "-":
        fark = s1 - s2
        print(fark)
    if islemtip == "/":
        bolme = s1 / s2
        print(bolme)
    if islemtip == "*":
        carpma = s1 * s2
        print(carpma)


# In[ ]:


s1 = int(input(s1))
s2 = int(input(s2))
islemtipi = input("+-/* ")
HesapMakinesi(s1,s2,islemtipi)


# # OOP
# ## Sınıf

# In[41]:


class İnsan():
    def __init__(self,name,surname,age,weight,height):
        self.name = name
        self.surname = surname
        self.age = age;
        self.weight = weight
        self.height = height
    def KitleEndeksi(self):
        endeks = self.weight * self.height / 100
        print(endeks)


# In[42]:


Ali = İnsan("Ali","Yılmaz",15,50,1.60)


# In[43]:


print("Adı : ",Ali.name)
print("Soyadı : ",Ali.surname)
print("Yaşı : ",Ali.age)
print("Kilo : ",Ali.weight)
print("Uzunluk : ",Ali.height)


# In[44]:


name = input("Adınız ")
surname = input("Soyadınız ")
age = int(input("Yaşınız "))
weight = float(input("Kilonuz "))
height = float(input("Boyunuz "))


# In[45]:


insan1 = İnsan(name, surname, age,weight,height)


# In[46]:


print("Adı : ",insan1.name)
print("Soyadı : ",insan1.surname)
print("Yaşı : ",insan1.age)
print("Kilo : ",insan1.weight)
print("Boy : ",insan1.height)


# In[47]:


insan1.KitleEndeksi()


# ## Inheritence

# In[58]:


class İnsan():
    def __init__(self,name,surname,age,weight,height):
        self.name = name
        self.surname = surname
        self.age = age;
        self.weight = weight
        self.height = height
class Bebek(İnsan):
    def __init__(self, name, surname, age, weight, height, eyecolor):
        super().__init__(name, surname, age, weight, height)
        self.eyecolor = eyecolor


# In[59]:


bebek1 = Bebek("Aslı","Yıldız",1,10,1.2,"Ela")


# In[61]:


print("Adı:", bebek1.name)
print("Soyadı:", bebek1.surname)
print("Yaşı:", bebek1.age)
print("Kilosu:", bebek1.weight)
print("Boyutu:", bebek1.height)
print("Göz Rengi:", bebek1.eyecolor)


# ## Polymorphism

# In[63]:


class İnsan():
    def __init__(self,name,surname,age,weight,height):
        self.name = name
        self.surname = surname
        self.age = age;
        self.weight = weight
        self.height = height
    def Konus():
        print("Ses 123")
class Bebek(İnsan):
    def __init__(self, name, surname, age, weight, height, eyecolor):
        super().__init__(name, surname, age, weight, height)
        self.eyecolor = eyecolor
    def Konus():
        print("Agu bugu")


# In[69]:


Bebek.Konus()


# In[70]:


İnsan.Konus()


# ## Encaptulaion

# In[71]:


class İnsan:
    def __init__(self, name, surname, age, weight, height):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__weight = weight
        self.__height = height

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height


# In[86]:


insan1 = İnsan("John", "Doe", 30, 70, 180)
yas = insan1.get_age
yas = yas()
print(yas)


# 

# In[ ]:




