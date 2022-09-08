import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


Numbers = []                        # ვქმნით სიას რათა შევინახოთ ყველა ის 3-სა და 5-ის ჯერადი რიცხვები რაც არის 1000-მე

for i in range(0,1000):             # for-ლუპის დახმარებით ვიძახებთ ყევლა რიცხვს 0-დან 1000-მდე        
    if i % 3 ==0 or i % 5 ==0:      # თუ რომელიმე გამოძახებული რიცხვი 3-სა ან 5-ის ჯერადია, ეს რიცხვი ემატება სიაში
        Numbers.append(i)

print(sum(Numbers))                 # ვკრიბავთ სიის ყველა ელემენტს


print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს