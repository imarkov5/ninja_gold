from django.shortcuts import render,redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'total_gold' not in request.session or 'activities' not in request.session or 'counter' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
        request.session['counter'] = 0
    return render(request, 'index.html')

def process(request):
    if request.method == "POST":
        # request.session['money_goal'] = request.POST['money_goal']
        # print(request.session['money_goal'])
        if request.POST['location'] == 'farm':
            gold = int(random.random()*10 + 10)
            request.session['activities'].append(f"Earned {gold} golds from the {request.POST['location']}! ({datetime.now().strftime('%Y-%m-%d %H:%M')})")
        elif request.POST['location'] == 'cave':
            gold = int(random.random()*5 + 5)
            request.session['activities'].append(f"Earned {gold} golds from the {request.POST['location']}! ({datetime.now().strftime('%Y-%m-%d %H:%M')})")
        elif request.POST['location'] == 'house':
            gold = int(random.random()*3 + 2)
            request.session['activities'].append(f"Earned {gold} golds from the {request.POST['location']}! ({datetime.now().strftime('%Y-%m-%d %H:%M')})")
        elif request.POST['location'] == 'casino':
            gold = int(random.random()*100 - 50)
            if gold > 0:
                request.session['activities'].append(f"Entered a {request.POST['location']} and won {gold} golds! ({datetime.now().strftime('%Y-%m-%d %H:%M')})")
            else:
                request.session['activities'].append(f" Entered a {request.POST['location']} and lost {abs(gold)} golds... Ouch.. ({datetime.now().strftime('%Y-%m-%d %H:%M')})") 
        request.session['total_gold'] += gold
        request.session['counter'] += 1
        if request.session['total_gold'] > 100:
            request.session['game_over'] = 'YOU WON!!!'
        if request.session['counter'] > 7:
            request.session['game_over'] = 'GAME OVER!!!'

    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')