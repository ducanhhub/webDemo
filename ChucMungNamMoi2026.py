from datetime import date,timedelta 

today = date.today()
ngay_tet = date(2026,2,17)
if today >= ngay_tet:
    print("Chúc Mừng Năm Mới năm Bính Ngọ!")
    print("Chúc bạn vạn sự như ý, tỉ sự như mơ!!!")
else:
    print("Đang chờ đến tết...")
# next_day = x + timedelta(days=1)
# print(next_day.strftime("%d/%m/%Y"))17 