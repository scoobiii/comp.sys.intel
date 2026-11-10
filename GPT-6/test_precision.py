from fractions import Fraction
from decimal import Decimal, localcontext
import platform
import sys

print("GPT-6 NUMERICAL INTEGRITY")
print("Version: 1.1.0")
print("Platform:", platform.platform())
print("Python:", sys.version)

x = 4195835.0
y = 3145727.0

q = x / y
product = q * y
residual = x - product

# Referência racional exata dos operandos
exact_x = Fraction(4195835)
exact_y = Fraction(3145727)
exact_q = exact_x / exact_y

# Referência decimal de alta precisão
with localcontext() as ctx:
    ctx.prec = 80
    dx = Decimal(4195835)
    dy = Decimal(3145727)
    reference = dx / dy

print("\n=== FDIV ===")
print("Quotient binary64:", format(q, ".17g"))
print("Residual binary64:", format(residual, ".17g"))
print("Exact rational quotient:", exact_q)
print("Decimal reference:", reference)

# Erro da representação binary64 do quociente
binary_q = Fraction.from_float(q)
error = abs(binary_q - exact_q)

print("Absolute quotient error:", float(error))
print("Relative quotient error:",
      float(error / abs(exact_q)))

print("\n=== RECIPROCAL ===")
n = 824633702441.0
p = n * (1.0 / n)

print("Product:", format(p, ".17g"))
print("Deviation from 1:", format(abs(p - 1.0), ".17g"))

print("\n=== FLOAT ACCUMULATION ===")
total = sum([0.00001] * 1_000_000)
print("Accumulation:", format(total, ".17g"))
print("Error:", format(abs(total - 10.0), ".17g"))

print("\nPASS: calculations executed.")
print("NOTE: PASS does not certify hardware integrity.")
