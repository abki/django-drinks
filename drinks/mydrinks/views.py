from django import forms
from mydrinks.models import DrinkForm, CommentForm

class DrinkForm(forms.Form):
    name = forms.CharField(max_length=254)
    content = forms.TextField()
    rating = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

def addDrink(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })
