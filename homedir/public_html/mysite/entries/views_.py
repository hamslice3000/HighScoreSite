from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect # redirect needed for back to index after voting
from entries.models import Entry # imports model class and manager
from datetime import datetime # needed for datetime in add below
from django.utils import timezone # timezone needed for datetime
from django.views.decorators.csrf import csrf_protect # protection decorator for POST get


def index(request): 
    context = {
      'latest_entry_list': Entry.objects.order_by('-pub_date')[:10],
      'high_entry_list': Entry.objects.order_by('-score','-pub_date')[:10],
      'high_entry': Entry.objects.order_by('-score','-pub_date')[:1],
      'low_entry_list': Entry.objects.order_by('score','-pub_date')[:10],
      'voting_entry': Entry.objects.unvoted_or_random(),
      'lottery': Entry.objects.random(),
      'lottery_winner': Entry.objects.random(),
    }
    return render(request, 'entries/index.html', context);

def indexHi(request): 
    context = {
      'latest_entry_list': Entry.objects.order_by('-pub_date')[:10],
      'high_entry_list': Entry.objects.order_by('-score','-pub_date')[:10],
      'high_entry': Entry.objects.order_by('-score','-pub_date')[:1],
      'low_entry_list': Entry.objects.order_by('score','-pub_date')[:10],
      'voting_entry': Entry.objects.unvoted_or_random(),
    }
    return render(request, 'entries/indexHi.html', context);

def indexLow(request): 
    context = {
      'latest_entry_list': Entry.objects.order_by('-pub_date')[:10],
      'high_entry_list': Entry.objects.order_by('-score','-pub_date')[:10],
      'high_entry': Entry.objects.order_by('-score','-pub_date')[:1],
      'low_entry_list': Entry.objects.order_by('score','-pub_date')[:10],
      'voting_entry': Entry.objects.unvoted_or_random(),
    }
    return render(request, 'entries/indexLow.html', context);

def indexLat(request): 
    context = {
      'latest_entry_list': Entry.objects.order_by('-pub_date')[:10],
      'high_entry_list': Entry.objects.order_by('-score','-pub_date')[:10],
      'high_entry': Entry.objects.order_by('-score','-pub_date')[:1],
      'low_entry_list': Entry.objects.order_by('score','-pub_date')[:10],
      'voting_entry': Entry.objects.unvoted_or_random(),
    }
    return render(request, 'entries/indexLat.html', context);
    
def add(request):
    created_date = default=datetime.now()
    created_text = request.GET.get('text')    
    e = Entry(text=created_text,pub_date=created_date) 
    e.save()       
    return HttpResponse('done') 

def enter(request):
    return render(request, 'entries/enter.html');
    #return HttpResponse('done')  

def top(request):
    context = {
      'high_entry': Entry.objects.order_by('-score','-pub_date')[:1],
    }
    return render(request, 'entries/top.html', context);

def voting(request):
    context = {'voting_entry': Entry.objects.random(),}      
    return render(request, 'entries/voting.html', context);

def vote(request):
    context = {'vote_entry': Entry.objects.unvoted_or_random(),}      
    return render(request, 'entries/vote.html', context);

def lottery(request): 
    context = {
      'lottery_cycle': Entry.objects.random(),
      'lottery_winner': Entry.objects.random(),
    }
    return render(request, 'entries/lottery.html', context);

def lotteryCycle(request):
    context = {
      'lottery': Entry.objects.random(),
    }
    return render(request, 'entries/lotteryCycle.html', context);

def lotteryWinner(request):
    lottery_id = request.GET.get('lotteryid')
    if request.method=='GET':
        l = Entry.objects.get(pk=lottery_id)
        l.score +=500
        l.save()
        return HttpResponse(l.score)
    else:
        pass
    return HttpResponse('done')

def random_entry(request):
    e = Entry.objects.random()[0]
    return HttpResponse("%s,%s,%s" % (e.id, e.text, e.score))

def vote_entry(request):
    e = Entry.objects.unvoted_or_random()[0]
    return HttpResponse("%s,%s,%s" % (e.id, e.text, e.score))

def entryup(request):
    voting_id = request.GET.get('voteid')
    if request.method=='GET':
        e = Entry.objects.get(pk=voting_id) 
        n = e.get_next_by_pub_date()
        return HttpResponse("%s,%s,%s" % (n.id, n.text, n.score))
    else:
        pass
    return HttpResponse('done')

def entrydown(request):
    voting_id = request.GET.get('voteid')
    if request.method=='GET':
        e = Entry.objects.get(pk=voting_id) 
        n = e.get_previous_by_pub_date()
        return HttpResponse("%s,%s,%s" % (n.id, n.text, n.score))
    else:
        pass
    return HttpResponse('done')

def voteup(request):
    voting_id = request.GET.get('voteid')
    if request.method=='GET':
        v = Entry.objects.get(pk=voting_id)
        v.score +=1
        v.voted=True
        v.save()
        return HttpResponse(v.score)
    else:
        pass
    return HttpResponse('done')   

def votedown(request):
    voting_id = request.GET.get('voteid')
    if request.method=='GET':
        v = Entry.objects.get(pk=voting_id)
        v.score -=1
        v.voted=True
        v.save()
        return HttpResponse(v.score)
    else:
        pass
    return HttpResponse('done') # Only on console
    


    