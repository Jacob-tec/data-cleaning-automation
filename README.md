# data-cleaning-automation
Automatyzacja Czyszczenia Danych

Spis treści

    Opis Projektu

    Wymagania

    Struktura Plików

    Instalacja

    Użycie

1. Opis Projektu

Ten projekt to skrypt w języku Python, którego celem jest automatyzacja procesu czyszczenia i transformacji danych. Skrypt wykonuje następujące zadania:

    Wczytuje dane z pliku CSV (data/input.csv).

    Usuwa duplikaty i puste wiersze, zapewniając spójność danych.

    Eksportuje wyczyszczone dane do nowego pliku Excel (data/output/cleaned_data.xlsx).

    Generuje raport PDF (data/output/report.pdf), podsumowujący proces czyszczenia, w tym liczbę usuniętych wierszy i inne istotne statystyki.

2. Wymagania

Do uruchomienia skryptu wymagane jest środowisko Python 3 oraz następujące biblioteki:

    pandas

    openpyxl

    fpdf

Wszystkie zależności są wyszczególnione w pliku requirements.txt.

3. Struktura Plików

data-cleaning-automation/
├── src/
│   ├── main.py             # Główny skrypt Pythona
├── data/
│   ├── input.csv           # Przykładowy plik wejściowy
│   └── output/             # Folder na pliki wyjściowe
│       ├── cleaned_data.xlsx
│       └── report.pdf
├── requirements.txt        # Lista wymaganych bibliotek
└── README.md               # Ten plik

4. Instalacja

    Sklonuj repozytorium:
    Bash

git clone https://github.com/twoja_nazwa_uzytkownika/data-cleaning-automation.git
cd data-cleaning-automation

Zainstaluj wymagane biblioteki:
Bash

    pip install -r requirements.txt

5. Użycie

Aby uruchomić skrypt, umieść plik CSV z danymi, które chcesz przetworzyć, w folderze data/ i nazwij go input.csv.

Następnie uruchom główny skrypt z terminala:
Bash

python src/main.py

Po zakończeniu działania skryptu, wyczyszczony plik Excel (cleaned_data.xlsx) oraz raport PDF (report.pdf) zostaną zapisane w folderze data/output/.
