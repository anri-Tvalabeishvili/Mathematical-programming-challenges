import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


largest_sum = 0  # ვქმნით საწყის ჯამს შესადარებლად

for a in range(1,101):  # შემოგვყავს a კომპონენტი
    if a == 10:     # ვტოვებთ 10-ს რადგან მისი ყველა ხარისიხს ციფრთა ჯამი 1-ია
        continue
    for b in range(3,101): # შემოგვყავს b კომპონენტი
        number = a**b   # ვქმნით ახარისხებულ რიცხვს
        digits = [int(x) for x in str(number)]  # ახარისხებულ რიცხვს ვწერთ სიის სახით რათა შემდეგ შევკრიბოთ
        
        if sum(digits) > largest_sum:   # თუ ახალი რიცხვის ციფრთა ჯამი მეტი იქნება ძველი რიცხვის ციფრთა ჯამზე მაშინ 
            largest_sum = sum(digits)   # ძველ ციფრთა ჯამს ვცვლით ახალი ციფრთა ჯამით

print(largest_sum) # ვპრინტავთ პასუხს
print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს

