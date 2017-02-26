a=[]
c=0
print "Press the letter s to end the list"
timh = raw_input("Enter the number of your choice: ")

while "TRUE":
    if (timh != "s"):
        a.append(timh)
        timh = raw_input("Enter again the number of your choice: ")
        c = c+1
    else:
        break;
print a 
print "Your list has changed to"
for i in range(0,c):
    if (a[i] == '0'):
        a.remove(a[i])
        a.append('0')
       
print a
