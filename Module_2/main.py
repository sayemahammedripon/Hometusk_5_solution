print(20//6)
print(1+2+3)
print(5**2+2*5*9+(9**2))
#quotients
print(13//5)
#Remainder
print(13%5)
print('30//4'*2**2)
print('2*3//5*4')
print( 7%(5 // 2) )
#a)As a CEO of your company, you can have 20% of the company’s profit as your salary per month. Last year, from January to April the company purchased 30,000 BDT each month and sold 50,000 BDT products each month. From May to December purchased 20,000 BDT each month and sold out 45,000 BDT products each month. If you calculate your total salary for last year, how much it is?
#Last year january to april =4;total profit P=(50000-30000)*4 ,and may to december total profit (45000-20000)*8;total salary S=(P*20)/100
P=(((50000-30000)*4)+((45000-20000)*8));S=((P*20)/100)
print(P)
print(S)
#b)Suppose, Last year in June, Sylhet had a rainfall of 20cm, Chattogram had 40cm, Dhaka 35 cm. But, Bogura had only 20mm. If, Sylhet, Chattogram and Dhaka decreased by 5cm of rainfall every next month till October and Bogura increased by 2cm every next month till October, then calculate the total rainfall of each area at the end of October.
#june rainfall sylhet=20cm,chattagram=40cm,Dhaka=35cm ,Bogra=20mm=20/10=2cm
#Chattogram had 40cm, Dhaka 35 cm. But, Bogura had only 20mm. If, Sylhet, Chattogram and Dhaka decreased by 5cm of rainfall every next month till October and Bogura increased by 2cm
#till Octobor Sylhet, Chattogram and Dhaka decreased by 5cm of rainfall,sylhet(S)=(20-(5*4)),Chattagram(C)=(40-(5*4)),Dhaka(D)=(35-(5*4)),Bogra increased 2cm B=2+(2*4) Octobor rainfall O=(S+C+D+B)
S=(20-(5*4));C=(40-(5*4));D=(35-(5*4));B=(2+(2*4))
Octobor=(S+C+D+B)
print(Octobor)
#c)Some bricks of 12cm (Length), 6cm (Width), and 2cm (height) size is used to build a wall of 100m2 Area. How many full bricks can be used to build the wall? (Hint: brick area = length x wide
Area_of_the_wall=(100);Brick_area=((12/100)*(6/100))
number_of_brick=int(Area_of_the_wall/Brick_area)
print(number_of_brick)
