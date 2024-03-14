# 연습문제 1
print("100")
print(100)
print(50+50)
print("50+50") ## 결과 다르게 나옴

# 연습문제 2
print('%d / 8d= 20' % (5, 10, 5/10))

# 연습문제 3
print("%04d" % 876)
print("%5s" % "CookBook")
print("%1.1f" % 123.45)

# 연습문제 4
print ("{2:d} {0:d} {1:d]".format (111, 222, 333))

# 연습문제 10
# (1) 2진수 0011
int(0b0011)
# (2) 2진수 01010
int(0b01010)
# (3) 16진수11
int(0x11)
# (4) 8진수 17
int(0o17)

# 연습문제 11
# (1) 1011(2진수)
int(0b1011)
# (2) 1A (16진수)
int(0x1A)

# 연습문제 13
# (1) int('1002', 2)   ## 오류 발생: 1002 가 2 진수가 아님
# (2) int('1008', 8)   ## 오류 발생: 1008 이 8 진수가 아님
# (3) int('AAFG', 16)  ## 오류 발생: G 는 16 진수가 아님

# 연습문제 15
num =  12345678
hex_num = hex(num)
oct_num = oct(num)
bin_num = bin(num)
print("10진수 =>", num)
print("16진수 =>", hex_num)
print(" 8진수 =>", oct_num)
print(" 2진수 =>", bin_num)
