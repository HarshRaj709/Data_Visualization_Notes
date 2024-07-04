                            ------------------> CHAPTER 1 <-------------------

        --------------------------------->WITHOUT INVOLVMENT OF DJANGO<-----------------------------


first we will download the chart.js file in our system so that we can use it offline as well.

Basic Chart Structure
const ctx = document.getElementById('myChart');

new Chart(ctx,{
        type:'doughnut',
        data:{
            labels:['python','javascript','php','java','django'],
            datasets: [{
                'data':[10,20,43,11,68],
            }]
        }    
    }
)

---------------------------------------------------------------------------------------------------------------

To set height and widthof canvas then you have to make responsive : false

options:{
            responsive:false, //to make width and height work.
}

---------------------------------------------------------------------------------------------------------------

mostly options comes under the options

like 
    animation
    layout

    Example:

         options:{
            responsive:false, //to make width and height work.
            
            onClick:function(){
                alert('Sticks clicked');
                },
                
            animation: {
                  duration: 1000,
                  easing: 'easeInOutBounce',
                  //loop:true,        // use to make animation continuosly
                },

            layout:{
                padding:{
                    left:50,
                    top:100,
                    bottom:60,
                    },
                }
         }

--------------------------------------------------------------------------------------------------------------

After that plugins is the main option which contains majour elements.

    legend   -  The chart legend displays data about the datasets that are appearing on the chart.

                data:{
            labels:['python','javascript','php','java','django'],
            datasets: [{
                'data':[10,20,43,11,68],
                'label':'Programming Language',                     // this is legend
                'backgroundColor':['red','black','green','lime','brown'],
                'borderColor':['green','red','white','black','blue'],
                'borderWidth':3,


            }]
        },

    title - 
            title:{
                    display:true,
                    text:'Custom Title',
                    position:'bottom',
                    color:'red',
                    font:{
                        family:'Comic Sans MS',
                        style:'italic',
                        size:50,
                    }
                },
    tooltip- 

                tooltip:{
                    enabled:true,
                    backgroundColor:'red',
                    titleColor:'black',             //use to color the title
                    titleAlign:'center',        // use to align title text {left,ight,center}
                    
                    titleFont:{
                        size:30,
                        style:'italic',
                        family:'Comic Sans MS',
                    },

                    bodyColor:'white',
                    bodyFont:{
                        size:20,
                        style:'underline',
                        family: 'Sarif',
                    },
                    position:'nearest',
                    xAlign:'left',      // it position the tooltip {left,right,center}
                    yAlign:'top',       //it position the tooltip on y axis{top,bottom,center}
                    
                    footerColor:'white',
                
                        },  

---------------------------------------------------------------------------------------------------------------

                            --------------> complete Programme <-----------------

    const ctx = document.getElementById('myChart');

