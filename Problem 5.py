import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

""" 
ამ დავალების მთავარი მიზანია ვიპოვოთ ისეთი ციფრები, რომელთა ერთმანეთზე გამრავლებით მივიღებთ ნებისმიერ ციფრს 2-დან 20-მდე
თუ ჩვენ მოვახერხებთ და ასეთ ტიცხვებს ვიპოვით და ამავდროულად ერმანეთზე გადავამრავლებთ მივიღებთ იმ იმცირეს რიცხვს რომელიც უნაშდოდ
იყოფა 2-დან 20-მდე ნებისმიერ ციფრზე

 """

list = []   # ვქმნით სიას სადაც შევინახავთ რიცხვთა სიმრავლეს რაზეც უნდა იყოფოდეს მისაღები რიცხვი


for i in range(2,21):       # ზემოთ აღნიშნულ სიაში ვამატებთ ამ ციფრებს
    list.append(i)

for i in range(0, len(list)):       # ამ ციკლით ვწვდებით თითოეულ ელემენტს ჩვენს სიაში
    for j in range(1, i+1):         # ამ ციკლით ვწვდდებით i-ელემენტამდე არსებულ სხვა ელემენტებს (რაგან სია ზრდადობითაა დალაგებული)
        if list[i] % list[i-j] == 0:       # თუ i-ადგილას მდგომი ციფრი უნაშდოდ იყოფა მის წინ არსებულ ციფრზე მაშინ
            list[i] = int(list[i] / list[i-j])  # i-ადგილას მდგომ ციფრს ვყოფს მის წინ არსებულ ციფრზე და მიღებულ განაყოფით ვანაცვლებთ მას

answer = 1

for i in range(0, len(list)):   # ვიღებთ ჩანაცვლებულ და ჩაუნაცვლებელ ციფრებს
    answer = answer * list[i]       # ამ ციფრებს ვამრავლებთ ერმანეთზე

print(answer)


end = time.time()  
print(end-start)    # ვპრინტავთ გამოთვალზე დახარჯულ დროს