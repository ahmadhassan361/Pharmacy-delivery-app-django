from django.db import models

# Create your models here.
class Slider(models.Model):
    image = models.ImageField(upload_to='slider-images/',blank=True,null=True)


class Medicines(models.Model):
    image = models.ImageField(upload_to='medicine-images/',blank=True,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    salt = models.CharField(max_length=200,null=True,blank=True)
    price = models.IntegerField(default=0)
    discounted_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)


class OrderMedicine(models.Model):
    medicine = models.ForeignKey(Medicines,on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=1)

class Orders(models.Model):
    CHOICES = (
        ('Pending','Pending'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    )
    name = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    medicines = models.ManyToManyField(OrderMedicine)
    prescription = models.CharField(max_length=250,null=True,blank=True)
    order_status = models.CharField(max_length=200,choices=CHOICES,default='Pending')
    created_date = models.DateTimeField(auto_now_add=True)

class UploadPrescription(models.Model):
    image = models.ImageField(upload_to='prescription-images/')

    def get_image_url(self):
        if self.image:
            return self.image.url
        return None
