from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = [
    "#"+str(i + 1)+" - Lorem ipsum dolor sit amet." for i in range(12)
]

monthly_challenges_dict = {
    "january": monthly_challenges[0],
    "february": monthly_challenges[1],
    "march": monthly_challenges[2],
    "april": monthly_challenges[3],
    "may": monthly_challenges[4],
    "june": monthly_challenges[5],
    "july": monthly_challenges[6],
    "august": monthly_challenges[7],
    "september": monthly_challenges[8],
    "october": monthly_challenges[9],
    "november": monthly_challenges[10],
    "december": monthly_challenges[11],
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    if not month or month < 0 or month > 12:
        return HttpResponseNotFound('Please enter a valid month number (1 - 12).')
    months = list(monthly_challenges_dict.keys())
    month = months[month - 1]
    url = reverse('month-challenge', args=[month])
    return HttpResponseRedirect(url)


def monthly_challenge(request, month):
    if month not in list(monthly_challenges_dict.keys()):
        return HttpResponseNotFound('Please enter a valid month name (january, ..., december)')
    return HttpResponse(monthly_challenges_dict[month])
