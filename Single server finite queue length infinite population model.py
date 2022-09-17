import math

print("                              Solving queueing model M/M/1/N/∞               ")

x= input("Enter the arrival rate/hour = ")
y= input("Enter the service rate/hour = ")
z= input("Enter the number of finite population = ")
x = float(x)
y = float(y)
z = float(z)
print("The following results for the model is given below : ")
def result():
    row = x/y
    c = (1- row)/(1-math.pow(row,z+1))
    lenns = (row/(1-row)*(1-math.pow(row,z+1)))*(1+(z*math.pow(row,z+1))-(z+1)*math.pow(row,z))

    popn = math.pow(row,z)*c
    m = x*(1-popn)
    lenq = lenns - (m/y)
    times = lenns/x
    timeq= lenq/x
    m = "{:.2f}".format(m)
    popn = "{:.2f}".format(popn)
    c= "{:.2f}".format(c)
    lenns = "{:.2f}".format(lenns)
    lenq = "{:.2f}".format(lenq)
    times = "{:.2f}".format(times)
    timeq = "{:.2f}".format(timeq)
    print("The effective arrival rate for the finite population is = ",m)
    print("The probability of no person is Po =  ",c)
    print("The probability of someone joining the system, Pn = ",popn)
    print("The length of the system is Ls =  ", lenns)
    print("The length of the queue is  Lq = ", lenq)
    print("The waiting time in the system is Ws(hour) =  ", times)
    print("The waiting time in the queue is  Wq(hour) = ", timeq)

result()

