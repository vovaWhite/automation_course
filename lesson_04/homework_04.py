adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("Task 1")
adwentures_of_tom_sawer_fixed = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer_fixed)
print("********************************************************************")
# task 02 ==
""" Замініть .... на пробіл
"""
print("Task 2")
adwentures_of_tom_sawer_fixed = adwentures_of_tom_sawer_fixed.replace(" .... ", " ")
print(adwentures_of_tom_sawer_fixed)
print("********************************************************************")
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("Task 3")
# already done in task 02
adwentures_of_tom_sawer_fixed = adwentures_of_tom_sawer_fixed.replace("  ", " ")
print(adwentures_of_tom_sawer_fixed)
print("********************************************************************")
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("Task 4")
count_h = adwentures_of_tom_sawer_fixed.count("h")
print(f"The letter 'h' count is {count_h}")
print("********************************************************************")
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("Task 5")
words = adwentures_of_tom_sawer_fixed.split()
capitalized_words_count = sum(1 for word in words if word[0].isupper())
print(f"The number of capitalized words is {capitalized_words_count}")
print("********************************************************************")
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("Task 6")
first_occurrence = adwentures_of_tom_sawer_fixed.find("Tom")
second_occurrence = adwentures_of_tom_sawer_fixed.find("Tom", first_occurrence + 1)
print(f"The second occurrence position is {second_occurrence}")
print("********************************************************************")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("Task 7")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_fixed.split(". ")
print(adwentures_of_tom_sawer_sentences)
print("********************************************************************")
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("Task 8")
print(adwentures_of_tom_sawer_sentences[3].lower())
print("********************************************************************")
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("Task 9")
starts_with_verification = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)

print(f"Is any sentence starts with 'By the time' ? {starts_with_verification}")
print("********************************************************************")
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.

"""
print("Task 10")
last_sentence = adwentures_of_tom_sawer_sentences[-1].split()
print(f"The words count in the last sentence is {len(last_sentence)}")
