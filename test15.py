# При помощи функции filter() из списка слов отфильтровать только те, которые являются полиндромами
# (слова которые читаются одинаково в обе стороны), регистр букв не учитывать.

inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

print(list(filter(lambda x: x.lower() == x[::-1].lower(), inputdata)))
