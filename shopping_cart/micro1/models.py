from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db import models

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class PaymentDetail(models.Model):
    client_address = models.CharField(max_length=50)
    client_phone = models.IntegerField()
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

    
class ShoppingCart(models.Model): 
    user_name = models.ForeignKey(PaymentDetail, on_delete=models.CASCADE) #client
    sc_total_price = models.FloatField()

class CartDetail(models.Model):
    sc = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    product_quantity = models.IntegerField()
    product_price = models.FloatField()

class Sale(models.Model):
    user_name = models.ForeignKey(PaymentDetail,  on_delete=models.CASCADE)
    sale_date = models.DateField()

class SaleDetail(models.Model):
    sale_id = models.ForeignKey(Sale,  on_delete=models.CASCADE) 
    product_id = models.IntegerField()
    product_quantity = models.IntegerField()
    product_price = models.FloatField()