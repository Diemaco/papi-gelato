import builtins

# Welkom
print('Welkom bij Papi Gelato.')

# Lijst van bestelde ijsjes
ijsjes = []


# Input van de gebruiker en antwoorden limiteren tot een lijst
def input(input_string, allowed: list = None, incorrect_msg: str = 'Sorry, dat snap ik niet...'):
    while (antwoord := builtins.input(input_string)) is not None and not (allowed is None or antwoord in allowed):
        print(incorrect_msg)
    return antwoord


# Nodige informatie opslaan per ijsje
class Ijsje:
    def __init__(self):
        self.hoeveelheid = -1
        self.bakje = True
        self.topping_kosten = 0.0


# Gebruiker prijzen/totaal laten zien
def print_bonnetje():
    print('--------- ["Papi Gelato"] ---------\n')

    # Hoeveelheid (HvH) liters/bolletjes
    hvh = 0

    # Hoeveelheid bakjes
    hvh_bakjes = 0

    # Hoeveelheid hoorntjes
    hvh_hoorntjes = 0

    # Kosten voor alle toppings bij elkaar
    topping_kosten = 0

    # Totalen berekenen
    for ijsje in ijsjes:

        # Bakje/Hoorntje totaal verhogen als het niet zakelijk is
        if not is_zakelijk:
            if ijsje.bakje:
                hvh_bakjes += 1

            else:
                hvh_hoorntjes += 1

        # De totaale hoeveelheid verhogen
        hvh += ijsje.hoeveelheid

        # De totale topping kosten verhogen met de topping kosten van het ijsje
        topping_kosten += ijsje.topping_kosten

    # Totaal prijs is de hoeveelheid keer €9.80 (zakelijk) en €1.10 (particulier)
    totaal_prijs = hvh * (9.8 if is_zakelijk else 1.1)

    # Print de totale prijs voor het aantal Liters/Bolletjes
    print(f'{("Liters" if is_zakelijk else "Bolletjes").ljust(16 - len(str(hvh)))}{hvh} x €9.80 = €{totaal_prijs:.2f}')

    # Alleen laten zien indien het niet nul is
    if hvh_bakjes != 0:

        # De totale prijs verhogen met de kosten van alle bakjes
        totaal_prijs += hvh_bakjes * 0.75

        # Hoeveelheid, prijs en totaal laten zien
        print(f'{"Bakje".ljust(16 - len(str(hvh_bakjes)))}{hvh_bakjes} x €0.75 = €{(hvh_bakjes * 0.75):.2f}')

    # Alleen laten zien indien het niet nul is
    if hvh_hoorntjes != 0:

        # De totale prijs verhogen met de kosten van alle hoorntjes
        totaal_prijs += hvh_hoorntjes * 1.25

        # Hoeveelheid, prijs en totaal laten zien
        print(f'{"Horrentje".ljust(16 - len(str(hvh_hoorntjes)))}{hvh_hoorntjes} x €1.25 = €{(hvh_hoorntjes * 1.25):.2f}')

    # Alleen de topping kosten laten zien als het niet 0 is
    if topping_kosten != 0:

        # De totale prijs verhogen met de kosten van alle toppings
        totaal_prijs += topping_kosten

        # Hoeveelheid, prijs en totaal laten zien
        print(f'{"Topping".ljust(20 - len(str(topping_kosten)))}1 x €{topping_kosten:.2f} = €{topping_kosten :.2f}')

    # Divider tussen losse kosten en totaal (en btw) laten zien
    print(f'{"".ljust(25)}-------- +')

    # Totaal prijs laten zien
    print(f'{"Totaal".ljust(25)}= €{totaal_prijs:.2f}')

    # Alleen de btw laten zien als het zakelijk is
    if is_zakelijk:
        print(f'{"BTW (9%)".ljust(25)}= €{((totaal_prijs / 109) * 9):.2f}')


