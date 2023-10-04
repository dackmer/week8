n = int(input("input "))
sum_result = sum(range(1, n + 1))
sum_expression = ' + '.join(map(str, range(1, n + 1)))
if 1 <= n <= 10000:
    print(f"{sum_result}({sum_expression})")
else:
    pass