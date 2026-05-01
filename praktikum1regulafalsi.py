import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 - x - 2

print("=" * 55)
print("   PROGRAM METODE REGULA FALSI - AKAR PERSAMAAN")
print("=" * 55)
print("  f(x) = x^3 - x - 2")
print("  Mencari akar persamaan dengan metode Regula Falsi")
print("=" * 55)

x1 = float(input("\nMasukkan nilai x1 (batas kiri): "))
x2 = float(input("Masukkan nilai x2 (batas kanan): "))
iterasi = int(input("Masukkan jumlah iterasi: "))

if f(x1) * f(x2) > 0:
    print("\n[!] f(x1) dan f(x2) bertanda sama!")
    print("    Tidak ada akar di interval ini, coba interval lain.")
else:
    hasil_iterasi = []
    x3_lama = None

    print("\n" + "=" * 110)
    print(f"{'Iterasi':<10} {'x1':<12} {'x2':<12} {'x3':<12} {'f(x3)':<12} {'Error Abs':<15} {'Error Rel':<15}")
    print("=" * 110)

    for i in range(1, iterasi + 1):
        x3 = x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1))
        fx3 = f(x3)

        if x3_lama is None:
            error_abs = 0
            error_rel = 0
        else:
            error_abs = abs(x3 - x3_lama)
            error_rel = abs((x3 - x3_lama) / x3)

        print(f"{i:<10} {x1:<12.6f} {x2:<12.6f} {x3:<12.6f} {fx3:<12.6f} {error_abs:<15.6f} {error_rel:<15.6f}")

        hasil_iterasi.append((x1, x2, x3))

        if fx3 == 0:
            break
        elif f(x1) * fx3 < 0:
            x2 = x3
        else:
            x1 = x3

        x3_lama = x3

    print("=" * 110)
    print(f"\n[✓] Estimasi akar setelah {iterasi} iterasi: x = {x3:.6f}")
    print(f"    f({x3:.6f}) = {fx3:.6f}")

    x_plot = np.linspace(x1 - 1, x2 + 1, 500)
    y_plot = f(x_plot)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.plot(x_plot, y_plot, 'b-', label='f(x) = x^3 - x - 2')
    ax1.axhline(0, color='k', linewidth=0.8)
    ax1.axvline(0, color='k', linewidth=0.8)
    ax1.set_title('Grafik f(x)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(x_plot, y_plot, 'b-', label='f(x) = x^3 - x - 2')
    ax2.axhline(0, color='k', linewidth=0.8)

    colors = ['red', 'green', 'orange', 'purple', 'brown']
    for idx, (a, b, c) in enumerate(hasil_iterasi):
        warna = colors[idx % len(colors)]
        ax2.plot([a, b], [f(a), f(b)], '--', color=warna, label=f'Iterasi {idx+1}')
        ax2.scatter([c], [0], color=warna, zorder=5)

    ax2.set_title('Proses Iterasi Regula Falsi')
    ax2.set_xlabel('x')
    ax2.set_ylabel('f(x)')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()
