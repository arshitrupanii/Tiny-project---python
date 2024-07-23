import os, data
os.system('cls')

print("Kon Banega Crodpati main Apka swagat hain.\n")
print("Computer ji sawal Pesh kiya Jaye -- \n")
print("Apka Pehla sawal Pesh kiya Jata hain -- \n")


ans = ('a','c','b','a','c','a','b','d','a','c','b','b','a','c','a')
total = 0

for i in range(0, len(data.que)):
    price = [100,150,200,300,500,1000,2000,4000,8000,16000,32000,64000,128000,256000,512000]
    print(data.que[i])
    print("Your option is {a, b, c, d} \n")
    
    user_ans = input("ans := ")
    
    if user_ans == ans[i]:
        print(f"---Congratulations You are win $ {price[i]}")
        total += price[i]
        print(f"---You Total win {total}")

    else :
        print("\n:- Maf kijiye app age nahi khel sakte")
        print(":- Kon banega Karodpati main aake khelne ke liye apka bahut bahut shukriya 🎉🎉🎉\n")
        exit()
