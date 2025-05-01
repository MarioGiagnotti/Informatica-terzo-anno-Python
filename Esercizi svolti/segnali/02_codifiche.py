import matplotlib.pyplot as plt

def codifica_NRZ(bits):
    time, signal = [], []
    for i, bit in enumerate(bits):
        time += [i, i+1]
        signal += [1 if bit == '1' else 0] * 2
    return time, signal

def codifica_RZ(bits):
    time, signal = [], []
    for i, bit in enumerate(bits):
        time += [i, i+0.5, i+0.5, i+1]
        if bit == '1':
            signal += [1, 1, 0, 0]
        else:
            signal += [0, 0, 0, 0]
    return time, signal

def codifica_Manchester(bits):
    time, signal = [], []
    for i, bit in enumerate(bits):
        time += [i, i+0.5, i+0.5, i+1]
        if bit == '1':
            signal += [1, 1, 0, 0]  # 1 = high → low
        else:
            signal += [0, 0, 1, 1]  # 0 = low → high
    return time, signal

def codifica_Manchester_802_3(bits):
    time, signal = [], []
    for i, bit in enumerate(bits):
        time += [i, i+0.5, i+0.5, i+1]
        if bit == '1':
            signal += [0, 0, 1, 1]  # 1 = low → high (IEEE 802.3)
        else:
            signal += [1, 1, 0, 0]  # 0 = high → low
    return time, signal

def codifica_ManchesterDifferenziale(bits):
    time, signal = [], []
    last_level = 1  # Inizia alto
    for i, bit in enumerate(bits):
        time += [i, i+0.5, i+0.5, i+1]
        if bit == '0':
            last_level = 1 - last_level
        mid_level = 1 - last_level
        signal += [last_level, last_level, mid_level, mid_level]
        last_level = mid_level
    return time, signal

def codifica_AMI(bits):
    time, signal = [], []
    last_polarity = -1
    for i, bit in enumerate(bits):
        time += [i, i+1]
        if bit == '0':
            signal += [0, 0]
        else:
            last_polarity *= -1
            signal += [last_polarity, last_polarity]
    return time, signal

# --- Main Program ---
def main():
    bits = input("Inserisci il bitstream (es. 1011001): ").strip()
    codifica = input("Tecnica di codifica (NRZ, RZ, Manchester, Manchester 802.3, Differenziale, AMI): ").strip().lower()

    if not all(bit in '01' for bit in bits):
        print("Errore: il bitstream può contenere solo 0 e 1.")
        return

    codifica_funzioni = {
        'nrz': codifica_NRZ,
        'rz': codifica_RZ,
        'manchester': codifica_Manchester,
        'manchester 802.3': codifica_Manchester_802_3,
        'differenziale': codifica_ManchesterDifferenziale,
        'ami': codifica_AMI
    }

    funzione = codifica_funzioni.get(codifica)
    if not funzione:
        print("Tecnica di codifica non riconosciuta.")
        return

    time, signal = funzione(bits)

    plt.figure(figsize=(10, 3))
    plt.plot(time, signal, drawstyle='steps-post', color='blue')
    plt.title(f"Codifica {codifica.upper()} del bitstream {bits}")
    plt.ylim(-1.5, 1.5)
    plt.xlabel("Tempo")
    plt.ylabel("Segnale")
    plt.grid(True)
    plt.yticks([-1, 0, 1])
    plt.xticks(range(len(bits) + 1))
    plt.show()

if __name__ == "__main__":
    main()
