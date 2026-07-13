"""
    Đội Manchester United tham gia giải ngoài hạng anh.
    Yêu cầu người dùng nhập vào lần lượt 3 số tự nhiên
    tương ứng với số trận thắng, hòa, thua của đội.
    Quy tắc tính điểm như sau:
    - Mỗi trận thắng đội sẽ được 3 điểm
    - Mỗi trận hòa đội sẽ được 1 điểm
    - Mỗi trận thua đội sẽ không được điểm nào
    Tính số điểm đội có được
"""
w,l,d=map(int,input("Enter the number of win games,lose and draw in a line:").split())
points=w*3+d
print("Total points:",points)