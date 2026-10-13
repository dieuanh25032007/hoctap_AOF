import numpy as np
from datetime import datetime
def nhap_so_nguyen(ten):
    while True:
        try:
            return int(input())
        except:
            print(ten,"phải là số nguyên.Hãy nhập lại",ten,":")
def nhap_so_nguyen_duong(ten):
    while True:
        n=nhap_so_nguyen(ten)
        if n>0:
            return n
        else:
            print(ten,"phải là số nguyên dương.Hãy nhập lại",ten,":")
def ketthuc():
    while True:
            traloi=input("Bạn có muốn tiếp tục ko?").lower()
            dstrlko=['ko','k','không','no','n']
            dstrlco=['có','c','co','yes','y']
            if traloi in dstrlco:
                return True
            if traloi in dstrlko:
                return False
            else:
                print("Bạn phải chọn có hoặc không")
while True:
    print("Nhập số dòng:")
    n=nhap_so_nguyen_duong("n")
    print("Nhập số cột:")
    m=nhap_so_nguyen_duong("m")

    while True:
        print("Nhập a:")
        a=nhap_so_nguyen("a")
        print("Nhập b:")
        b=nhap_so_nguyen("b")
        if a<b:
            break
        else:
            print("a phải nhỏ hơn b")
    mt=np.random.randint(a,b+1,size=(n,m))
    print(mt)
    f = open("/Users/nguyenhongdieuanh/Bài tập/log.txt", mode="a", encoding="utf-8")

    f.write("Ngày giờ: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")
    f.write("m,n,a,b: " + str(m) + "," + str(n) + "," + str(a) + "," + str(b) + "\n")
    f.write("Ma trận:\n")
    f.write(str(mt) + "\n")
    f.write("\n")

    f.close()
    if not ketthuc():
        print("Cảm ơn bạn đã sử dụng chương trình")
        break
