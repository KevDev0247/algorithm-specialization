def karatsuba_algo(num1, num2):
    if len(str(num1)) == 1 or len(str(num2)) == 1:
        return num1 * num2
    else:
        n = max(len(str(num1)), len(str(num2))) // 2

        a = num1 // 10**n
        b = num1 % 10**n
        c = num2 // 10**n
        d = num2 % 10**n

        ac = karatsuba_algo(a, c)
        bd = karatsuba_algo(b, d)
        sum_ab_sum_cd = karatsuba_algo(a + b, c + d)

        ad_bc = sum_ab_sum_cd - ac - bd
        
        return 10**(n*2) * ac + 10**n * ad_bc + bd


num_1 = int(input())
num_2 = int(input())

print(karatsuba_algo(num_1, num_2))
