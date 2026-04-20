from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.all()

    # Har bir rating bo‘yicha count
    rating_counts = {
        1: Feedback.objects.filter(rating=1).count(),
        2: Feedback.objects.filter(rating=2).count(),
        3: Feedback.objects.filter(rating=3).count(),
        4: Feedback.objects.filter(rating=4).count(),
        5: Feedback.objects.filter(rating=5).count(),
    }

    return render(request, 'feedback/feedback.html', {
        'form': form,
        'feedbacks': feedbacks,
        'rating_counts': rating_counts
    })
