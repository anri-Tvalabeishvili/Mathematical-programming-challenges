from itertools import permutations  
import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time() 

perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # შემოგვყავს ლისთი რომელშიც იქნება პერმუტატიულობის სიმრავლე
 

counter = 0           # პოზიციის დასათვლელად შემოგყვავს ქაუნთერი
for i in list(perm):    # ციკლით ვისშვებთ ყველა პერმუტატიულ სიმრავლეს
    counter += 1        # ყოველი ახალი სიმრავლის გაშვებისას მთვლელს ვუმატებთ 1-ს

    if counter == 1000000:  # როცა მთვლელი მივა მემილიონე ელემეტზე პრინტავს ამ ელემეტს როგორც რიცხვს
        number = ""         # ვქმნით ცარიელ სტრინგ - ცვლადს
        for k in range(len(i)):
            number += str(i[k])  # თავიდან არსებულ სიცარიელეს ვუმატებთ მემილიონე პემუტაციური ლისთის თითოეულ ელემეტს რათა საბოლოოდ წარმოსდგეს რიცხვად
        print(number)  

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს