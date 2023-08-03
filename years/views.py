from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import random
from django.contrib.auth.models import User

# Create your views here.
@login_required
def headlines(request):
    month = str(random.randint(1, 12)).zfill(2)
    if month != "02":
        day = str(random.randint(1, 30)).zfill(2)
    else:
        day = str(random.randint(1, 28)).zfill(2)
    year = str(random.randint(1901, 2022))
    page = f"https://www.nytimes.com/search?dropmab=false&endDate={year}{month}{day}&query=&sort=best&startDate=19000101"
    soup = BeautifulSoup(requests.get(page).content, "html.parser")
    days_list = []
    for h4 in soup.select("h4"):
        text = h4.get_text(strip=True)
        if str(year) not in text:
            days_list.append(text)
    print("day:" + day + " month:" + month + " year:" + year)
    context = {"days_list": days_list, "day":day, "month": month, "year":year}
    return render(request, "years/year_headlines.html", context)


@login_required
def welcome_user(request):
    context = {"person": request.user}
    return render(request, "years/home.html", context)
