#!/usr/bin/python3
import calculator_1

a = 10
b = 5

result_add = calculator_1.add(a, b)
result_sub = calculator_1.sub(a, b)
result_mul = calculator_1.mul(a, b)
result_div = calculator_1.div(a, b)

print(f"{a} + {b} = {result_add}")
print(f"{a} - {b} = {result_sub}")
print(f"{a} * {b} = {result_mul}")
print(f"{a} / {b} = {result_div}")
