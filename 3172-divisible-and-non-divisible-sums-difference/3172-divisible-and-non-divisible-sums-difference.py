class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1 = sum2 = 0
        totalSum = (n*(n+1))//2
        # for i in range(1,n+1):
        #     if i%m != 0:
        #         sum1 += i
        #     else:
        #         sum2 += i
        mul = 0
        while mul+m <= n:
            mul +=m
            sum2 +=mul
            #mul += 1
        sum1 = totalSum-sum2
        #print(totalSum,sum1,sum2)
        return (sum1-sum2)


        