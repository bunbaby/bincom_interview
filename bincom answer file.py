# Color details from the HTML table
from statistics import median, variance
import random

color_details = '''
GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE
GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE
BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE
'''

color_rows = color_details.strip().split('\n')

all_colors = []

for row in color_rows:
    colors = row.split(',')
    all_colors.extend(colors)

mean_color = ''
if all_colors:
    mean_color = max(set(all_colors), key=all_colors.count)
color_frequency = {}
for color in all_colors:
    color_frequency[color] = color_frequency.get(color, 0) + 1
most_worn_color = max(color_frequency, key=color_frequency.get)

median_color = median(all_colors)
total_colors = 0
red_colors = 0

for row in color_rows:
    colors = row.split(',')
    for color in colors:
        total_colors += 1
        if color.strip().lower() == 'red':
            red_colors += 1
probability_red = red_colors / total_colors




print(color_rows)
print(colors)
print(all_colors)
print("Mean Color:", mean_color)
print("Color Mostly Worn:", most_worn_color)
print("Median Color:", median_color)
print("Probability of Choosing Red:", probability_red)

def recursive_search(numbers, target, start_index=0):
    if start_index >= len(numbers):
        return False

    if numbers[start_index] == target:
        return True

    return recursive_search(numbers, target, start_index + 1)

numbers = [4, 2, 7, 1, 9, 5]
target = int(input("Enter a number to search: "))

if recursive_search(numbers, target):
    print("Number found in the list.")
else:
    print("Number not found in the list.")


random_number = ''.join(random.choice('01') for _ in range(4))
print("Random Number (Binary):", random_number)
decimal_number = int(random_number, 2)
print("Decimal Number:", decimal_number)





