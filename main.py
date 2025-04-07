monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]

first_semester_avg = sum(monthly_spending[:6]) / 6
second_semester_avg = sum(monthly_spending[6:]) / 6

print(f"Средние расходы за первый семестр: {first_semester_avg: .2f}")
print(f"Средние расходы за второй семестр: {second_semester_avg: .2f}")


john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]  
sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]

john_spent_more = sum(1 for j, s in zip(john_monthly_spending, sam_monthly_spending) if j > s)

print(f"Джон тратил больше, чем Сэм, в {john_spent_more} месяцах")


paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
tina_friends = ["Tim", "Susan", "Mary", "Josh"]

all_friends = list(set(paul_friends + tina_friends))

print("Общий список друзей:", all_friends)


paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
tina_friends = ["Tim", "Susan", "Mary", "Josh"]

common_friends = list(set(paul_friends) & set(tina_friends))

print("Общие друзья Пола и Тины:", common_friends)


football_players = {"Eve", "Tom", "Richard", "Peter"}  
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}  
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}

basketball_players_only = basketball_players - (football_players | volleyball_players)

print("Игроки, зарегистрированные только в баскетболе:", basketball_players_only)


poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]

count_votes = {}
for language in poll_results:
    count_votes[language] = count_votes.get(language, 0) + 1

print("Результаты опроса:")
for language, count in count_votes.items():
    print(f"{language}: {count} голосов")


scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('Tom', 8), ('Tom', 9), ('Tom', 8)]

total_scores = {}
for player, score in scores:
    total_scores[player] = total_scores.get(player, 0) + score

print("Суммарные очки голосов:")
for player, total_scores in total_scores.items():
    print(f"{player}: {total_scores} очков")


numbers = [10, 3, 5, 9, 18, 3, 0, 7]

max_value = max(numbers)
total_sum = sum(numbers)
avg = total_sum / len(numbers)

print(f"Максимальное значение: {max_value}")
print(f"Сумма чисел: {total_sum}")
print(f"Среднее арифметическое: {avg:.2f}")


word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]

longest_word = max(word_list, key=len)
shortest_word = min(word_list, key=len)

print(f"Самое длинное слово: {longest_word}")
print(f"Самое короткое слово: {shortest_word}")


number_list = [5, 8, 2, 7, 3, 5, 6, 9, 2, 4, 8, 7, 1, 5, 3]

frequency = {}
for number in number_list:
    frequency[number] = frequency.get(number, 0) + 1

filtered_list = [number for number, count in frequency.items() if count >=3]

print("Числа, встречающиеся не менее трёх раз:", filtered_list)


exam_results = [23, 78, 96, 32, 53, 67, 23, 98, 33, 38, 45, 39, 86, 12, 43, 45]

results = sorted(set(exam_results), reverse=True)

if len(results) > 2:
    print(f"Второй лучший результат: {results[1]}")
else:
    print("Нет второго лучшего результата")

