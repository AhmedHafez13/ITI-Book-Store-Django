from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField()
    price = models.FloatField()
    cover_image = models.ImageField(upload_to='books/static/books/images')
    appropriate_for = models.CharField(max_length=20, choices=[("Under 8", "Under 8"),
                                                               ("8 - 15", "8 - 15"),
                                                               ("Adults", "Adults")])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (by {self.author})"
