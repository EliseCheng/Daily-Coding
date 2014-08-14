from django.shortcuts import render
#from django.shortcuts import render_to_response

from forms import ContactForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        pass
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})

