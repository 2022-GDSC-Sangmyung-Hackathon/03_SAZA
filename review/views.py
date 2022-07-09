from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from review.forms import ReviewForm


def add_review(request):
    if request.user.is_authenticated:
        #restaurant = get_object_or_404(Restaurant, pk=pk)
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect(review.get_absolute_url())
        else:
            return render(request, 'restaurant/inputReview.html')
    else:
        raise PermissionDenied