import csv
from datetime import datetime


def save_move_to_file(userID, timestamp, points, game_variant, row, column, event_changed):
    with open('dane.csv', 'a', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        current_timestamp = datetime.now().timestamp() - timestamp

        if game_variant == 0:
            gameVersion = "smile_face"
            event = 1 if event_changed == 1 else 0

        if game_variant == 1:
            gameVersion = "bigger_radius"
            event = 1 if event_changed == 1 else 0

        if game_variant == 2:
            gameVersion = "sad_face"
            event = 1 if event_changed == 1 else 0

        if game_variant == 3:
            gameVersion = "sound_fail"
            event = 1 if event_changed == 1 else 0

        csvwriter.writerow(
            [userID, current_timestamp, gameVersion, event, points, row, column])
