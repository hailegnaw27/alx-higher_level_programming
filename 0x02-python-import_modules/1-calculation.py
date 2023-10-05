#!/usr/bin/python3
import calculator_1

a = 10
b = 5

result_add = calculator_1.add(a, b)
result_sub = calculator_1.sub(a, b)
result_mul = calculator_1.mul(a, b)
result_div = calculator_1.div(a, b)

output = f"{a} + {b} = {result_add}\n{a} - {b} = {result_sub}\n{a} * {b} = {result_mul}\n{a} / {b} = {result_div}"
print(output, end='')
