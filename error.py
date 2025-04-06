def fuc():
    try:
        l=[1,6,8,9,56]
        i=int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I always execute")
x=fuc()
print(x)
    