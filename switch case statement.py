def Mesbah (choice):
    type={
       1:"Holy Quran",
       2:"Salat",
       3:"Roza",
       4:"Hazz",
       5:"ZaKat",
       6:"Kalema",
       7:"Doa ",
       8:"Sunnath",
       9:"Hadith",
       10:"Masala",
       11:"Fikah",
    }
    return type [choice]
print("Enter 1 to 11 any number: ")
m=int(input())
print(Mesbah(m))