import numpy as np
import matplotlib.pyplot as plt

def genera_segnale_NRZ(bitstream, bitrate, t):
    bit_duration = 1 / bitrate
    segnale = np.zeros_like(t)
    for i, bit in enumerate(bitstream):
        inizio = int(i * bit_duration * len(t) / t[-1])
        fine = int((i + 1) * bit_duration * len(t) / t[-1])
        segnale[inizio:fine] = int(bit)
    return segnale

def portante(frequenza, ampiezza, t):
    return ampiezza * np.sin(2 * np.pi * frequenza * t)

def modulazione_ASK(bitstream, freq, amp, durata):
    bitrate = len(bitstream) / durata
    t = np.linspace(0, durata, 1000)
    segnale = genera_segnale_NRZ(bitstream, bitrate, t)
    carrier = portante(freq, amp, t)
    modulato = carrier * segnale
    return t, segnale, carrier, modulato

def modulazione_FSK(bitstream, freq, amp, freq_dev, durata):
    bitrate = len(bitstream) / durata
    t = np.linspace(0, durata, 1000)
    segnale = genera_segnale_NRZ(bitstream, bitrate, t)
    modulato = np.zeros_like(t)
    for i, bit in enumerate(bitstream):
        f = freq + freq_dev if bit == '1' else freq - freq_dev
        inizio = int(i * (len(t) / len(bitstream)))
        fine = int((i + 1) * (len(t) / len(bitstream)))
        modulato[inizio:fine] = amp * np.sin(2 * np.pi * f * t[inizio:fine])
    carrier = portante(freq, amp, t)
    return t, segnale, carrier, modulato

def modulazione_PSK(bitstream, freq, amp, fase_gradi, durata):
    bitrate = len(bitstream) / durata
    t = np.linspace(0, durata, 1000)
    segnale = genera_segnale_NRZ(bitstream, bitrate, t)
    fase = np.deg2rad(fase_gradi)
    modulato = np.zeros_like(t)
    for i, bit in enumerate(bitstream):
        shift = 0 if bit == '0' else fase
        inizio = int(i * (len(t) / len(bitstream)))
        fine = int((i + 1) * (len(t) / len(bitstream)))
        modulato[inizio:fine] = amp * np.sin(2 * np.pi * freq * t[inizio:fine] + shift)
    carrier = portante(freq, amp, t)
    return t, segnale, carrier, modulato

def modulazione_QAM(bitstream, M, freq, amp, durata):
    bits_per_symbol = int(np.log2(M))
    symbols = [bitstream[i:i+bits_per_symbol] for i in range(0, len(bitstream), bits_per_symbol)]

    # Padding se necessario
    if len(symbols[-1]) < bits_per_symbol:
        symbols[-1] += '0' * (bits_per_symbol - len(symbols[-1]))

    # Mapping simboli per 4-QAM, 8-QAM, 16-QAM
    if M == 4:
        mapping = {
            '00': (1, 1), '01': (-1, 1), '11': (-1, -1), '10': (1, -1)
        }
    elif M == 8:
        mapping = {
            '000': (1, 1),   '001': (0, 1),   '010': (-1, 1),
            '011': (-1, 0),  '100': (-1, -1), '101': (0, -1),
            '110': (1, -1),  '111': (1, 0)
        }
    elif M == 16:
        mapping = {
            '0000': (3, 3),  '0001': (1, 3),  '0010': (-1, 3),  '0011': (-3, 3),
            '0100': (3, 1),  '0101': (1, 1),  '0110': (-1, 1),  '0111': (-3, 1),
            '1000': (3, -1), '1001': (1, -1), '1010': (-1, -1), '1011': (-3, -1),
            '1100': (3, -3), '1101': (1, -3), '1110': (-1, -3), '1111': (-3, -3)
        }
    else:
        print("Modulazione QAM non supportata. Usa solo 4, 8 o 16.")
        exit()

    t = np.linspace(0, durata, 1000)
    simboli_estesi = np.zeros_like(t)
    portante_reale = np.cos(2 * np.pi * freq * t)
    portante_immaginaria = np.sin(2 * np.pi * freq * t)

    symbol_duration = durata / len(symbols)
    for i, bits in enumerate(symbols):
        a, b = mapping.get(bits, (0, 0))  # default se simbolo mancante
        inizio = int(i * (len(t) / len(symbols)))
        fine = int((i + 1) * (len(t) / len(symbols)))
        simboli_estesi[inizio:fine] = amp * (a * portante_reale[inizio:fine] + b * portante_immaginaria[inizio:fine])

    segnale = genera_segnale_NRZ(bitstream, len(bitstream) / durata, t)
    portante_mix = portante(freq, amp, t)
    return t, segnale, portante_mix, simboli_estesi


# === MAIN ===
print("Scegli tipo di modulazione: [ASK, FSK, PSK, QAM]")
scelta = input("Modulazione: ").upper()

if scelta == 'ASK':
    bitstream = input("Inserisci la sequenza di bit (es. 10110): ")
    freq = float(input("Frequenza portante [Hz]: "))
    amp = float(input("Ampiezza portante: "))
    durata = float(input("Durata simulazione [s]: "))
    t, segnale, carrier, modulato = modulazione_ASK(bitstream, freq, amp, durata)

elif scelta == 'FSK':
    bitstream = input("Inserisci la sequenza di bit (es. 10110): ")
    freq = float(input("Frequenza portante [Hz]: "))
    amp = float(input("Ampiezza portante: "))
    freq_dev = float(input("Deviazione di frequenza [Hz]: "))
    durata = float(input("Durata simulazione [s]: "))
    t, segnale, carrier, modulato = modulazione_FSK(bitstream, freq, amp, freq_dev, durata)

elif scelta == 'PSK':
    bitstream = input("Inserisci la sequenza di bit (es. 10110): ")
    freq = float(input("Frequenza portante [Hz]: "))
    amp = float(input("Ampiezza portante: "))
    fase = float(input("Sfasamento [gradi]: "))
    durata = float(input("Durata simulazione [s]: "))
    t, segnale, carrier, modulato = modulazione_PSK(bitstream, freq, amp, fase, durata)

elif scelta == 'QAM':
    M = int(input("Scegli M per M-QAM (4, 8, 16): "))
    bitstream = input("Inserisci la sequenza di bit (es. 10110): ")
    freq = float(input("Frequenza portante [Hz]: "))
    amp = float(input("Ampiezza portante: "))
    durata = float(input("Durata simulazione [s]: "))
    t, segnale, carrier, modulato = modulazione_QAM(bitstream, M, freq, amp, durata)

else:
    print("Tipo di modulazione non valido.")
    exit()

# === PLOT ===
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, segnale, label="Segnale Modulante (NRZ)")
plt.title("Segnale Modulante (NRZ)")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, carrier, label="Portante", color='orange')
plt.title("Portante")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, modulato, label="Segnale Modulato", color='green')
plt.title("Segnale Modulato")
plt.grid()

plt.tight_layout()
plt.show()
