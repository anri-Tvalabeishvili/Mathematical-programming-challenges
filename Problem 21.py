answer = []    # ვქმნით ლისთს პასუხებიშტვის

def Chaker(number):    # ვქმნით ფუნქციას რომელიც აჯამავას ყველა გამყოფს გარდა თივითონ ამ რიცხვისა 
    factor_1 = 0        # ვადგენთ საწისს გამყოფს
    factors= []         # ვქმნით ლისთს რათა რიცხვის გამოყოფები დროებით გავათავსოთ
    while True:             
            factor_1+=1         # საწყის გამყოფს ვუმატებთ 1-ს, ანუ პირველ გამყოფად ვიღებთ 1-ს
            if (number) % factor_1 == 0:        # თუ რიცხვი უნაშთოდ იყოფა საწყის გამყოფზე
                factor_2 = number / factor_1        # რიცხვს ვყოფთ ამ გამყოფზე და ვინახავთ ცვლადში

                if factor_1 < factor_2 :            # ამ ლოგიკით ორჯერ ვამცირებთ შემოწმების დროს რადგან 2*4=8 და 4*2=8
                    factors.append(int(factor_1))   # ორივე გამყოფს ვამატებთ გამყოფთა სიაში
                    factors.append(int(factor_2))   # ორივე გამყოფს ვამატებთ გამყოფთა სიაში
                else:
                    break   # მეორე გამყოფი გადააჭარბებს პირველ გამყოფს შესაბამისად ვწყვეტთ ციკლს
    if number in factors:
        factors.remove(number)      # ამ რიცხვს ვაგდებთ მისივე გამყოფებიდან ანუ 5 გამყოფები თია 1 და 5, ვტოვებთ მხოლოდ 1-ს

    new_number = sum(factors)       #  ვკრიბავთ ყველა გამყოვს
    return new_number       # და ფუნქციის პასუხად ვაბრუნებთ გამყოფთა ჯამს


for i in range (1,10000):       # ვიღებთ ყველა რიცხვს 1-დან 10000-მდე
    first  = Chaker(i)      # ვითვლით პირველი რიცხვის გამყოფთა ჯამს
    second = Chaker(first)  # ვითვლით პირველი რიცხვის გამყოფთა ჯამის გამოყოფთა ჯამს

    if i == second and i != first:      # ეს პირველი რიცხვის გამოყოფთა ჯამი, არაა ტოლი ამავე ჯამის გამყოფთა ჯამის მაშინ ვამატებთ სიაში
        answer.append(i)

print(sum(answer)) 

