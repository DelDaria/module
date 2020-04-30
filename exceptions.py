import csv
import datetime


class GameOver(Exception):
    @staticmethod
    def add_score(name, score):
        scores = []
        dict = {
            'id': '',
            'name': '',
            'score': '',
            'date': ''}
        fieldnames = dict.keys()

        with open('scores.txt', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['score'] = int(row['score'])
                scores.append(row)
        new = {
            'name': name,
            'score': score,
            'date': str(datetime.datetime.today())
        }
        scores.append(new)
        scores = sorted(scores, key=lambda j: j['score'], reverse=True)
        with open('scores.txt', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            i = 0
            while i < len(scores) and i < 10:
                scores[i]['id'] = i+1
                writer.writerow(scores[i])
                i += 1


class EnemyDown(Exception):
    pass
