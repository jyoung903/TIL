univ = ["연대", "고대", "서울대"]
univ.append("포스텍")
print(univ)
univ.insert(1, "독일")
print(univ)

# 함수 가변인자 사용
def profile(name,age, *langauge):
    print("name: {0}\tage: {1}\t" .format(name, age), end = " ")

    for lan in langauge:
        print(lan, end = " ")
    print()
profile("푸름", 22, "python", "c")


def std_weight(height, gender):
    if gender == "male":
        return (height * 0.01)**2 * 22
    else :
        return (height * 0.01)**2 * 21
height = 175
gender = "female"

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
    # print(line, end="") # 별도 줄바꿈 방지

# n1 = int(input())
# for i in range(1, n1+1):
#     if(i%10==3)|(i%10==6)|(i%10==9):
#         print("X", end=' ')
#     else:2
#         print(i, end=" ")

# a, d, n = map(int,input().split())
# print(a,d,n) # print = (a,d,n)으로 적었었네ㅎ
# n2 = a + (n-1)*d
# print("n2: ", n2)

d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
print(d)

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end='')
    print()

n = int(input())
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end='')
    print()

