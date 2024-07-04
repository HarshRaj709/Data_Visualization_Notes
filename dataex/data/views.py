from django.shortcuts import render,redirect
from .models import Languages,Username
from django.urls import reverse
from django.contrib import messages

# Create your views here.
# def home(request,username):
#     users = Username.objects.all()      #given to show list
#     labell = []
#     data = []
#     language = Languages.objects.filter(userlang = username)
#     for label in language:
#         labell.append(label)
#     print(labell)
#     return render(request,'data/home.html',{'users':users,'labels':labell})

def home(request, username):
    users = Username.objects.all()
    labels = ['Python', 'Java', 'Php', 'Cotlin', 'Golang']

    # Fetch the user by username
    user = Username.objects.filter(username=username).first()
    print(user)
    
    if user:
        # Fetch the languages associated with the user
        languages = Languages.objects.filter(User=user).first()     #foreign key always takes id
        
        if languages:
            # Populate the data list with the scores

            # Get all the fields from the Languages model except for the 'User' field
            # language_fields = [field.name for field in Languages._meta.get_fields() if field.name != 'User' and isinstance(field, models.IntegerField)]
            
            # # Populate the data list with the scores dynamically
            # data = [getattr(languages, field) for field in language_fields]
            data = [
                languages.Python,
                languages.Java,
                languages.Php,
                languages.Cotlin,
                languages.Golang
            ]
    
    # Print the labels and data for debugging purposes
    print(labels)
    print(data)
    
    # Render the template with the users, labels, and data
    return render(request, 'data/home.html', {'user':username,'users': users, 'labels': labels, 'data': data})


def username(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        python = request.POST['python']
        java = request.POST['Java']
        php = request.POST['Php']
        cotlin = request.POST['Cotlin']
        golang = request.POST['Golang']
        print(golang)
        if Username.objects.filter(username=username).exists():
            messages.error(request,'Username already registerd, please use different')
            return redirect('username')
        else:
            form = Username(username = username)
            form.save()
            lang = Languages(User = form,Python = python,Java=java,Php=php,Cotlin=cotlin,Golang=golang)
            lang.save()
            return redirect(reverse('home', args=[username])) 
    return render(request,'data/username.html')

