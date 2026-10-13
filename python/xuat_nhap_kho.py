import os
duongdan='/Users/nguyenhongdieuanh/Bài tập/vatuton.txt'
while True:
    try:
        print("1.Kiểm tra số lượng")
        print("2.Nhập thêm số lượng vật tư")
        print("3.Xuất số lượng vật tư")
        print("4.Kết thúc")
        chon=int(input("Nhập lựa chọn của bạn:"))
        if chon==1:
            f=open(duongdan,mode="r",encoding="utf-8")
            soluong=int(f.read())
            f.close()
            print(f"Số lượng vật tư hiện tại:{soluong}")
        elif chon==2:
            f=open(duongdan,mode="r",encoding="utf-8")
            soluong=int(f.read())
            f.close()
            them=int(input("Nhập số lượng vật tư muốn thêm:"))
            if them>0:
                soluong=soluong+them
                f=open(duongdan,mode="w",encoding="utf-8")
                f.write(str(soluong))
                f.close()
                print(f"Số lượng vật tư hiện tại là:{soluong}")
            else:
                print("Số lượng thêm vào phải >0")
        elif chon==3:
            f=open(duongdan,mode="r",encoding="utf-8")
            soluong=int(f.read())
            f.close()
            xuat=int(input("Nhập số lượng vật tư muốn xuất:"))
            if xuat<0:
                print("Số lượng xuất phải > 0")
            elif xuat>soluong:
                print("Không đủ số lượng để xuất")
            else:
                soluong=soluong-xuat
                f=open(duongdan,mode="w",encoding="utf-8")
                f.write(str(soluong))
                f.close()
                print(f"Số lượng vật tư hiện tại:{soluong}")
        elif chon==4:
             print("Kết thúc chương trình")
             break
        else:
            print("Bạn phải nhập từ 1 đến 4")
    except FileNotFoundError:
        print("Không tìm thấy file vatuton.txt")
    except ValueError as e:
        print("Lỗi",e)
          
