from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.db.models import Max

from .models import User, Listing, Category, Comments, Bid, winnerPages


def index(request):
    lists = Listing.objects.filter(isActive=True)
    categories = Category.objects.all()
    return render(request, "auctions/index.html", {
        'lists': lists,
        'categories': categories,
        'titleofpage': 'Active Listings'
    })


def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        'categories': categories,
    })


def displayCategory(request):
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(categoryName=categoryFromForm)
        lists = Listing.objects.filter(isActive=True, category=category)
        categories = Category.objects.all()
        return render(request, "auctions/index.html", {
            'lists': lists,
            'categories': categories,
            'titleofpage': 'Categories'
        })


def createListing(request):
    categories = Category.objects.all()
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image = request.POST['image']
        price = request.POST['price']
        categoryselect = request.POST['category']
        categoryD = Category.objects.get(categoryName=categoryselect)
        currentUser = request.user
        bid = Bid(bid=price, user=currentUser)
        bid.save()
        Listing.date_modified = datetime.now()

        inh = Listing(title=title, description=description, imageUrl=image, price=bid,
                      seller=currentUser, category=categoryD, date_modified=datetime.now())
        inh.save()

        return HttpResponseRedirect(reverse(index))
    elif request.method == "GET":
        return render(request, "auctions/create.html", {
            'categories': categories,

        })


# --------------------------------------

def lists(request, id):
    mainlist = Listing.objects.get(pk=id)
    comments = Comments.objects.all()
    currentUser = request.user
    isListInWatchlist = request.user in mainlist.watchlist.all()
    Comments.date_commented = datetime.now()
    return render(request, "auctions/list.html", {
        'currentUser': currentUser,
        'mainlist': mainlist,
        'id': id,
        'isListInWatchlist': isListInWatchlist,
        'comments': comments,
    })


def removeWatchlist(request, id):
    mainlist = Listing.objects.get(pk=id)
    currentUser = request.user
    mainlist.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("lists", args=(id, )))


def addWatchlist(request, id):
    mainlist = Listing.objects.get(pk=id)
    currentUser = request.user
    mainlist.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("lists", args=(id, )))


def watchlist(request):
    currentUser = request.user
    lists = currentUser.listingWatchList.all()
    return render(request, 'auctions/watchlist.html', {
        'lists': lists,
        'currentUser': currentUser,
    })


def addBid(request, id):
    newbid = request.POST['bid']
    mainlist = Listing.objects.get(pk=id)
    if int(newbid) > mainlist.price.bid:
        updateBid = Bid(user=request.user, bid=int(newbid))
        updateBid.save()
        mainlist.price = updateBid
        mainlist.save()
        return render(request, 'auctions/list.html', {
            "mainlist": mainlist,
            "message": "Successful Buy",
            "update": True,
        })
    else:
        return render(request, 'auctions/list.html', {
            "mainlist": mainlist,
            "message": "Failed Buy",
            "update": False,
        })


def winnersPage(request):
    lists = Listing.objects.all()
    swinnerPages = winnerPages.objects.all()
    return render(request, "auctions/winnersPage.html", {
        'lists': lists,
        'winnerPages': swinnerPages
    })


def closeBid(request, id):
    mainlist = Listing.objects.get(pk=id)
    mainlist.isActive = False
    ttf = winnerPages(winneruser=mainlist.price.user, winnerlist=mainlist)
    ttf.save()
    mainlist.save()
    currentUser = request.user
    isListInWatchlist = request.user in mainlist.watchlist.all()
    comments = Comments.objects.all()
    return render(request, "auctions/list.html", {
        'currentUser': currentUser,
        'mainlist': mainlist,
        'id': id,
        'isListInWatchlist': isListInWatchlist,
        'comments': comments,
        'update': True,
        "message": "Successful the bid been closed"
    })


def comment(request, id):
    mainlist = Listing.objects.get(pk=id)
    comment = request.POST['comment']
    listcomment = mainlist
    usercomment = request.user
    bhh = Comments(comments=comment, date_commented=datetime.now(),
                   usercomment=usercomment, listcomment=listcomment)
    bhh.save()
    return HttpResponseRedirect(reverse("lists", args=(id, )))


def deletecomment(request, comid, reqid):
    maincomment = Comments.objects.get(pk=comid)
    maincomment.delete()
    return HttpResponseRedirect(reverse("lists", args=(reqid, )))

# --------------------------------------


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
