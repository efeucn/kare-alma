num = float(input("Karesinin alinmasini istediginiz degeri giriniz:\n"))
squared = num**2
if squared%1== 0:
    squared = int(squared)
print(f"Girdiginiz sayinin karesi {squared}'dir")