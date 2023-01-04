from django.db import models

# Create your models here.
CATEGORY= (

('AP', 'Apple'), 
('SA', 'Samsung'),
('XI', 'Xiaomi'),
('RM', 'realme'),
('OP', 'Oppo'),
('VI', 'Vivo'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    spec = models.TextField()
    category = models.CharField(choices=CATEGORY, max_length=2)
    product_image = models.ImageField(upload_to='product')
    stock = models.IntegerField(default=10)
    def __str__(self) -> str:
            return self.title
        
