import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

answer = []  # ვქმნით ლისთს რათა შევინახოთ Pandigital products-ები
chack = set('123456789')        # ვქმნით სეთს რათა შევადაროთ თუ შემდგომში ნამრავლსა და სამრავლებს

for i in range (1,100):     # ვიღებთ რეინჯებს
    for k in range (100,10000):

        number_str = str(i*k) + str(i) + str(k)     # სტრინგის სახით ვწერთ ნამრავლსა და ნამრავლებს
        number = i*k        # ინტეჯერის სახით ვწერთ ნამრავლს
        if len(number_str) == 9 and set(number_str) == chack and number not in answer:  # თუ number_str ტოლია 9  და ციფრებიც მოცემულია 1-დან 9-მდე მაშინ ვამატებთ ლისთში
                answer.append(number)
            
""" line 10      თუ ნამრავლის და სამრავლების სტრინგის სიგრძე არ არის ტოლი 9-ს მაშინ ფიზიკურად ვერ იქნება მოცემული ყველა ციფრი 1-დან 9-მდე
როცა მის სიგგრძეს შევამოწმებთ მერე ვამოწმებთ ნამდვლად შედის თუ არა ყველა ციფრი 1-დან 9-მდე
და ბოლოს იგივე ციფრისგან თავის არიდების მიზნით ვამოწმებთ გვაქვს თუ არა კონკრეტული რიცხვი უკვე დამატებული პასუხების ლისთში """

print(sum(answer))
    

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს