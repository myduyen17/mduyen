# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:20:54 2024

@author: Student
"""

distance=float(input("Nhập độ dài đoạn đường đến tường (m):"))
if distance <   500    :
    print("Đường đến trường quá gần.Thôi ! Đi bộ")
elif distance>1200  :
    print("Đường đến trường quá xa.Thôi ! Đi xe máy")
elif distance >= 500 and distance <= 1000   :
    print("Đường đến trường không xa. Thôi ! Đi xe đạp ")
else:
        print("Không xác định")


    