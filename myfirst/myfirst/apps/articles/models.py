import datetime
from django.db import models

from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length = 200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата')
    def short_text(self):
            # Take the first 100 characters
            s = self.article_text[:100]
            
            # Split by whitespace
            parts = s.split()
            
            # Join all but the last element
            short_s = " ".join(parts[:-1])
            
            return short_s
    
    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'много текста'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('имя', max_length = 50)
    comment_text = models.CharField('комментарий', max_length = 200)
    pub_date = models.DateTimeField('дата добавления', auto_now=True)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        

     
