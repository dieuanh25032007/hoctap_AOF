'''
Bổ sung chức năng tra cứu từ điển tiếng việt sang tiếng anh
'''
def tracuu(loaitudien): #nhận 1 trong 2 giá trị AV hoặc VA
    while True:
        if loaitudien=="AV":
            f_AV=open("/Users/nguyenhongdieuanh/Bài tập/TuDien_AnhViet_A.txt",mode='r',encoding='utf-8')
        else:
            f_AV=open("/Users/nguyenhongdieuanh/Bài tập/TuDien_VietAnh(23460 tu).txt",mode='r',encoding='utf-8')
        while True:
            if loaitudien=="AV":
                tracuu=input("Nhập từ Tiếng Anh cần tra cứu:").lower()
            else:
                tracuu=input("Nhập từ tiếng Việt cần tra cứu:").lower()
            if tracuu.replace(" ","").isalpha():
                break
            else:
                print("Từ tra cứu phải là chữ cái")
        print("=====================================================================")
        while True:#Định vị tìm đến dòng cần tra cứu
            dong=f_AV.readline()
            if (loaitudien == "AV" and dong.lower().startswith("@"+t+tracuu+" /")) or (loaitudien == "VA" and dong.rstrip().lower() == "@"+tracuu):
                print(dong[1:].strip())#in dòng từ tra cứu+phiên âm
                #in các dòng giải thích cho từ tra cứu
                while True:
                     dong=f_AV.readline()
                     if dong[0]=='@':
                         break
                     else:
                        if dong[0]=='*':
                            print()
                            print(dong.upper().strip()) #Dòng loại từ
                        else:
                            print(dong.strip())
                print("=====================================================================")

                    
                break
            if dong=="":
                print("Không tìm thấy từ",tracuu)
                break
                
        f_AV.close()
        while True:
            traloi=input("Bạn có muốn tiếp tục không?(C/K)")
            dstrlko=['ko','k','không','no','n']
            dstrlco=['co','c','có','yes','y']
            if traloi.lower() in dstrlko:
                print("Cảm ơn bạn đã sử dụng chương trình")
                break
            if traloi.lower() in dstrlco:
                break
            else:
                print("Bạn cần trả lời nghiêm túc")
        if traloi.lower() in dstrlko:
            break
#Thân chính chương trình:
print("1.Anh-Việt")
print("2.Việt-Anh")
chon=int(input("Nhập lựa chọn của bạn:"))
if chon==1:
    tracuu("AV")
elif chon==2:
    tracuu("VA")
else:
    print("Lựa chọn ko hợp lệ")
               


