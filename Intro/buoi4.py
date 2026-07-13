# Có 5 kiểu đối số trong python
# Đối số vị trí
def fun(name, job):
    print(name, "is a", job)
fun("Hoàng", "Algoict")
# Đối số từ khóa
fun(job="Algoict", name="Hoàng")
# Đối số vị trí và đối số từ khóa
def func(name, job, location):
    print(name, "is a", job, "in", location)
func("Hoàng", location="SYDNEY", job="Algoict")
# Đối số mặc định
def func1(name, job="Al engineer"):
    print(name, "is a", job)
func1("Hoàng", "coder")
func1("Hoàng")
# sorted() sắp xếp giá trị tăng dần
sorted([1,5,2,4,6])
print(sorted([1,5,2,4,6]))
# có reverse thì sẽ giảm dần
print(sorted([1,5,2,4,6],reverse=True))
# Hàm in dãy range()

