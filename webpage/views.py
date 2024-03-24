from django.shortcuts import render, redirect
from webpage.forms import TextFileForm
from webpage.models import TextFile
import math


#Функция загрузки файла и перехода на старницу с таблицей обработанных данных
def upload_file(request):
    if request.method == 'POST':
        form = TextFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                file = form.save()
                file_path = file.file.path
                return redirect('output', file_path=file_path)
            except:
                form.add_error(None, "Ошибка при обработке формы!!!")
    else:
        form = TextFileForm()
    context = {
        'title': 'Главная страница',
        'header': 'Загрузить файл можно здесь!!!',
        'form': form,
    }
    return render(request, 'index.html', context=context)


#Функция расчёта параметра IDF
def calculate_idf(counts_doc: int, term: int) -> float:
    return math.log(counts_doc/term)


#Функция, читающая текст из файла и вычисляющая все значения
def info_from_text(request, file_path):

    #Читаем файл
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            #Преобразуем строки в массив из строк
            words = content.split()
    except FileNotFoundError:
        print("Файл не был найден!!!")

    #Кол-во всех слов в файле
    size_content = len(words)
    #Кол-во загруженных файлов с текстом
    documents = TextFile.objects.all().count()

    #Cписок из вычисленных значений для занесения в таблицу
    items = []

    for idx, word in enumerate(words):
        #Кол-во слов в коллекции
        count_word = words.count(word)
        #Частота появления слова в переданном тексте из файла
        TF = round(count_word / size_content, 4)
        #Частота появления слова в загруженных документах (Обратная частота документа)
        IDF = round(calculate_idf(documents, count_word), 4)
        items.append([word, TF, IDF])


    #Выбираем первые 50 записей для задания
    items = items[:50]
    items.sort(key=lambda x: x[2], reverse=True)

    context = {
        'title': 'Таблица',
        'header': 'Таблица с проведенным анализом данных!!!',
        'items': items,
    }
    return render(request, 'output.html', context=context)

