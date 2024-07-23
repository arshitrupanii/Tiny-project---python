def check_lcm(a,b):
    maxi = max(a,b)
    while(True):
        if(maxi%a == 0 and maxi%b == 0):
            return maxi
        maxi+=1

def check_hcf(a,b):
    mini = min(a,b)
    for i in range(1 , mini + 1):
        if a%i == 0 and b%i == 0:
            hcf = i

if __name__ == "__main__":
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))

    print("The LCM is ", check_lcm(a,b))
    print("The HCF/GCD is ", check_hcf(a,b))