import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PythonWeb.settings')
import django

django.setup()
from django.contrib.auth.models import User
from home.models import Category, Book
import random
from faker import Faker

category_list = ["Action and adventure",
                 "Art",
                 "Alternate histor",
                 "Autobiography",
                 "Anthology",
                 "Biography",
                 "Chick lit",
                 "Book review",
                 "Cookbook",
                 "Children's"]


def fakeCategory():
    for i in range(len(category_list)):
        print(category_list[i])
        category = Category.objects.create(name=category_list[i])
        print("Done Category")


def fakeUser():
    for x in range(1, 10):
        name = "user" + x.__str__()
        email = name + "@gmail.com"
        user = User.objects.get(username=name, email=email, password="123456")
        user.save()


def fakeBook():
    faker_gen = Faker()
    category_list = Category.objects.all()

    for i in range(1, 12):
        title = faker_gen.sentence()
        content = faker_gen.sentences()
        author = faker_gen.name()
        price = random.randint(1, 99)
        category = category_list[random.randint(0, len(category_list)-1)]
        publish_date = faker_gen.date()
        image = 'images/books/' + random.randint(1, 12).__str__() + '.jpg'
        number_page = random.randint(100, 500)
        # create book
        book = Book.objects.create(title=title,
                                   content=content,
                                   author=author,
                                   price=price,
                                   category=category,
                                   publish_date=publish_date,
                                   image=image,
                                   number_page=number_page
                                   )


if __name__ == '__main__':
    print("Begin Fake Data")
    print("Done Fake Data")
