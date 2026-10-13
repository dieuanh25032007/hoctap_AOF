"""Chương trình từ điển Anh_Việt
V4: Bổ sung:
-từ tra cứu chữ hoa/thường đều hiểu như nhau
-Khi trả lời có/không bằng chữ hoa/thường đều hiểu như
-Sửa lỗi:Phải tìm đúng từ cần tra,không tìm từ gần
-Chuyển các dòng loại từ về chữ hoa(Dòng có dấu * ở đầu dòng)
-Bổ sung nét gạch đúp ở đầu và cuối phần tra từ ==========
-Bổ sung dòng trống ở phía trên mỗi dòng LOẠI TỪ
"""
while True:
    f_AV=open("/Users/nguyenhongdieuanh/Bài tập/TuDien_AnhViet_A.txt",mode='r',encoding='utf-8')
    tracuu=input("Nhập từ cần tra cứu:").lower()
    print("=====================================================================")
    while True:#Định vị tìm đến dòng cần tra cứu
        dong=f_AV.readline()
        if dong.startswith("@"+tracuu+" /"):
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
           
