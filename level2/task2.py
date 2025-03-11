def fibbo_series(num):
    i = 1
    a,b = 0,1
    while i <= num:
        print(a,end=' ')
        a,b = b,a+b
        i+=1
fibbo_series(int(input("number of time fibbo series..")))

