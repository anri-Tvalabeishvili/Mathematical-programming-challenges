import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


limit = 28123     # შემოგვაქ ზღვრული რიცხვი

def divisors(number):    # ვქმნით ფუნქციას რომელიც აჯამავას ყველა გამყოფს გარდა თივითონ ამ რიცხვისა 
    factor_1 = 0        # ვადგენთ საწისს გამყოფს
    factors= []         # ვქმნით ლისთს რათა რიცხვის გამოყოფები დროებით გავათავსოთ
    while True:             
            factor_1+=1         # საწყის გამყოფს ვუმატებთ 1-ს, ანუ პირველ გამყოფად ვიღებთ 1-ს
            if (number) % factor_1 == 0:        # თუ რიცხვი უნაშთოდ იყოფა საწყის გამყოფზე
                factor_2 = number / factor_1        # რიცხვს ვყოფთ ამ გამყოფზე და ვინახავთ ცვლადში

                if factor_1 < factor_2 :            # ამ ლოგიკით ორჯერ ვამცირებთ შემოწმების დროს რადგან 2*4=8 და 4*2=8
                    factors.append(int(factor_1))   # ორივე გამყოფს ვამატებთ გამყოფთა სიაში
                    factors.append(int(factor_2))   # ორივე გამყოფს ვამატებთ გამყოფთა სიაში
                elif factor_1 == factor_2:          # თუ რიცხვი იშლება კვადრატულ წევრათ მაგალითად 9*9 = 81 გამყოფებში ვწერთ მხოლოდ ერთ 9-იანს
                    factors.append(int(factor_1))
                else:
                    break   # მეორე გამყოფი გადააჭარბებს პირველ გამყოფს შესაბამისად ვწყვეტთ ციკლს
    if number in factors:
        factors.remove(number)      # ამ რიცხვს ვაგდებთ მისივე გამყოფებიდან ანუ 5 გამყოფები თია 1 და 5, ვტოვებთ მხოლოდ 1-ს
    
    new_number = sum(factors)       #  ვკრიბავთ ყველა გამყოვს
    return new_number       # და ფუნქციის პასუხად ვაბრუნებთ გამყოფთა ჯამს

 
abundant = []    # ვქმნით ლისთს სადაც შევინახავთ abundant-რიცხვებს 

for i in range(12,limit):       # 12 -დან ზღვრულ მაჩვენებლამდე ვირჩევთ რიცხვებს რათა გავიგოთ არიან თუ არა ისინი abundant-რიცხვები
    number = divisors(i)
    if number > i :         # თუ არიან მაშინ ვამატებთ
        abundant.append(i)



all_numbers = [i for i in range(limit)]   # ვქმნით რიცხვების მასივს 0-დან ზღვრამდე


for k in range(len(abundant)):
    for i in range(k,len(abundant)):
        if abundant[k] + abundant[i] < limit:       # თუ რომელიმე abundant-რიცხვის ჯამი ნაკლებია ზღვრულ მაჩვენებელზე მაშინ კვრიბავთ ამ რიცხვებს
            all_numbers[abundant[i]+abundant[k]] = 0    # ამ ორი რიცხვის ჯამს აუცილებლად შეესაბამება რიცხვის all_numbers-ის ლისთიდან, სწორედ ამ ციფრს all_numbers-ში ვუტოლებთ ნულს
                                                        # რათა დაგვჩეს მხოლოდ ის ციფრები რომლებიც არ წარმოსდგებიან როგორც ორი abundant რიცხვის ჯამი
print(sum(all_numbers))     # ვკრიბავთ მთლიან ლისთს სადაც ყველა ის ციფრი რომელი მიიღება ორი abundant- რიცხვის შეკრებით, გატოლებულია 0-ის


print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს