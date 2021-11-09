mahsulotlar = ['sabzi', 'piyoz','kartoshka','tuz','yog\'','guruch','choy','kofee','sholg\'om','anor','uzum','olma']
savat = []
d = input(" 5 ta mahsulot nomini kiriting")
for i in range(0,5):
    print(f"mahsulot nomini kiriting")
    savat.append(input(d))
if savat:
        for mah in mahsulotlar:
            if mah in savat:
                print(f"bizda {mah} mavjud")
            else:
                print(f"bizda bunday {mah} mahsulot yoq")