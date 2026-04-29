import math

def buat_fungsi(expr):
    def f(x):
        return eval(expr, {"__builtins__": None}, {
            "x": x,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "exp": math.exp,
            "log": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e
        })
    return f

print("=" * 80)
print("PROGRAM PENCARIAN AKAR PERSAMAAN - METODE SECANT")
print("=" * 80)

print("Contoh fungsi:")
print("  x**3 - x - 2")
print("  cos(x) - x")
print("  exp(-x) - x")
print("-" * 80)

fungsi_input = input("Masukkan fungsi f(x): ")
x0 = float(input("Masukkan nilai awal x0: "))
x1 = float(input("Masukkan nilai awal x1: "))
maks_iterasi = int(input("Masukkan jumlah iterasi maksimum: "))
toleransi = float(input("Masukkan toleransi error, contoh 0.000001: "))

f = buat_fungsi(fungsi_input)

print("\n" + "=" * 95)
print(f"{'Iterasi':<10}{'x0':<15}{'x1':<15}{'x2':<15}{'f(x2)':<15}{'Error':<15}")
print("=" * 95)

akar = None

for i in range(1, maks_iterasi + 1):
    fx0 = f(x0)
    fx1 = f(x1)

    if fx1 - fx0 == 0:
        print("Perhitungan berhenti karena terjadi pembagian dengan nol.")
        break

    x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
    fx2 = f(x2)
    error = abs(x2 - x1)

    print(f"{i:<10}{x0:<15.6f}{x1:<15.6f}{x2:<15.6f}{fx2:<15.6f}{error:<15.6f}")

    if error < toleransi or abs(fx2) < toleransi:
        akar = x2
        break

    x0 = x1
    x1 = x2
    akar = x2

print("=" * 95)

if akar is not None:
    print(f"[✓] Estimasi akar persamaan: x = {akar:.6f}")
    print(f"[✓] Nilai f(x): {f(akar):.6f}")
else:
    print("[!] Akar belum ditemukan.")
