# Ex.05 Design a Website for Server Side Processing
## Date:22/11/2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
 area = length * breadth

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<title>Area of a Rectangle</title>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<link rel="stylesheet" href="math.css" />
<style>

    * {
        padding: 0;
        margin: 0;
        color: #222020;
    }


    h1 {
        margin-bottom: 10px;
    }


    .container {
        background-color: #fbfbfb;
        height: 100vh;
        width: 100vw;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: sans-serif;
    }

    .box {
        background-color: #f1f1f1;
        width: fit-content;
        height: fit-content;
        padding: 30px 50px;
        border-radius: 18px;
        box-shadow: rgba(0, 0, 0, 0.15) 0px 5px 15px 0px;   
        text-align: center;
    }

    .form-box {
        margin-top: 20px;
        height: 200px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    form {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
    }

    .formelt {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .input {
        width: 40px;
        height: 25px;
        text-align: center;
        border: 1px solid #898989;
        border-radius: 5px;
    }

    .button {
        padding: 10px 25px;
        margin: 0px auto;
        border-radius: 8px;
        font-size: 16px;
        border: none;
        cursor: pointer;
        color: #ffffff;
        background-color: #fd5732;
        transition: transform 0.3s;
    }

    .button:hover {
        transform: translateY(-3px);
    }

    .result {
        width: 130px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 5px;
    }

    .final {
        border: none;
        background-color: transparent;
        font-size: 18px;
        font-weight: bold;
        width: 60px;
    }

    span {
        color: #fd5732;
    }


</style>
</head>
<body>
<div class="container">
    <div class="box">
        <h1>Area of a <span>Rectangle</span></h1>
        <h3>Name: <span>Mohamed Rafeek</span> Ref.No: <span>24900640</span></h3>
        <div class="form-box">
            <form method="POST">
                {% csrf_token %}
                <div class="formelt">
                    Breadth : <div><input class="input" type="text" name="length" value="{{ h }}"> m<br/></div>
                </div>
                <div class="formelt">
                    Length : <div><input class="input" type="text" name="breadth" value="{{ r }}"> m<br/></div>
                </div>
                <div class="formelt">
                    <input type="submit" class="button" value="Calculate"><br/>
                </div>
                <div class="formelt result">
                    Surface Area: <div><input class="input final" type="text" name="area" value="{{ area }}" readonly> m<sup>2</sup><br/></div>
                </div>
            </form>
        </div>
        
    </div>
</div>
</body>
</html>

views.py

from django.shortcuts import render

def rectarea(request):
    context = {
        'area': "0",
        'r': "0",
        'h': "0"
    }
    if request.method == 'POST':
        print("POST method is used")
        r = request.POST.get('breadth', '0')
        h = request.POST.get('length', '0')
        
        try:
            breadth = float(r)
            length = float(h)
            
            # Calculate surface area of the rectangle
            area = length * breadth
            context['area'] = round(area, 2)
            context['r'] = r
            context['h'] = h
            print('length=', length)
            print('breadth=', breadth)
            print('Surface Area=', area)
        except ValueError:
            context['area'] = "Invalid input"
            print("Invalid input provided")
            
    return render(request, 'mathapp/math.html', context)


urls.py

from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('areaofrectangle/',views.rectarea,name="areaofrectangle"),
    path('',views.rectarea,name="areaofrectangleroot")
]

```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (21).png>)
## HOMEPAGE:
![alt text](<Screenshot (19).png>)

## RESULT:
The program for performing server side processing is completed successfully.
