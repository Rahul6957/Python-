import gc
import sys

class Student:
    def __del__(self):
        print("Student object destroyed")


s1 = Student()

print(sys.getrefcount(s1))  # 2

student2 = Student

print(sys.getrefcount(s1))
del s1
#print(sys.getrefcount(s1))
gc.collect()