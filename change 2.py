##Eric Broadbent
#9/18
# change sorter

def change():
    #1 get input from user find out how much change
    total_change = int(input("how much change do you have in your pocket: "))
    #2 calculate total for q n d p
    q = total_change // 25
    whats_left = total_change % 25
    d = whats_left / 10
    whats_left = whats_left % 10
    n = whats_left / 5
    whats_left = whats_left % 5
    p = whats_left
    #3 display it back to user
    print("Quaters: ",q, "\nDimes: ",d, "\nNickles: ",n,"\nCents: ",p)

#change()

def change2(total_change):
    #1 get input from user find out how much change
    total_change = total_change 
    #2 calculate total for q n d p
    dol = total_change // 100
    whats_left = total_change % 100
    q = whats_left  // 25
    whats_left = whats_left  % 25
    d = whats_left // 10
    whats_left = whats_left % 10
    n = whats_left //5
    whats_left = whats_left % 5
    p = whats_left
    return dol,q,d,n,p
    
total_change = 256
dol,q,d,n,p =change2(total_change)
#3 display it back to user
print("$",dol,"Quaters: ",q, "\nDimes: ",d, "\nNickles: ",n,"\nCents: ",p)





    
