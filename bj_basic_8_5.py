#5

num = int(input())

for i in range(num):
    H, W, N = map(int, input().split())
    fun1 = N%H
    fun2 = N//H + 1
    if fun1 == 0:
        fun1 = H
        fun2 -= 1
    print(fun1 * 100 + fun2)


#6

Test = int(input())

for _ in range(Test):
    k = int(input())
    n = int(input())
    base = [j for j in range(1, n+1)] # base(0층)은 입력 받는 값보다 1만 많으면 모든값을 찾을 수 있음.
    #  base = for j in range(1, n+1):
    #
    for l in range(k): # 층마다 반복
        for m in range(1, n): # 가장 아래층의 층부터 갱신을 시작하여 base = [1, 2, 3, 4...] 와 같이 0층부터 갱신을 시작한다.
            base[m] += base[m-1] # 피보나치 수열과 비슷한 개념 그전에 값을 지금 값에 더하여 값을 갱신
    print(base[n-1]) # base를 계속하여 갱신하여 그 값을 획득 base의 인덱스 처리이기때문에 0부터시작


#7


Test = int(input())

dis = 0

for i in range(Test):
    start, end = map(int, input().split())
    dis = end - start
    n = 0

    while True:
        if dis <= n*(n+1):
            break
        n += 1

    if dis <= n*n:
        print(2*n - 1)

    else:
        print(2*n)
