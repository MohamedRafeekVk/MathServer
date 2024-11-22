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
