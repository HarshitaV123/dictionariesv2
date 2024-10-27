numinput=input("Enter a number: ")
numchart={
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    "0":0

}
for num in numinput:
    if num in numchart:
        numchart[num]+=1
pangram=True
for count in numchart.values():
    if count<=0:
        pangram=False
if pangram:
    print("This number is a pangram")
else:
    print("This number is not a pangram")