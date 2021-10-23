import csv
import secrets
from datetime import datetime


#### Sekcja wartości ustawianych przy uruchomieniu programu ###

#######################################################################


def save_move_to_file(userID, timestamp, points, game_variant, row):
    with open('plik.csv', 'a', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        current_timestamp = datetime.now().timestamp() - timestamp

        tempPoints = points
        # zmienna tempPoints przechowuje liczbę punktów przed wykonaniem ostatniego kroku
        # służy do porównania czy ostatni krok był poprawny i zapisania w pliku tekstowym

        if game_variant == 0:
            if (points > tempPoints):
                gameVersion = "smile_face"
                event = "smile_face"
                # correct = 1
                tempPoints = points

            if (points <= tempPoints):
                gameVersion = "smile_face"
                event = '0'
                # correct = 0

        if game_variant == 1:
            if (points > tempPoints):
                gameVersion = "lighter_background"
                event = "lighter_background"
                # correct = 1
                tempPoints = points

            if (points <= tempPoints):
                gameVersion = "lighter_background"
                event = "0"
                # correct = 0

        if game_variant == 2:
            if (points > tempPoints):
                gameVersion = "sad_face"
                event = "0"
                # correct = 1
                tempPoints = points

            if (points <= tempPoints):
                gameVersion = "sad_face"
                event = 'sad_face'
                # correct = 0

        if game_variant == 3:
            if (points > tempPoints):
                gameVersion = "sound_fail"
                event = "0"
                # correct = 1
                tempPoints = points

            if (points <= tempPoints):
                gameVersion = "sound_fail"
                event = "sound_fail"
                # correct = 0

        colNumber = row

        # row wybrana kolumna przez użytkownika

        # csvwriter.writerow(
        #     [userID, current_timestamp, gameVersion, event, correct, colNumber])
        csvwriter.writerow(
            [userID, current_timestamp, gameVersion, event, points, colNumber])
