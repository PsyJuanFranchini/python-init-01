score = input("Enter Score:")
try:
    scr = float(score)
except:
    print("Please write a socre between 0.0 and 1.0")
    input("Press enter to exit")
if scr >= 0.9:
    print("A")
elif scr >= 0.8:
    print("B")
elif scr >=0.7:
    print("C")
elif scr >=0.6:
    print("D")
else:
    print("E")
input("Press enter to exit")
