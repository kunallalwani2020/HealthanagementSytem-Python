import datetime
def gettime():
         return datetime.datetime.now()

def take(k):
    if k==1:
        c= int(input("Press the key\n1)Food\n2)Exercise"))
        if c==1:
            type = input("Type here")
            with open("Hammad-food.txt","a") as f:
                f.write(str([str(gettime())])+": "+type+"\n")
                print("Successfuly")
        elif c==2:
            type = input("Type here")
            with open("Hammad-exe.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + type + "\n")
                print("Successfuly")
    elif (k == 2):
            c = int(input("Press the key\n1)Food\n2)Exercise"))
            if c == 1:
                type = input("Type here")
                with open("Harry-food.txt", "a") as f:
                    f.write(str([str(gettime())]) + ": " + type + "\n")
                    print("Successfuly")
            elif c == 2:
                    type = input("Type here")
                    with open("Harry-exe.txt", "a") as f:
                        f.write(str([str(gettime())]) + ": " + type + "\n")
                        print("Successfuly")
    elif (k == 3):
        c = int(input("Press the key\n1)Food\n2)Exercise"))
        if c == 1:
            type = input("Type here")
            with open("Rohan-food.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + type + "\n")
                print("Successfuly")
        elif c == 2:
            type = input("Type here")
            with open("Rohan-exe.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + type + "\n")
                print("Successfuly")
        else:
            print("Please Enter Valid Input")
def retrieve(k):
        if (k==1):
                 c = int(input("Press the key\n1)Food\n2)Exercise"))
                 if c == 1:
                     with open("Hammad-food.txt")as f:
                         for i in f:
                             print(i,end="")
                 elif c==2:
                     with open("Hammad-exe.txt") as f:
                         for i in f:
                             print(i, end="")
        elif (k==2):
                     c = int(input("Press the key\n1)Food\n2)Exercise"))
                     if c == 1:
                         with open("Harry-food.txt") as f:
                             for i in f:
                                 print(i, end="")
                     elif c == 2:
                         with open("Harry-exe.txt") as f:
                             for i in f:
                                 print(i, end="")
        elif (k==3):
                         c = int(input("Press the key\n1)Food\n2)Exercise"))
                         if c == 1:
                             with open("Rohan-food.txt") as f:
                                 for i in f:
                                     print(i, end="")
                         elif c == 2:
                             with open("Rohan-exe.txt") as f:
                                 for i in f:
                                     print(i, end="")
                                 else:
                                     print("Please Enter Valid Input")


























print("-------------*Health Management System*-------------")
a = int(input("1) Look\n2) Retrieve"))
print("-------------------------------")
if a==1:

   b = int(input("1) Hammmad\n2) Harry\n3) Rohan"))
   print("--------------------------------------")
   take(b)
else:
    b = int(input("1) Hammmad\n2) Harry\n3) Rohan"))
    retrieve(b)



