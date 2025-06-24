from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = self.post_set.aggregate(total=models.Sum('rating'))['total'] or 0
        post_rating *= 3

        comment_rating = self.user.comment_set.aggregate(total=models.Sum('rating_comment'))['total'] or 0
        post_comments_rating = 0
        
        for post in self.post_set.all():
            comments_sum = post.comment_set.aggregate(total=models.Sum('rating_comment'))['total'] or 0
            post_comments_rating += comments_sum

        self.rating = post_rating + comment_rating + post_comments_rating
        self.save()

    def __str__(self):
        return f"{self.user.username}"


class Category(models.Model):
    name = models.CharField(max_length=255, unique = True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = 'AR'
    news = 'NW'
    POST_TYPES = [
        (article, 'Статья'),
        (news, 'Новость'),
    ]
    post_type = models.CharField(max_length=2, choices=POST_TYPES, default=article)
    created_at = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    
    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '.......'

    def str(self):
        return f"{self.title} ({self.get_post_type_display()})"


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def str(self):
        return f"{self.post.title} — {self.category.name}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    text_comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    rating_comment = models.IntegerField(default=0)    
    
    def like(self):
        self.rating_comment += 1
        self.save()
    
    def dislike(self):
        self.rating_comment -= 1
        self.save()

    def str(self):
        return f"Комментарий от {self.user.username} к '{self.post.title}'"