import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


Numbers = [1,2]    # ვქმნით სიას საწყისი ფიბონაჩის რიცხვებით

even_numbers= []   # ვქმნით სიას სადაც შევინახავთ ლუწ რიცხვებს


while True:                     # ვიყენებთ while ოპერატორს რათა უსასრულოდ გავაგრძელოთ მოქნედება
    if Numbers[-1] < 4e6:           # სანამ ფიბონაჩის ბოლო რიცხვი ნაკლებია 4 მილიონზე მანამ გავაგრძელოთ მოქმედება
        Previous_1 = Numbers[-1]      # ვიღემთ სიის (ფიბონაჩის) ბოლო წევრს
        Previous_2 = Numbers[-2]      # ვიღემთ სიის (ფიბონაჩის) ბოლოს წინა წევრს
        new_number = Previous_1 + Previous_2  # ამ ორ წევრს ვუმატებთ ერთმანეთს (რათა გავიგოთ შემდგომი წევრი)
        Numbers.append(new_number)    # ახალ წევრს ვამატებთ სიაში
    else:
        break                   # თუ ბოლო ციფრი გადააჭარბებს 4 მილიონს, ვწყვეტთ while ოპერატორს


for i in Numbers:               # შეგროვებული ფიბონაჩის რიცხვებიდან ვიღებთ თითოეულს
    if i % 2 ==0 :              # ვამოწმებთ არის თუ არა ლუწი 
        even_numbers.append(i)  # თუ ლუწია ვამატებთ ლუწების სიაში 


print(sum(even_numbers))    # ვკრიბავთ ყველა იმ ლუწ ბიბონაჩის რიცხვს, რომელიც გვხვდება  4-მილიონამდე 

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს