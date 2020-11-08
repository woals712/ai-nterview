from django.conf import settings
import django
import os
import csv

settings.configure(DEBUG=True)

django.setup()

# 무조건 이 위치에 있어야함!
from interviews.models import Question, Category


# python manage.py shell에 아래 코드 복붙

# 질문 데이터 생성

QUESTION_PATH = 'C:/Users/multicampus/Documents/ai_project/s03p23a206/data/question_data_modified.csv'


hand = open(QUESTION_PATH)
reader = csv.reader(hand)

print(reader)

bulk_list = []
pk = 1
for row in reader:
    bulk_list.append(Question(
        pk=pk,
        question=row[0],
        category_id=row[1],
        time=row[2],
    ))
    print(bulk_list[-1])
    pk += 1
Question.objects.bulk_create(bulk_list)


# 카테고리 데이터 생성

CATEGORY_PATH = 'C:/Users/multicampus/Documents/ai_project/s03p23a206/data/category.csv'

hand = open(CATEGORY_PATH)
reader = csv.reader(hand)

print(reader)

bulk_list = []
for row in reader:
    bulk_list.append(Category(
        pk=row[0],
        category=row[1],
    ))
Category.objects.bulk_create(bulk_list)


# try1

# with open(CSV_PATH, 'r', newline='') as csvfile:
#     # data_reader = csv.DictReader(csvfile)
#     for row in csvfile:
#         print(row)
#         Question.objects.create(
#             question=row[0],
#             category_id=row[1],
#             time=row[2],
#         )


# try2

# # loop:
# f = open('../data/question_data_modified.csv', 'r', encoding='CP949')

# rdr = csv.reader(f)
# for row in rdr:
#     question, category, time = row
#     data = Question(question=question, category=category, time=time)
#     # add some custom validation\parsing for some of the fields
#     try:
#         data.save()
#     except:
#         # if the're a problem anywhere, you wanna know about it
#         print("there was a problem with line", i)
