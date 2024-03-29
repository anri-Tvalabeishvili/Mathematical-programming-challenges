import math as m
import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

answer = int(m.factorial(40) / (m.factorial(20) * m.factorial(20)))

print(answer)

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს

""" 
ესაა სუფთა სტატისტიკური ამოცანა, მინიშნება არის შემდეგი

ჩვენ გვაქვს 20 X 20  ბლოკი რომლის უკიდურესი მარცხენა მაღლა მდებარე ბლოკიდან უნდა ჩავიდეთ უკიდურეს მარჯვენა ქვედა ბლოკამდე. შესაბამისად ჩვენდა უნებურად უნდა გავიაროთ
20 ბლოკი მარჯვნივ და 20 ბლოკი ქვემოთ.
ანუ გვაინტერესებს ამ მარჯვენა-ქვემო მოძრაობის კომბინაციათა რაოდენობა (იგივე რაც რამდენი სხვადასხვა გზით შეგვიძლია მივიდეთ დანიშნულების ადგილამდე)

ამიტომ ვიყენებთ "ჯუფდების" ფორმულას რომელშიც არააქ მნიშვნელობა რა თანმიმდევრობით შესრულდება მოვლენა, მთავარია რამდენი განსხვავებული სახის მოველნა შეიძლება მოხდეს


"""