'''
4 3 3
0 0 1 0
0 0 1 0
1 1 0 1
0 0 2 0
1 2 2 1 5
2 1 2 1 1
3 2 1 2 3
1 2
2 1
3 3

'''

'''
0 : 빈칸, 1 : 함정, 2: 벽

1. 기사 이동
- 상하좌우 중 하나
- 이동할려는 곳에 기사가 있으면 하나씩 밀림(연쇄)
- 하지만 만약 기사가 이동하려는 방향의 끝에 벽이 있다면 모든 기사는 이동할 수 없게 됩니다.
- 사라지면 응답 X

2. 대미지
- 밀려난 기사는 피해
- 이동한 곳에서 w*h 만큼 대미지
- 체력 = 체력 - 대미지  if 체력 == 0: ㅅ하망
- 밀렸더라도 밀쳐진 위치에 함정이 전혀 없다면 그 기사는 피해를 전혀 입지 않게 됨에 유의합니다.?
'''
#방향: 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [ 0, 1, 0,-1]

N, M, Q = map(int, input().split())
# 벽으로 둘러싸서, 범위체크 안하고, 범위밖으로 밀리지 않게 처리
arr = [[2]*(N+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(N)]+[[2]*(N+2)]
units = {}
init_k = [0]*(M+1)

for m in range(1, M+1):
    si,sj,h,w,k=map(int, input().split())
    units[m]=[si,sj,h,w,k]
    init_k[m]=k                 # 초기 체력 저장(ans 처리용)

def push_unit(start, dr):       # s를 밀고, 연쇄처리..
    q = []                      # push 후보를 저장
    pset = set()                # 이동 기사번호 저장
    damage = [0]*(M+1)          # 각 유닛별 데미지 누적

    q.append(start)             # 초기데이터 append
    pset.add(start)

    while q:
        cur = q.pop(0)          # q에서 데이터 한개 꺼냄
        ci,cj,h,w,k = units[cur]

        # 명령받은 방향진행, 벽이아니면, 겹치는 다른조각이면 => 큐에 삽입
        # 큐에서 빼낸 좌표를 탐색, 이동 가능한지 확인(벽이있으면 빠꾸)
        ni,nj=ci+di[dr], cj+dj[dr]
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if arr[i][j]==2:    # 벽!! => 모두 취소
                    return
                if arr[i][j]==1:    # 함정인 경우
                    damage[cur]+=1  # 데미지 누적

        # 겹치는 다른 유닛있는 경우 큐에 추가(모든 유닛 체크)
        for idx in units:
            if idx in pset: continue    # 이미 움직일 대상이면 체크할 필요없음

            ti,tj,th,tw,tk=units[idx]
            # 겹치는 경우
            if ni<=ti+th-1 and ni+h-1>=ti and tj<=nj+w-1 and nj<=tj+tw-1:
                q.append(idx)
                pset.add(idx)

    # 명령 받은 기사는 데미지 입지 않음
    damage[start]=0

    # 이동, 데미지가 체력이상이면 삭제처리
    for idx in pset:
        si,sj,h,w,k = units[idx]

        if k<=damage[idx]:  # 체력보다 더 큰 데미지면 삭제
            units.pop(idx)
        else:
            ni,nj=si+di[dr], sj+dj[dr]
            units[idx]=[ni,nj,h,w,k-damage[idx]]

for _ in range(Q):  # 명령 입력받고 처리(있는 유닛만 처리)
    idx, dr = map(int, input().split())
    if idx in units:
        push_unit(idx, dr)      # 명령받은 기사(연쇄적으로 밀기: 벽이 없는 경우)

ans = 0
for idx in units:
    ans += init_k[idx]-units[idx][4]
print(ans)



