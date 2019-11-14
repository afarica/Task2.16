# If you were on the moon now, your weight will be 16,5% of your earth weight.
# To calculate it you have to multiple to 0,165. If next 15 years your weight will
# increase 1 kg each year. What will be your weight each year on the moon next
# 15 years?
your_weight=float(input("Enter your weight:"))
years=int(input("How many years:"))
on_the_moon=your_weight*0.165
for x in range(0,years+1):
	y=x*0.165+on_the_moon
	print(y)
