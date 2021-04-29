from django.db import models
from django.urls import reverse


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.author.id}/{filename}'

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=user_directory_path)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=140)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.comment