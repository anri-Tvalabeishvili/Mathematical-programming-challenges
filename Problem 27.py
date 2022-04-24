from sympy import isprime

Quantity = 0    # მარტივი რიცხვების რაოდენობა
Produce = 0     # a*b კოეფიციენტების ნამრალი

for a in range (-999, 1000):        # a განსაზღვურლია -999 დან 999 მდე
    for b in range (-1000,1001):    # b განსაზღვრულია -1000 დან 1000-მდე
        n=0                     # n-რიცხვის მნიშვნელობას ნელ ნელა ვზრდით რათა გავიგოთ რა მაქსიმალურ სიმრალემდე ავა
        while isprime(n**2 + (a*n) + b):    # ვამოწმებთ თითოეული n-ის თვის არის თუ არა ნამრავლი მარტივი
            n +=1   # თუ არის მაშნ ვუმატებთ 1-ს რათა შემდეგი რიცხვისთვის განვსაზღვროთ
        if n > Quantity:       # თუ ახლად მიღებული n მეტი იქნება ძველზე ანუ ახალ კოეფიცინტებს უფრო მეტი მარტივი რიცხვის წამოშობა შეუძლიათ მაშინ ძველ n-ს ვანაცვლებთ ახლისთ
            Quantity=n  
            Produce = a*b   

print(Produce)