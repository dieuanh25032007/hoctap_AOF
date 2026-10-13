"""Chương trình từ điển Anh_Việt"""
f_AV=open("/Users/nguyenhongdieuanh/Bài tập/TuDien_AnhViet_A.txt",mode='r',encoding='utf-8')
tracuu=input("Nhập từ cần tra cứu:")
while True:#Định vị tìm đến dòng cần tra cứu
    dong=f_AV.readline()
    if dong.startswith("@"+tracuu):
        print(dong[1:])
        break
    if dong=="":
        print("Không tìm thấy từ",tracuu)
        break
        
f_AV.close()
