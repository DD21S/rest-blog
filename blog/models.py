from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    '''
    Information, data and content of the post.
    '''

    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='blog/',
        default='blog/default.jpg',
        blank=True,
        null=True
    )
    description = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(
        max_length=200,
        unique_for_date='published',
        null=False,
        unique=True
    )
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='posts'
    )

    class Meta:
        ordering = ('-published',)
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
    