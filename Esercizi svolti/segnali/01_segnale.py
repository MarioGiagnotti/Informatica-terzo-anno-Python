import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave(ampiezza, frequenza, fase_gradi, durata=1, campioni=1000):
    # Converte fase da gradi a radianti
    fase = np.deg2rad(fase_gradi)
    
    # Asse temporale
    t = np.linspace(0, durata, campioni)
    
    # Calcolo dell'onda
    y = ampiezza * np.cos(2 * np.pi * frequenza * t + fase)
    # Plot
    plt.figure(figsize=(10, 4))
    plt.plot(t, y, label=f'{ampiezza}·cos(2π·{frequenza}·t + {fase_gradi}°)')
    plt.title('Onda Sinusoidale')
    plt.xlabel('Tempo [s]')
    plt.ylabel('Ampiezza')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Input dell'utente
ampiezza = float(input("Inserisci l'ampiezza: "))
frequenza = float(input("Inserisci la frequenza [Hz]: "))
fase_gradi = float(input("Inserisci la fase [gradi]: "))

plot_sine_wave(ampiezza, frequenza, fase_gradi)
