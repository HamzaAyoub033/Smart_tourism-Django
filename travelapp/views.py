
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from .models import Book, Destination, City, Gallery, Location, Hotels, Guides, Gallery, Reviews
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    data = Destination.objects.all()

    stu = {
        "destination": data
    }
    print(stu)
    return render(request, 'travelapp/index.html', stu)


def destination(request):
    info = Destination.objects.all()
    info_city = City.objects.all()
    info_hotels = Hotels.objects.all()
    info_locations = Location.objects.all()

    context = {
        'destination': info,
        'city': info_city,
        'hotels': info_hotels,
        'location': info_locations,
    }
    return render(request, 'travelapp/destination.html', context)


class packageDetail(DetailView):
    model = Destination
    context_object_name = "destination"
    template_name = "travelapp/package-details.html"


def packageDetails(request):
    return render(request, 'travelapp/package-details.html')


# def book(request):
#     if request.method == 'POST':
#         if request.POST.get('name'):
#             post=Book()
#             post.save()
#             return render(request, 'travelapp/destination.html')
#         else:
#             return render(request,'travelapp/package-details.html')

def book(request):
    if request.method == 'POST':
        print("This is booking")
        return render(request, 'travelapp/package-details.html')


def contact(request):
    if request.POST.get('name') and request.POST.get('email'):
        post = Book()
        post.name = request.POST.get('name')
        post.email = request.POST.get('email')
        post.save()
        return render(request, 'travelapp/contact.html')
    else:
        return render(request, 'travelapp/contact.html')


def booking(request):
    return render(request, 'travelapp/Book.html')


def packages(request):
    info = Destination.objects.all()
    info_city = City.objects.all()
    info_hotels = Hotels.objects.all()
    info_locations = Location.objects.all()

    context = {
        'package': info,
        'city': info_city,
        'hotels': info_hotels,
        'location': info_locations,
    }
    return render(request, 'travelapp/package.html', context)


def about(request):
    rev = Reviews.objects.all()
    context = {
        "rev": rev,
    }
    return render(request, 'travelapp/about.html', context)


def contact(request):
    return render(request, 'travelapp/contact.html')


def guide(request):
    guides = Guides.objects.all()

    return render(request, 'travelapp/guide.html', {'guides': guides})


def gallary(request):
    images = Gallery.objects.all()

    return render(request, 'travelapp/gallary.html', {'images': images})


def startup(request):
    if request.method == "POST":

        city = request.POST.get('whereto')
        budget = request.POST.get('budget')
        date = request.POST.get('check-in')
        person = request.POST.get('person')
        tour = request.POST.get('type')
        # user = User.objects.create_user(
        #     city=city, date=date, tour=tour)
        # user.save()
        print(city)
        print(budget)
        print(date)
        print(person)
        print(tour)

    return render(request, 'travelapp/index.html')
