"""Chương trình từ điển Anh_Việt"""
f_AV=open("/Users/nguyenhongdieuanh/Bài tập/TuDien_AnhViet_A.txt",mode='r',encoding='utf-8')
tracuu=input("Nhập từ cần tra cứu:")
while True:#Định vị tìm đến dòng cần tra cứu
    dong=f_AV.readline()
    if dong.startswith("@"+tracuu):
        print(dong[1:].strip())#in dòng từ tra cứu+phiên âm
        #in các dòng giải thích cho từ tra cứu
        while True:
             dong=f_AV.readline()
             if dong[0]=='@':
                 break
             else:
                print(dong.replace('\n',''))
            
        break
    if dong=="":
        print("Không tìm thấy từ",tracuu)
        break
        
f_AV.close()
