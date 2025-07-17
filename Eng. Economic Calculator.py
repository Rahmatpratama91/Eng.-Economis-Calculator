import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

# Fungsi mencari Present Value
def present_value(future_value, interest_rate, n_periods):
    return future_value / ((1 + interest_rate) ** n_periods)

# Fungsi mencari Future Value
def future_value(present_value, interest_rate, n_periods):
    return present_value * ((1 + interest_rate) ** n_periods)

# Fungsi mencari NPV
def npv(cash_flows, interest_rate):
    return sum(cf / (1 + interest_rate) ** i for i, cf in enumerate(cash_flows))

# Fungsi mencari IRR
def irr(cash_flows):
    return npf.irr(cash_flows)

# Input contoh
cash_flows = [-10000, 3000, 4000, 5000, 3000, 5000, 6000, 2000]
rate = 0.15  # 15%

# Hitung nilai sekarang per tahun
present_values = [cf / (1 + rate) ** i for i, cf in enumerate(cash_flows)]
years = list(range(len(cash_flows)))

# Visualisasi
plt.figure(figsize=(10, 6))
plt.plot(years, cash_flows, marker='o', label='Cash Flow')
plt.plot(years, present_values, marker='s', linestyle='--', label='Present Value')
plt.axhline(0, color='gray', linewidth=1)
plt.title('Cash Flow dan Present Value per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah (Rp)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Output hasil hitung
print("NPV:", round(npv(cash_flows, rate), 2))
print("IRR:", round(irr(cash_flows) * 100, 2), "%")
print("PV dari 5000 dalam 3 tahun:", round(present_value(5000, rate, 3), 2))
print("FV dari 3000 dalam 8 tahun:", round(future_value(3000, rate, 8), 2))