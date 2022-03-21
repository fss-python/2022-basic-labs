signal=[8.4,3.3,4.5,1.2,5.6,8.1,4.0,2.3,4.1]
#        1   0    1  0   0   1   0   0   1
maximums=[0,0,1,0,1,0,0,1]
times=[1,3,6,10,20,35,55,65]

ms_list = []

#for i in times:
#    for i in maximums:
for i in range(len(maximums)):
    if maximums[i] == 1:
        ms_list.append(times[i])

#   for i in range(len(maximums)):
#      if maximums[i] == 1:
#          ms_list.append(times[i])

print(ms_list)
print(len(ms_list))




#def calculate_rr(maximums: list, times: list):
'''
if type(maximums) != list or type(times) != list:
    return None
i = maximums.index(1)
rr_list = []
for m in maximums[i:]:
    if type(m) != bool:
        return None
    if m == 1:
        rr = times[maximums.index(1, i + 1)] - times[i]
        print(rr)
        rr_list.append(rr)
        i += 1
    else:
        i += 1

return rr_list
'''
'''
 i = maximums.index(1)
 rr_list = []
 for m in maximums[i:]:
     if type(m) != int:
          return None       
     if m == 1:
         rr = times[maximums.index(1, i + 1)] - times[i]
         print(rr)
         rr_list.append(rr)
         i += 1
     else:
         i += 1

 return rr_list
 pass
 '''

'''
def calculate_rr(maximums: list, times: list):
   
    if type(maximums) != list or type(times) != list:
        return None

  
    i = maximums.index(1)
    rr_list = []
    for m in maximums[i:]:
        if type(m) != int:
             return None
        if m == 1:
            pt = times[i]
            i += 1
            if maximums.index(1, i) != 0:
                rr = times[maximums.index(1, i)] - pt
                print(rr)
                rr_list.append(rr)
                print(rr_list)
            else:
                break

        else:
            i += 1

    return rr_list
    pass
'''

'''

mxms=[]
threshold = 2.1
i = 0

mxms = [0]
for s in signal:
        if type(threshold) != float or type(s) != float:
            print('None')
            break
        else:
            for s in signal[1:-2]:
                if signal[s] >= threshold and signal[s - 1] < signal[s] and signal[s + 1] < signal[s]:
                    mxms.append(1)
                else:
                    mxms.append(0)


            if signal[-1] >= threshold and signal[-2] > signal [-1]:
                mxms.append(1)
            else:
                mxms.append(0)
'''
'''
while i < len(signal)-2:

    if type(threshold) != float or type(signal[i]) != float:
        print('None')
        mxms=[]
        break

    else:

        if signal[0] >= threshold and signal[0] > signal[1]:
            mxms.append(1)
            i+=1
            if signal[i] >= threshold and signal[i - 1] < signal[i] and signal[i + 1] < signal[i]:
                mxms.append(1)
                i += 1
            else:
                mxms.append(0)
                i += 1
        else:
            mxms.append(0)
            i+=1
            if signal[i] >= threshold and signal[i - 1] < signal[i] and signal[i + 1] < signal[i]:
                mxms.append(1)
                i += 1
            else:
                mxms.append(0)
                i += 1


print(i)
print(signal[i])
print(mxms)

'''



'''
for s in range(len(signal[1:-1])):
    if signal[s] >= threshold and signal[s - 1] < signal[s] and signal[s + 1] < signal[s]:
        mxms.append(1)
    else:
        mxms.append(0)
print(mxms)

'''


'''

l=[2.5,3.4,4.5,1.2,5.6,3.6]
print(l[-1])
x = []
print(x)
x.append(True)
x.append(False)
print(x)


def calculate_threshold(signal: list):
    """Calculating threshold for RR peaks detection"""
    thrh = max(signal) * 0.8
    return(thrh)
    pass

print(calculate_threshold(l))

print(type(l[0]))
for i in l:
    if type(i)!=float:
        print('no')
    else:
        print("yes")

mxms = list()
list=[0,1,0,1]
mxms+=[1]
print(mxms)



print('-----------------------------')
a=1

print(a)

#REPL -Read Eval Print Loop
#exit()


a=2 # int - integer number
b=2.3 # float - floating point number

print(a)
print(b)


a= int ('2') # cast/casting
b=float ('0.5')

print(a,b)

print('Арифметические операции')
print(a*b)
print(a/b)
print(a+b)
print(a-b)

if 5 % 2 == 0:
    print('четное число')
else:
    print('нечетное число')

'''
