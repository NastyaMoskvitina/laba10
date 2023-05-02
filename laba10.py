import json

new_spisok_productov='product_spisok.json'
a=''
def avail(x):
    if x == True or x == 1:
        return 'В наличии'
    else:
        return 'Нет в наличии!'
with open(new_spisok_productov, encoding='utf-8 ') as myfile:
    dict=json.load(myfile)
    name=input('Введите название: ')
    price=int(input('Введите Цену: '))
    weight=int(input('Введите вес: '))
    available=bool(input('В наличии? '))
    dict['products'].append({
        'name': name,
        'price': price,
        'weight': weight,
        'available': avail(available),
    })
    with open('new_spisok_productov.json', 'w') as outfile:
        json.dump(dict, outfile, indent=4, ensure_ascii=False)
    for tov in dict['products']:
            a+='Название: '+ str(tov['name'])+ '\n'
            a += 'Цена: ' + str(tov['price']) + '\n'
            a += 'Вес: ' + str(tov['weight']) + '\n'
            a += avail(tov['available']) + '\n\n'

print(a)

en_ru = open("en-ru.txt", encoding='utf-8')
num1 = {}
num2 = {}
for stroka in en_ru.read().split("\n"):
    k = stroka.split(" - ")
    k[1] = list(k[1].split(", "))
    for i in k:
        i = k[0]
        num1[i] = k[1]
for znach in num1:
    s = num1[znach]
    for slovo in s:
        num2[slovo] = znach

ru_en = open("ru-en.txt", "w", encoding='utf-8')
for znach in sorted(num2):
    ru_en.write(znach+ " - " + num2[znach] + "\n")
ru_en.close()


#ghgh