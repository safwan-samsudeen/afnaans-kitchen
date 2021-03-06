from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    new_email = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=100)
    confirm_id = models.BigIntegerField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class FoodType(models.Model):
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.long_name


class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    food_item_type = models.ForeignKey(
        FoodType, on_delete=models.CASCADE)
    price = models.IntegerField()
    main_image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField()
    veg = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class PersonInTeam(models.Model):
    name = models.CharField(max_length=200)
    positions = models.TextField()
    main_image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField()
    email_address = models.EmailField(max_length=254)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user} - {self.item} - {self.qty}"


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    order_description_dict = models.TextField(default='{}')
    status = models.CharField(max_length=2, choices=(
        ('W', 'To be Confirmed'),
        ('P', 'Being Prepared'),
        ('O', 'On the Way'),
        ('D', 'Delivered'),
        ('C', 'Cancelled'),
    ), default='W')
    last_modified = models.DateTimeField(auto_now=True)
    delivery_time = models.CharField(default='', max_length=500)
    date_added = models.DateTimeField(default=datetime.now)
    user_description = models.TextField(default="")

    def __str__(self):
        return f"{self.user} - {self.date_added.strftime('%d/%m/%y')}"
