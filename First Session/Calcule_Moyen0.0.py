intero_1 = float(input("Interrogation1 Mark : "))
intero_2 = float(input("Interrogation2 Mark : "))
control = float(input("control Mark : "))
moyen = (intero_1 + intero_2 + control) / 3
if moyen < 10:
    print(f"Your mark is : {moyen} ==> راسب ")
elif moyen >= 10 and moyen < 12:
    print(f"Your mark is : {moyen} ==> حسن ")
elif moyen >= 12 and moyen < 14:
    print(f"Your mark is : {moyen} ==> جيد ")
elif moyen >= 14 and moyen < 16:
    print(f"Your mark is : {moyen} ==> جيد جدا")
elif moyen >= 16 and moyen < 18:
    print(f"Your mark is : {moyen} Execellent")
