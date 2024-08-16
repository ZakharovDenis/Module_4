import fake_math as fm
import true_math as tm

fake_math = fm.fake_divide
true_math = tm.true_divide

result1 = fake_math(69, 3)
result2 = fake_math(3, 0)
result3 = true_math(49, 7)
result4 = true_math(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