# Vraagt de gebruiker of ze nog een keer iets willen bestellen
def nog_een_keer():
    if input(
            f'Hier is uw {"bakje" if ijsjes[-1].bakje else "hoorntje"} met {ijsjes[-1].hoeveelheid} bolletje(s). Wilt u nog meer bestellen?\n\t[Y/N] ',
            ['Y', 'N']) == 'Y':
        main()
    else:
        # Dit is geen slimme keuze van de gebruiker maar we kunnen ze niet forceren
        print('Bedankt en tot ziens!')

        # Bonnetje laten zien
        print_bonnetje()


# Lelijke manier van bepalen welke topping de gebruiker wilt en uitreken wat het gaat kosten
def welke_topping():
    topping = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?\n\t[A/B/C/D] ',
                    ['A', 'B', 'C', 'D'])

    # Geen topping
    if topping == 'A':
        print('Oké, u wilt geen topping.')

    # Slagroom
    if topping == 'B':
        ijsjes[-1].topping_kosten += 0.5

    # Sprinkels (prijs per bolletje)
    if topping == 'C':
        ijsjes[-1].topping_kosten += 0.3 * ijsjes[-1].hoeveelheid

    # Caramel Saus (prijs is niet hezelfde voor bakje/hoorntje)
    if topping == 'D':
        if ijsjes[-1].bakje:
            ijsjes[-1].topping_kosten += 0.9
        else:
            ijsjes[-1].topping_kosten += 0.6


# Vraagt aan de gebruiker of ze een hoorntje of een bakje willen
def bakje_of_hoorntje():
    ijsjes[-1].bakje = input(
        f'Wilt u deze {ijsjes[-1].hoeveelheid} bolletje(s) in A) een hoorntje of B) een bakje?\n\t[A/B] ',
        ['A', 'B']) == 'A'


# Voor ieder bolletje/liter in de laatste bestelling vragen welke smaak ze willen
def welke_smaak():
    for i in range(ijsjes[-1].hoeveelheid):
        input(
            f'Welke smaak wilt u voor {"liter" if is_zakelijk else "bolletje"} nummer {i + 1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?\n\t[A/C/M/V] ',
            ['A', 'C', 'M', 'V'])


# Boolean die bepaalt of het een zakelijke transactie is
is_zakelijk = input('Bent u zakelijk of particulier?\n\t[A/B] ', ['A', 'B']) == 'A'


def main():
    # Nieuw ijsje toevoegen aan de lijst van bestelde ijsjes
    ijsjes.append(Ijsje())

    # Door blijven vragen tot de gebruiker iets goeds invoert
    while True:

        # Aantal bolletjes/liters opslaan in het nieuwe ijsje
        ijsjes[-1].hoeveelheid = int(input(f'Hoeveel {"liters" if is_zakelijk else "bolletjes"} wilt u?\n\t'))

        # Hoeveelheid maakt niet uit voor een zakelijke transactie
        if is_zakelijk:
            break

        # Checken of de gekozen hoeveelheid tussen 0 en 4 zit
        if 0 < ijsjes[-1].hoeveelheid < 4:
            bakje_of_hoorntje()

        # Anders tussen 3 en 9
        elif 3 < ijsjes[-1].hoeveelheid < 9:
            print(f'Dan krijgt u van mij een bakje met {ijsjes[-1].hoeveelheid} bolletjes')

        # Boven 8 is te veel
        elif ijsjes[-1].hoeveelheid > 8:
            print('Sorry, zulke grote bakken hebben we niet')
            continue

        # Gebruiker heeft een negatief getal of 0 ingevoerd
        else:
            print('Sorry dat snap ik niet...')
            continue

        # Dit wordt alleen bereikt als de gebruiker iets heeft ingevuld wat aan minimaal 1 van de condities voldoet
        break

    # Bij zakelijke klanten hoef je alleen te vragen welke smaak (per liter) ze willen bestellen
    if is_zakelijk:
        welke_smaak()
        print_bonnetje()

    else:
        welke_topping()
        welke_smaak()
        nog_een_keer()


if __name__ == "__main__":
    main()
