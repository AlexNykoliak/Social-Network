from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    """Created profile for user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Post(models.Model):

    """Our post model which is connected to included User function"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, verbose_name='title', help_text='write the title')
    body = models.TextField(verbose_name='body', help_text='write the body')
    publication_date = models.DateField(auto_now_add=True, verbose_name='publication_date')

    def __str__(self):
        return "{}: {}".format(self.author.username, self.title)


class Like(models.Model):

    """Our like model with ForeignKey User & Post"""
    user = models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_like', on_delete=models.CASCADE)
    like = models.SmallIntegerField(default=0)
    publication_date = models.DateField(format('%Y-%m-%d'), auto_now_add=True)


class Unlike(models.Model):

    """Our unlike model with ForeignKey User & Post"""
    user = models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_like', on_delete=models.CASCADE)
    like = models.SmallIntegerField(default=0)
    publication_date = models.DateField(format('%Y-%m-%d'), auto_now_add=True)