# 🎯 PROJEKT 1 - PROGRAM: TEXTOVÝ ANALYZÁTOR

main.py: první projekt do Engeto Online Python Akademie
author: Martina Ježková
email: jezkova.m94@gmail.com
------------------------------------------------------------------------------
## SUMMARY: 
1. 📝 O PROJEKTU
2. 🧪 UKÁZKA VÝSTUPU
3. ⚙️ SPUŠTĚNÍ
4. 🧾 ZADÁNÍ PROJEKTU - vychozí: from Engeto
5. 🔁 REFAKTORING A ZLEPŠENÍ
------------------------------------------------------------------------------

## 1. 📝 O PROJEKTU
Tento projekt je mým prvním Pythonovým zadáním v rámci
Engeto Online Python Akademie. Cílem bylo vytvořit konzolovou aplikaci 
pro analýzu zvoleného textu. Aplikace umožňuje přihlášení uživatele, 
výběr jednoho ze tří předdefinovaných textů a 
následně provádí analýzu zvoleného textu.

✨ **Funkcionalita:**
- Přihlášení uživatele (ověření dle zadaného seznamu)
- Výběr jednoho ze tří textů
- Analýza textu:
  - počet slov
  - počet slov psaných s velkým počátečním písmenem
  - počet slov psaných VELKÝMI PÍSMENY
  - počet slov psaných malými písmeny
  - počet číselných řetězců a jejich součet
  - frekvenční tabulka délek slov (textová histogramová vizualizace)
------------------------------------------------------------------------------

## 2. 🧪 UKÁZKA VÝSTUPU
Username: mike
Password: password123
----------------------------------------
Welcome to the app, mike
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 3
----------------------------------------
There are 74 words in the selected text.
There are 4 titlecase words.
There are 0 uppercase words.
There are 68 lowercase words.
There are 2 numeric strings.
The sum of all the numbers is: 8298
----------------------------------------
LEN| OCCURRENCES     |  NR.
----------------------------------------
  1|  *               |  1
  2|  ***********     |  11
  3|  *************** |  15
  4|  *********       |  9
  5|  **********      |  10
  6|  *****           |  5
  7|  ***********     |  11
  8|  ******          |  6
  9|  ***             |  3
 10|  ***             |  3
------------------------------------------------------------------------------

## 3. ⚙️ SPUŠTĚNÍ:

1. Ujisti se, že máš nainstalovaný Python 3.x
2. V terminálu přejdi do složky, kde je uložený soubor main.py:
      ```bash
      cd /cesta/k/projektu
      ```bash
3. Spusť aplikaci:
      ```bash
      python main.py
      ```bash
------------------------------------------------------------------------------

## 4. 🧾 ZADÁNÍ PROJEKTU: 

Hlavička: 
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Svetr
email: petr.svetr@gmail.com
"""
tady bude začínat tvůj kód


Zadání: 
- 3 texty

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

Obsah programu: 
1. Vyžádat si od uživatele přihlašovací jméno a heslo,
2. zjistit, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
3. pokud je registrovaný, pozdravit a umožnit analyzovat texty,
pokud není registrovaný, upozorni jej a ukonči program.


Registrovaní uživatelé: 
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+


Program:
- nechá vybrat usera mezi 3 texty v proměnné TEXT (viz. výše)
- pokud user vybere takové číslo textu, které není v zadání, program jej upozorní a skončí
- pokud user zadá jiný výstup než číslo, program jej rovněž upozorní a skončí

Pro vybraný text spočítá následující statistiky: 
- počet slov,
- počet slov začínajících velkým písmenem,
- počet slov psaných velkými písmeny,
- počet slov psaných malými písmeny,
- počet čísel (ne cifer),
- sumu všech čísel (ne cifer) v textu.

Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:

 7| * 1
 8| *********** 11
 9| *************** 15
10| ********* 9
11| ********** 10

Výstup: 
username:bob
password:123
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 1
----------------------------------------
There are 54 words in the selected text.
There are 11 titlecase words.
There are 1 uppercase words.
There are 38 lowercase words.
There are 4 numeric strings.
The sum of all the numbers 8540
----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------
  1|*                   |1
  2|**********          |10
  3|*****               |5
  4|***********         |11
  5|************        |12
  6|***                 |3
  7|****                |4
  8|*****               |5
  9|*                   |1
 10|*                   |1
 11|*                   |1


 Pokud uživatel není registrovaný: 
 username:marek
 password:123
 unregistered user, terminating the program..
-----------------------------------------------------------------

Řešení: 
- v souboru: main.py
- kód je popsán s komentáři (důvod: pro lepší učení se a snadný pochopení 
s odstupem času)

------------------------------------------------------------------------------

## 5. 🔁 REFAKTORING A ZLEPŠENÍ:

Původní řešení bylo rozšířeno a vylepšeno v následujících oblastech:

✅ Kód rozdělen do samostatných funkcí pro přehlednost
✅ Použití typové anotace (-> int, -> tuple[str, str])
✅ Nahrazení smyček za comprehension výrazy
✅ Striktní validace vstupu
✅ Ošetření délky řádku podle PEP 8 (< 79 znaků)
✅ Detailní a informativní docstringy u každé funkce
✅ Odstranění zbytečných proměnných a duplikací
