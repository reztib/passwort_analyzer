import math
import time

def calculate_entropy(password):
    """
    Berechnet die Entropie eines Passworts basierend auf der Zeichenvielfalt und Länge.
    """
    categories = {
        "lowercase": 26,
        "uppercase": 26,
        "digits": 10,
        "special": 32,
    }
    
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += categories["lowercase"]
    if any(c.isupper() for c in password):
        charset_size += categories["uppercase"]
    if any(c.isdigit() for c in password):
        charset_size += categories["digits"]
    if any(not c.isalnum() for c in password):
        charset_size += categories["special"]
    
    if charset_size == 0:
        return 0  # Kein valides Passwort
    entropy = len(password) * math.log2(charset_size)
    return entropy

def cracking_time(entropy, attempts_per_second):
    """
    Schätzt die Zeit, die benötigt wird, um ein Passwort per Brute-Force zu knacken.
    """
    total_combinations = 2 ** entropy
    seconds = total_combinations / attempts_per_second
    return seconds

def format_time(seconds):
    """
    Formatiert Sekunden in eine lesbare Zeitspanne (Jahre, Tage, Stunden, Minuten, Sekunden).
    """
    intervals = [
        ("Jahre", 31536000),
        ("Tage", 86400),
        ("Stunden", 3600),
        ("Minuten", 60),
        ("Sekunden", 1),
    ]
    result = []
    for name, count in intervals:
        value = seconds // count
        if value:
            result.append(f"{int(value)} {name}")
            seconds %= count
    return ", ".join(result) if result else "weniger als 1 Sekunde"

def main():
    """
    Hauptfunktion der Anwendung mit Begrüßung und interaktivem Prompt.
    """
    print("Willkommen zur Passwort-Analyse!")
    print("Dieses Tool berechnet die Entropie deines Passworts und schätzt die Zeit, die benötigt wird, um es zu knacken.")
    print("-" * 50)
    
    while True:
        password = input("\nBitte gib ein Passwort ein (oder 'exit', um zu beenden): ")
        if password.lower() == 'exit':
            print("Vielen Dank fürs Nutzen des Tools! Bleib sicher! 🚀")
            break
        
        entropy = calculate_entropy(password)
        if entropy == 0:
            print("Das eingegebene Passwort enthält keine validen Zeichen. Bitte versuche es erneut.")
            continue
        
        # Annahme: Brute-Force-Geschwindigkeit 10^9 Versuche/Sekunde
        attempts_per_second = 10**9
        time_to_crack = cracking_time(entropy, attempts_per_second)
        
        print(f"\nAnalyse deines Passworts:")
        print(f"- Entropie: {entropy:.2f} Bits")
        print(f"- Geschätzte Zeit zum Knacken (bei 10^9 Versuche/Sekunde): {format_time(time_to_crack)}")
        print("-" * 50)
        time.sleep(1)  # Kleiner Pauseeffekt für bessere User Experience

if __name__ == "__main__":
    main()
