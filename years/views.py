from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
import random
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY= os.getenv("NYT_API_KEY")
# Create your views here.

@login_required
def headlines(request):
    year = str(random.randint(1901, 2022))
    print("year",year)
    # Create the API request URL
    api_url = f"https://api.nytimes.com/svc/archive/v1/{year}/1.json?api-key={API_KEY}"

    # Send a GET request to the API URL
    response = requests.get(api_url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the headlines from the response
        headlines_list = [doc['headline']['main'] for doc in data['response']['docs']]

        # Randomly select 10 headlines
        selected_headlines = random.sample(headlines_list, 10)

        context = {"days_list": selected_headlines, "year": year}
        return render(request, "years/year_headlines.html", context)
    else:
        # Handle the case where the API request fails
        error_message = "Failed to retrieve headlines."
        context = {"error_message": error_message}
        return render(request, "error.html", context)

@login_required
def welcome_user(request):
    context = {"person": request.user}
    return render(request, "years/home.html", context)
