'''
5 * 5 내에서 특정 좌표를 기준으로 회전 시계방향 90, 180, 270
유물 획득 (같은 숫자가 3개 이상 연결된 경우) -> BFS(??), DFS(??) -> 좌표 찾아야 함
회전 우선순위 1. 유물 획득 가치 최대화
           2. 회전 횟수 최소
           3. 회전축 열이 적은 순
           4. 회전축 행이 적은 순
5 * 5 사이즈는 정해져 있으니 회전 축은
(2,2), (2,3), (2,4)
(3,2), (3,3), (3,4)
(4,2), (4,3), (4,4)

유물 획득 후 빈자리를 채워야 함.
빈자리를 채우는 기준은 1. 열 번호 적은 순, 2 행 번호 큰 순
좌측 하단부터 우측 방향으로...

이거를 K번 반복 -> 유물 획득 안되면 종료
뭉텅이 합계가 가치(333, 4444) -> 7

2 20
7 6 7 6 7
6 7 6 7 6
6 7 1 5 4
7 6 3 2 1
5 4 3 2 7
3 2 3 5 2 4 6 1 3 2 5 6 2 1 5 6 7 1 2 3

'''

'''
탐사 진행(K)
1. 최대 카운트 찾기
- 회전 횟수(90,180,270)
- 중심축 (열, 행)
- 회전-> 카운트 -> 비교 및 갱신

연쇄 획득(무한 루프)
- 카운트 없으면 끝
'''
def rotate(arr, si, sj):    # 90도 시계방향 회전
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j]=arr[si+3-j-1][sj+i]
    return narr

def bfs(arr,v,si,sj,clr):
    q = []
    sset = set()
    cnt = 0

    q.append((si,sj))
    v[si][sj]=1
    sset.add((si,sj))
    cnt+=1

    while q:
        ci,cj = q.pop(0)
        # 네방향, 범위내, 미방문, 조건: 같은 값이면
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj]==0 and arr[ci][cj]==arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj]=1
                sset.add((ni,nj))
                cnt+=1

    if cnt>=3:      # 유물이면: cnt 리턴 + clr==1이면 0으로 clear
        if clr==1:  # 0으로 초기화
            for i,j in sset:
                arr[i][j]=0
        return cnt
    else:           # 3개 미만이면 0리턴
        return 0

def count_clear(arr, clr):  # clr==1인 경우 3개이상값들을 0으로 clear
    v = [[0]*5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):  # 미방문인 경우 같은 값이면 fill
            if v[i][j]==0:
                # 같은 값이면, 3개 이상인 경우
                t = bfs(arr,v,i,j,clr)
                cnt+=t
    return cnt

K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split()))
ans = []

for k in range(K):  # K턴을 진행(유물이 없는 경우 즉시종료)
    #[1] 탐사진행
    mx_cnt = 0
    for rot in range(1, 4):     # 회전수->열->행 (작은순)
        for sj in range(3):
            for si in range(3):
                # rot 회수만큼 90도 시계방향 회전 => narr
                narr = [x[:] for x in arr]
                for _ in range(rot):
                    narr = rotate(narr, si, sj)

                # 유무개수 카운트
                t = count_clear(narr, 0)
                if mx_cnt < t:      # 최대개수
                    mx_cnt = t
                    marr = narr
    # 유물이 없는 경우 턴 즉시종료
    if mx_cnt==0:
        break
    #[2] 연쇄획득
    cnt = 0
    arr = marr
    while True:
        t = count_clear(arr, 1)
        if t==0:
            break   # 연쇄획득 종료 => 다음 턴으로..
        cnt += t    # 획득한 유물 개수 누적

        # arr의 0값인 부분 리스트에서 순서대로 추가
        for j in range(5):
            for i in range(4,-1,-1):
                if arr[i][j]==0:
                    arr[i][j]=lst.pop(0)

    ans.append(cnt) # 이번턴 연쇄획득한 개수 추가
print(*ans)