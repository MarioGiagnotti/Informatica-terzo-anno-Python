import numpy as np
import matplotlib.pyplot as plt

# === INPUT UTENTE ===
ampiezza = float(input("Inserisci l'ampiezza: "))
frequenza = float(input("Inserisci la frequenza [Hz]: "))
fase_gradi = float(input("Inserisci la fase [gradi]: "))
durata = float(input("Inserisci la durata [secondi]: "))

# Verifica numero livelli valido
while True:
    livelli = int(input("Inserisci il numero di livelli di quantizzazione (potenza di 2): "))
    if livelli > 1 and (livelli & (livelli - 1)) == 0:
        break
    print("⚠️ Deve essere una potenza di 2 (es. 2, 4, 8, 16...).")

# === PARAMETRI ===
fs = 10  # campioni al secondo (puoi aumentarlo)
fase_rad = np.deg2rad(fase_gradi)
t = np.linspace(0, durata, int(fs * durata), endpoint=False)

# === SEGNALI ===
# Segnale originale continuo
segnale = ampiezza * np.cos(2 * np.pi * frequenza * t + fase_rad)

# Quantizzazione
segnale_min = np.min(segnale)
segnale_max = np.max(segnale)
segnale_norm = (segnale - segnale_min) / (segnale_max - segnale_min)
segnale_quantizzato = np.round(segnale_norm * (livelli - 1)).astype(int)

# Converti in binario
bit_per_sample = int(np.log2(livelli))
bitstream = [format(val, f'0{bit_per_sample}b') for val in segnale_quantizzato]

# === GRAFICI ===
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# 1. Segnale continuo
t_cont = np.linspace(0, durata, 1000)
y_cont = ampiezza * np.cos(2 * np.pi * frequenza * t_cont + fase_rad)
axs[0].plot(t_cont, y_cont, label='Segnale y(t)')
axs[0].set_title("Segnale continuo y(t) = A·cos(2πft + fase)")
axs[0].grid()
axs[0].legend()

# 2. Campioni (con cerchi e valori)
axs[1].plot(t, segnale, 'o', color='red', label='Campioni')
for i in range(len(t)):
    axs[1].text(t[i], segnale[i], f"{segnale[i]:.2f}", ha='center', va='bottom')
axs[1].set_title("Campioni del segnale (con valori)")
axs[1].grid()
axs[1].legend()

# 3. Quantizzazione (step costanti)
valori_quant = (segnale_quantizzato / (livelli - 1)) * (segnale_max - segnale_min) + segnale_min
t_step = np.repeat(t, 2)[1:]
valori_step = np.repeat(valori_quant, 2)[:-1]
axs[2].plot(t_step, valori_step, drawstyle='steps-post', label='Quantizzazione')
for i in range(len(t)):
    axs[2].text(t[i], valori_quant[i], f"{valori_quant[i]:.2f}", ha='center', va='bottom')
axs[2].set_title("Segnale quantizzato (a livelli costanti)")
axs[2].grid()
axs[2].legend()

plt.xlabel("Tempo [s]")
plt.tight_layout()
plt.show()

# === STAMPA ===
print("\nSequenza di bit:")
print(" ".join(bitstream))
