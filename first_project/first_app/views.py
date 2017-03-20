from django.shortcuts import render
#from first_app.models import Topic, Webpage, AccessRecord, User
#from . import forms
#from first_app.forms import SignIn
from first_app.forms import UserForm, UserProfileInfoForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def test_simplepage(request):
    return render(request, 'first_app/test_simplepage.html')

def index(request):
    # webpages_list = AccessRecord.objects.order_by('date')
    # date_dict = {'access_records':webpages_list}
    # return render(request, 'first_app/index.html', context=date_dict)
    return render(request, 'first_app/index.html')

def register(request):
    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'first_app/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def share_screen(request):
    return render(request, 'first_app/share_screen.html')

def settings(request):
    form = forms.Settings()
    user_list = User.objects.order_by('id')
    user_dict = {'user_records':user_list}
    return render(request, 'first_app/settings.html', context=user_dict)

def form_name_view(request):
    form = SignIn()
    if request.method == 'POST':
        form = SignIn(request.POST)

        if form.is_valid():
            # do something code
            print('validation success')
            print('Firstname: ' + form.cleaned_data['firstname'])
            print('Lastname: ' + form.cleaned_data['lastname'])
            print('Email: ' + form.cleaned_data['email'])
            print('Password: ' + form.cleaned_data['password'])
            form.save(commit=True)
            return index(request)
        else:
            print ('Not valid')

    return render(request, 'first_app/form_page.html', {'form':form})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'first_app/sign_in.html', {})
