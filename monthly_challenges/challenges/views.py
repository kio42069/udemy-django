from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no candies",
    "february": "walk for atleast 20 minutes per day",
    "march": "thingues gonna be achieved here",
    "april": "woo hoo",
    "may": "thing",
    "june": "balls",
    "july": "bat",
    "august": "mouse",
    "september": "rat",
    "october": "xdd",
    "november": "kew",
    "december": None
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months" : months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month == 0:
        redirect_month = months[month]
    elif month > len(months):
        return HttpResponseNotFound("Invalid motnh")
    else:
        redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except Exception:
        return Http404()
