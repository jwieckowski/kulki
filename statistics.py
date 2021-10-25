import csv
import secrets
from datetime import datetime


#### Sekcja wartości ustawianych przy uruchomieniu programu ###

#######################################################################


def save_move_to_file(userID, timestamp, points, game_variant, row, event_changed):
    with open('plik.csv', 'a', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        current_timestamp = datetime.now().timestamp() - timestamp

        # zmienna tempPoints przechowuje liczbę punktów przed wykonaniem ostatniego kroku
        # służy do porównania czy ostatni krok był poprawny i zapisania w pliku tekstowym

        if game_variant == 0:
            gameVersion = "smile_face"
            event = 1 if event_changed == 1 else 0

        if game_variant == 1:
            gameVersion = "lighter_background"
            event = 1 if event_changed == 1 else 0

        if game_variant == 2:
            gameVersion = "sad_face"
            event = 1 if event_changed == 1 else 0

        if game_variant == 3:
            gameVersion = "sound_fail"
            event = 1 if event_changed == 1 else 0

        colNumber = row

        # row wybrana kolumna przez użytkownika

        # csvwriter.writerow(
        #     [userID, current_timestamp, gameVersion, event, correct, colNumber])
        csvwriter.writerow(
            [userID, current_timestamp, gameVersion, event, points, colNumber])
