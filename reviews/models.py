from django.db import models

class Review(models.Model):
    author = models.CharField(max_length=100)  # Или ForeignKey на User
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)  # От 1 до 5, например
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} ({self.rating}★) {self.text} {self.created_at} "
    # 2342
