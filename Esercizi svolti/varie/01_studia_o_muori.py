import random, time

def studia_o_muori():
    print("=== VITA DA PROGRAMMATORE ===\nSimulazione in corso...\n")
    time.sleep(1)

    m, c, d, s = random.choice(["alta", "bassa", "inesistente"]), random.randint(0, 10), random.choice(["miracoloso", "infinito", "inesistente"]), random.choice(["zero", "poco", "chi?"])
    print(f"Motivazione: {m}\nCaffè: {c}\nDebug: {d}\nSonno: {s}\n")

    if m == "alta" and c >= 3 and d == "miracoloso":
        print("Hai imparato! Successo sbloccato!")
    elif m == "bassa" or d == "infinito":
        print("Sei morto cercando un bug invisibile. RIP.")
    else:
        print("Vivi. Ma non chiederti come.")
        
    print("\n=== FINE ===")

studia_o_muori()