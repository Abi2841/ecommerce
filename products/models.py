from django.db import models
from django.contrib.auth.models import User
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
        
class Customer(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)

    name = models.CharField(max_length=200)

    locality =  models.CharField(max_length=200) 
    city = models.CharField(max_length=50)

    mobile = models.IntegerField(default=0)

    zipcode = models.IntegerField()


    def _str_(self):
        return self.name
