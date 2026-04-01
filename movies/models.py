from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-release_year']
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'