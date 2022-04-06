from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save

# from .utils import slugify_instance_title

# Create your models here.
User = get_user_model()

class Manual(models.Model):
    name = models.CharField(max_length=50, null=True, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Manuals"

    def __str__(self):
        return str(self.name)

class Article(models.Model):
    status_alt = (
        ('draft', 'draft'),
        ('published', 'published')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    manual = models.ForeignKey(Manual, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/media', null=True, blank=True)
    text = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    featured = models.BooleanField(default=False)
    status = models.CharField(max_length=25, choices=status_alt, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'article'
        index_together = ['manual', 'title']
        ordering = ['-created_at']

    def publish(self):
        self.published_at = timezone.now()
        self.status = 'published'
        self.save()

    def get_absolute_url(self):
        """Absolute URL for Post"""
        return reverse("articles_detail", kwargs={"manual":self.manual, "slug": self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey('knowledge.Article', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'post':self.post.slug , 'pk': self.pk})

    def __str__(self):
        return self.message
