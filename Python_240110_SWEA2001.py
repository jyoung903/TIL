# SW Expert Academy 2001 파리 퇴치
'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.

죽은 파리의 개수를 구하라!

예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.
[제약 사항]

1. N 은 5 이상 15 이하이다.

2. M은 2 이상 N 이하이다.

3. 각 영역의 파리 갯수는 30 이하 이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,

다음 N 줄에 걸쳐 N x N 배열이 주어진다.
10
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
...

[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
#1 49
#2 159
...
'''
# 5&2 : 4, 5&3 : 3, 5&4 : 2
# 1 - 런타임 에러 : readline() 써서 그런 듯!
from sys import stdin as s
s = open("input_2001.txt","rt")
for i in range(int(s.readline())):
    N, M = map(int, s.readline().split())
    #board = []
    #dead = []
    #kill = 0
    m = 0
    # for j in range(N):
    #     board.append([])
    #     for j2 in range(N):
    #         board[j].append(0)
    # for k in range(N):
    #     a = s.readline().split()
    #     for l in range(N):
    #         board[k][l] = int(a[l])
    board = [list(map(int, s.readline().split())) for _ in range(N)]
    for j in range((N+1)-M):
        for k in range((N+1)-M):
            kill = 0
            for x in range(M):
                for y in range(M):
                    kill += board[x+j][y+k]
            #dead.append(kill)
            if kill > m:
                m = kill
    
    print('#{} {}'.format(i+1,m))
    #print("#"+str(i+1),max(dead))

'''
최근 commit을 취소하고 강제 push하기
이미 커밋을 push한 상태에서 커밋을 수정하고 싶은데,
커밋을 다시만들어 보내자니 히스토리가 지저분해지는게 싫었다.

이럴때는 커밋을 취소하고 강제로 push해주어 커밋도 수정하고 히스토리도 깔끔하게 관리할 수 있다.

이때 커밋을 취소해주면 해당 커밋의 변경파일은 다시 untrackted 상태로 돌아간다.
그 다음 새롭게 git add를 해주어 새로운 commit을 만들고 강제로 push해주는 것이다.

이때 한번에 여러 커밋을 취소하고 싶다면 ~로 취소하고 싶은 개수를 적어주면 된다


$ git reset "HEAD^" #가장 최신 커밋 취소
$ git reset "HEAD~3" #최신 커밋 3개 취소

$ git push origin master -f #master brench에 강제로 push
(이때 -f 대신 branch이름 앞에 +기호를 붙여 다른 branch로 push할 수 있다)

[출처] https://velog.io/@jollyn/Git-%EC%BB%A4%EB%B0%8B%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0
'''
            

