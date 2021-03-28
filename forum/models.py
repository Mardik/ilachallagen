from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Thread(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Created At')
    title = models.CharField(max_length=150, verbose_name="Title", help_text="Title of the thread")
    text = models.TextField(verbose_name="Text")
    owner = models.CharField(max_length=150, verbose_name="User Name", help_text="Title of the thread")
    
    def get_replies_count(self):
        return len(self.replies.all())
    
    def get_absolute_url(self):
        return reverse('thread-detail', kwargs={'pk': self.pk})    

class Replie(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Created At')
    text = models.TextField(verbose_name="Text")
    thread = models.ForeignKey(
        Thread, 
        on_delete=models.CASCADE,
        related_name='replies',
    )
    owner = models.CharField(max_length=150, verbose_name="User Name")
    
    def get_absolute_url(self):
        return reverse('replie-detail', kwargs={'pk': self.pk})    