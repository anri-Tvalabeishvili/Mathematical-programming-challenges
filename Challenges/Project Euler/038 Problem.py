import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

# ვქმნით ცვლადს სადაც შევინახავთ უდიდეს Pandigital multiples-ს
largest = 0

# ციკლს ვწერთ 10**4 რადგან შემდეგ აზრს კარგავს
for i in range(1,10000):
	
	# ვქმნით დროებით ცვლადს სადაც შევინახავთ ნამრავლის შედეგებს
	multiplication = ''
	
	# ვქმნით მუდმივ მამრავლს რომელიც ნელ-ნელა გაიზრდება
	integer = 1
	
	# სანამ ნამრავლის შედეგების სტრინგული ჯამი ნაკლები იქნება 9-ზე მანმადე ვაგრძელებთ თითოეულ ციკლს
	while len(multiplication) < 9:
		
		# ყოველ ჯერზე ვამატებთ არსებული რიცხვის ნამრავლს მუდმივ მამრავლზე 
		multiplication += str(i*integer)
		
		# მუდმივი მამრავლი გავწარდოთ 1-ით
		integer += 1
		
	# ვამოწმებთ არის თი არა მიღებული პასუხის სიგრძე 9
	# ვამოწმებთ ნამდვილად არისს თუ არა მიღებულ პასუხში 9-სხვადასხვა ციფრი
	# და ვამოწმებთ იმას რომ ნული არ შეგვებაპროს 
	if ((len(multiplication) == 9) and (len(set(multiplication)) == 9) 
		and ('0' not in multiplication)):
	
		# და ბოლოს თუ არსებული რიცხვი მეტი იქნება წინად მიღებულ რიცხვზე, წინა რიცხვს ვცვლით ახალი რიცხვით
		if int(multiplication) > largest:
			largest = int(multiplication)



print (largest) # ვპრინტავთ მიღებულ პასუხს

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს