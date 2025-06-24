# Django News Portal (Итоговое задание 9.1 (HW-03))

## О проекте

Этот проект представляет собой реализацию моделей новостного портала на Django. Работа выполнена в рамках тестового задания на знание основ работы с Django ORM, моделями, реляционными связями и методами изменения рейтингов объектов.

### Что реализовано:

- Созданы модели: Author, Category, Post, Comment, PostCategory.
- Каждая модель снабжена нужными полями, методами like(), dislike() и preview().
- У модели Author реализован метод update_rating, который учитывает рейтинг постов, комментариев автора и комментариев к его постам.
- Настроены связи: OneToOne (Author ↔ User), ForeignKey и ManyToMany (Post ↔ Category).
- В модели Post можно создать как новость (news), так и статью (article).
- Добавлены методы __str__() для удобного отображения объектов.

### Используемые технологии:

- Python 3.11
- Django 4.x
- SQLite (по умолчанию)

## Как запустить

`bash
git clone https://github.com/ТВОЙ_НИК/news-portal-django.git
cd news-portal-django
python manage.py makemigrations
python manage.py migrate
python manage.py shell
