from django.db import models

# Create your models here.
class  Moshina(models.Model):
    model_name = models.CharField(max_length=100)  # Masalan: 'Gentra'
    model = models.CharField(max_length=100)  # Masalan: 'Chevrolet'
    color = models.CharField(max_length=50)  # Masalan: 'Qora'
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Masalan: 14500.00
    year = models.PositiveIntegerField()  # Masalan: 2023
    image = models.ImageField(upload_to='media/')  # Rasm uchun
    description = models.TextField(blank=True)  # Mashina haqida tavsif

    class Meta:
        verbose_name = 'Moshina'
        ordering = ['-year']

    def __str__(self):
        return  f"{self.model_name} {self.model} ({self.price})"