new Chart(ctx,{
        // type:'doughnut',
        type:'bar',
        data:{
            labels:['python','javascript','php','java','django'],
            datasets: [{
                'data':[10,20,43,11,68],
                'label':'Programming Language',
                'backgroundColor':['red','black','green','lime','brown'],
                'borderColor':['green','red','white','black','blue'],
                'borderWidth':3,


            }]
        },
        options:{
            responsive:false, //to make width and height work.
            
            onClick:function(){
                alert('Sticks clicked');
                },
                
            animation: {
                  duration: 1000,
                  easing: 'easeInOutBounce',
                  //loop:true,        // use to make animation continuosly
                },

            layout:{
                padding:{
                    left:50,
                    top:100,
                    bottom:60,
                    },
                },
            scales: {
                y: {
                    min: 10,
                    max: 50,
                }
                

            plugins:{

                legend:{        //label hota h ye jo dataset me diya tha
                    display:true,
                    position:'top',

                    onHover: function(){
                        alert('hovering on legend');
                    },

                    labels:{
                        color:'green',
                        font:{
                            size:20,
                            style:'italic',
                            family:'Comic Sans MS',
                            },
                        boxWidth:200,
                    }
                },

                title:{
                    display:true,
                    text:'Custom Title',
                    position:'bottom',
                    color:'red',
                    font:{
                        family:'Comic Sans MS',
                        style:'italic',
                        size:50,
                    }
                },

                tooltip:{
                    enabled:true,
                    backgroundColor:'red',
                    titleColor:'black',             //use to color the title
                    titleAlign:'center',        // use to align title text {left,ight,center}
                    
                    titleFont:{
                        size:30,
                        style:'italic',
                        family:'Comic Sans MS',
                    },

                    bodyColor:'white',
                    bodyFont:{
                        size:20,
                        style:'underline',
                        family: 'Sarif',
                    },
                    position:'nearest',
                    xAlign:'left',      // it position the tooltip {left,right,center}
                    yAlign:'top',       //it position the tooltip on y axis{top,bottom,center}
                    
                    footerColor:'white',
                
                        },  

                    }
                
            },


    }
)



                                    --------------->Structure<------------------
            
            const ctx = document.getElementById('chart')

new Chart(
    ctx,{
        type:'bar',
        data:{
            labels:[],
            datasets:[],     
        },

        options:{
            reaponsive:false,

            layout:{
                padding:{

                },
            },

            animation:{
                duration:
                easing:
            },

            plugins:{
                legend:{
                    display:,
                    position:,

                    onHover: function(){
                        alert('hovering on legend');
                    },

                    labels:{
                        color:,
                        font:{
                            size:,
                            style:,
                            family:,
                            },
                        boxWidth:200,
                    }
                },
                title:{
                    display:true,
                    text:,
                    position:,
                    color:,
                    font:{
                        family:,
                        style:,
                        size:,
                    }
                },
                tooltip:{

                    enabled:true,
                    backgroundColor:,
                    titleColor:
                    titleAlign:,
                    
                    titleFont:{
                        size:,
                        style:,
                        family:,
                    },

                    bodyColor:,
                    bodyFont:{
                        size:,
                        style:,
                        family:,
                    },
                    position:,
                    xAlign:,      // it position the tooltip {left,right,center}
                    yAlign:,
                    
                    footerColor:,
                },
            }

        }
    }
)

---------------------------------------------------------------------------------------------------------------

                               --------------------> Chapter 2<---------------------
                        
                ------------------------------> Django Involvment <----------------------------


To dynamicaly retrieve the data,
    we first take values as an input from the user to show them there graph ,
    and then store these values into models.
    then retrive those data and pass it to the views and then to html page.


    models.py

        from django.db import models

        # Create your models here.
        class Username(models.Model):
            username = models.CharField(max_length=100)

            def __str__(self):
                return self.username

        class Languages(models.Model):
            User = models.ForeignKey(Username,on_delete=models.CASCADE,related_name='userlang')
            Python = models.IntegerField()
            Java = models.IntegerField()
            Php = models.IntegerField()
            Cotlin = models.IntegerField()
            Golang = models.IntegerField()

---------------------------------------------------------------------------------------------------------------

    views.py

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

---------------------------------------------------------------------------------------------------------------

<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Statistics</title>
    <link rel="stylesheet" href="{% static 'path/to/bootstrap.min.css' %}">
    <style>
        .chart-container {
            display: flex;
            justify-content: space-between;
        }
        .chart-container canvas {
            flex: 1;
            margin: 0 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <!-- First Column: User Names -->
            <!-- Second Column: Statistics -->
            <div class="col-md-8">
                <h2>Statistics : {{user}}</h2>
                <div class="chart-container">
                    <canvas id="chart1" width="700" height="500"></canvas>
                    <canvas id="chart2" width="700" height="500"></canvas>
                </div>
            </div>
            <div class="col-md-4 column">
                {% comment %} <h2>Users:{{user}}</h2> {% endcomment %}
                <ul class="user-list">
                    <!-- Assuming users is a context variable passed from the view -->
                    {% for user in users %}
                        <a href="{% url 'home' user.username %}">{{ user.username }}</a>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
    
    <script src="{% static 'path/to/bootstrap.bundle.min.js' %}"></script>
    <script src="{% static 'data/chart.js' %}"></script>
    <script>
        {% comment %} const ctx = document.getElementById('chart') {% endcomment %}
        function createChart(ctx, type) {
            new Chart(ctx, {
                type: type,
                data: {
                    labels: {{labels|safe}}, //['python','java','php','golang'],
                    datasets: [
                        {
                            data: {{data|safe}},
                            label: '{{user}} Statistics',
                            backgroundColor: ['red', 'blue', 'green', 'yellow', 'orange']
                        }
                    ],     
                },
                options: {
                    responsive: false,
                    animation: {
                        duration: 1000,
                        easing: 'linear',
                    },
                    plugins: {
                        legend: {
                            display: true,
                            position: 'bottom',
                            labels: {
                                color: 'black',
                                font: {
                                    size: 15,
                                    family: 'Comic Sans MS'
                                }
                            }
                        }
                    }
                }
            });
        }

        const barCtx = document.getElementById('chart1').getContext('2d');
        createChart(barCtx, 'bar');
        const doughnutCtx = document.getElementById('chart2').getContext('2d');
        createChart(doughnutCtx, 'polarArea');
    </script>
</body>
</html>

