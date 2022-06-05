while True:
    print("AKIM İÇİN 0"
          " GERİLİM İÇİN 1"
          " DİRENÇ İÇİN 2"
          " ÇIKMAK İÇİN Q")
    soru = input("Hangi Değeri Hesaplamak istiyorsunuz ?:")

    if soru == "0":
        gerilim = float(input("Gerilim Değeri:"))
        direnc = float(input("Direnç Değeri:"))
        print("Akım Değeri =",(gerilim/direnc),"I")

    elif soru == "1":
        akım = float(input("Akım Değeri:"))
        direnc = float(input("Direnç Değeri: "))
        print("Gerilim Değeri =",(akım*direnc),"V")


    elif soru == "2":
        akım = float(input("Akım Değeri:"))
        gerilim = float(input("Gerilim Değeri:"))
        print("Direnç Değeri = ",(gerilim/akım),"ohm")


    elif soru == "Q" or "Q":
        break





