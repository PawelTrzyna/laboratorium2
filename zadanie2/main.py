import csv
import json
from PIL import ImageColor

def lambda_handler(event, context):
    paint_colors = []

    for file in event['files']:
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                paint_colors.append({
                    'color': row['color'],
                    'hex': row['value'],
                    'rgb': ImageColor.getrgb(str(row['value']))
                })

    with open('colors.json', 'w') as f:
        json.dump(paint_colors, f)

    print('color - hex - rgb')
    for color in paint_colors:
        print(f'{color["color"]} - {color["hex"]} - {color["rgb"]}')

    return paint_colors

if __name__ == '__main__':
    listOfFiles = ['example.csv', 'example1.csv', 'example2.csv']
    lambda_handler({'files': listOfFiles}, 0)

