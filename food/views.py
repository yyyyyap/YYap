from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Food,Review
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def foodhome(request):
    searchTerm=request.GET.get('searchFood')
    if searchTerm:
        food_list=Food.objects.filter(title__contains=searchTerm)
    else:
        food_list=Food.objects.all()
    paginator=Paginator(food_list,2)
    page_number=request.GET.get('page',1)
    foods=paginator.page(page_number)
    return render(request,'foodhome.html',{'searchTerm':searchTerm,'foods':foods})

def home(request):
    return render(request,'home.html',{'name':'YAP'})

def signup(request):
    number=request.GET.get('number')
    return render(request,'signup.html',{'number':'number'})

def fooddetail(request,food_id):
    food = get_object_or_404(Food, pk=food_id)
    reviews=Review.objects.filter(food=food)
    return render(request, 'fooddetail.html', {'food': food,'reviews':reviews})

@login_required
def createfoodreview(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    if request.method == 'GET' :
        return render(request, 'createfoodreview.html' ,
        {'form':ReviewForm , 'food':food})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.food = food
            newReview.save()
            return redirect('fooddetail',newReview.food.id)
        except ValueError:
            return render(request,'createfoodreview.html', {'form':ReviewForm, 'error':'非法数据'})

@login_required
def updatefoodreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatefoodreview.html', {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('fooddetail', review.food.id)
        except ValueError:
            return render(request, 'updatefoodreview.html', {'review':review, 'form':form, 'error':'提交非法数据'})

@login_required
def deletefoodreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('fooddetail', review.food.id)
