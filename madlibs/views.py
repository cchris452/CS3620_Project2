from django.shortcuts import get_object_or_404, redirect, render
from .forms import MadLibForm
from .models import madlibs

# Create your views here.
def index(request):
    return render(request, 'madlibs/index.html')

def create(request):
    if request.method == 'POST':
        form = MadLibForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.story_text = instance.create_story()
            instance.save()
            return redirect('madlibs:story', madlibs_id=instance.id)
    else:
        form = MadLibForm()
    return render(request, 'madlibs/madlib_form.html', {'form': form})

def story(request, madlibs_id):
    madlib = get_object_or_404(madlibs, pk=madlibs_id)
    context = {
        'madlib': madlib,
        'story_text': madlib.story_text
    }
    return render(request, 'madlibs/story.html', context)

def stories(request):
    madlibslist = madlibs.objects.all()
    context = {
        'madlibslist': madlibslist
    }
    return render(request, 'madlibs/stories.html', context)

def story_detail(request, madlibs_id):
    madlib = get_object_or_404(madlibs, pk=madlibs_id)
    context = {
        'madlib': madlib,
        'story_text': madlib.story_text
    }
    return render(request, 'madlibs/story_detail.html', context)