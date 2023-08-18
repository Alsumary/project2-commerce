from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    categoryName = models.CharField(max_length=60)

    def __str__(self):
        return self.categoryName


class Bid(models.Model):
    bid = models.FloatField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="userBid")


class Listing(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    imageUrl = models.CharField(max_length=3000)
    price = models.ForeignKey(
        Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="pricebid")
    isActive = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(
        User, blank=True, null=True, related_name="listingWatchList")
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class winnerPages(models.Model):
    winneruser = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="winneruser")
    winnerlist = models.ForeignKey(
        Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="winnerlist")


class Comments(models.Model):
    comments = models.CharField(max_length=100)
    date_commented = models.DateTimeField(auto_now_add=True)
    usercomment = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="usercomment")
    listcomment = models.ForeignKey(
        Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listcomment")

    def __str__(self):
        template = '{0.usercomment} {0.listcomment} {0.comments}'
        return template.format(self)
