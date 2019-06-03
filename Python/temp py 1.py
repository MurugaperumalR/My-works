mystring = 'this is test'
print(mystring)
len(mystring)
mystring[0]
mystring[1]
mystring[5:6]
mystring[:7]
mystring[4:]
mystring[-6]
example= mystring[5:]


#######tuples##############
mytuple = (11,12,13)
mytuple[1]
mytuple += (44,)
import numpy as np
np.mean(mytuple)
np.median(mytuple)
atuple=sorted(mytuple)
newtuple= tuple('this is my text')


def area_volume_of_cube (sidelength):
    area = 6*sidelength*sidelength
    volume = sidelength*sidelength*sidelength
    return area, volume

area_volume_of_cube(6)


def simple_intrest (principle,years,rate):
    si=(principle*years*rate)/100
    return si
simple_intrest(100,1,.1)
    
def compound_intrest (principle,years,rate):
    ci= principle*(pow((1+rate/100),years))
    return ci
compound_intrest(100,1,.1)

#######tuples############
mytuple=(4,4.5,True,'hello')

######dictioneries#############
arabic2roman={1:'i',2:'ii',3:'iii',4:'iv'}
arabic2roman[1]
len(arabic2roman)
arabic2roman[1]='one'
age={'aaa':2,'bbb':22}

age['aaa']
age={'a':1,'b':2,'a':3}#######it will not duplicate it will give the last##

age['a']

arabic2roman.items()
arabic2roman.keys()
arabic2roman.values()

age.update()

age.pop('a')

age.popitem()########remove random variablr#####

###########list alises##########
a=[5,6,7,8]
b=a
a[0]= 'change'
b[0]=5
c=a[0:3]   ###list and dic are mutable##
           ###sreing and tuples are imutable##
########sets########
cset={11,11,12}  
cset    
aset=cset  
cset=cset([55])   


myset={'apple','banana','oranga'}
myset[0]

aset={11,22,33}
bset={55,66,33}
aset|bset  #######union
aset&bset   #### intersection
aset={11,22,33}
bset={55,66,33}
aset-bset # difference
aset^bset  ###uncommon


########nympy#########
import numpy as np
data1=[[1,2,3,4],[5,6,9,8]]
ar1=np.array(data1)
ar1.ndim
ar1.shape
ar1.dtype
ar1.__class__
np.zeros((3,6))
np.ones((3,6))
np.random.randn(4,5)
np.arange(15).reshape(3,5)
np.arange(27).reshape(3,3,3)

arr=np.arange(10)
arr[4:7]
arr=np.random.randn(3,5)
arr_trans=arr.T

random_array=np.dot(arr,arr_trans)

arr1=np.arange(6).reshape(2,3)
arr2=np.arange(6).reshape(3,2)
arr12=np.dot(arr1,arr2)

x1=[4,5,6]
x2=[2,2,8]
np.greater_equal(x1,x2)
np.mod(x1,x2)

x1=[True,True,False,True]
x2=[True,False,True,False]
np.logical_and(x1,x2)


ar_1=np.random.randn(15).reshape(3,5)
np.mean(ar_1)
np.var(ar_1)
np.corrcoef(arr1,arr2)


x=np.random.randn(10)
y=np.random.randn(10)
z=np.random.randn(10)

a=np.array(zip(x,y,z))
b=np.array([[1,2,3],[2,3,4]])
z=np.zeros((1,3))
np.append(b,z,axis=1)
###axis=0 is row, axis=1 is coloumn####




















































































































