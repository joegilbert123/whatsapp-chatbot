from .client import make_request


def jokes(category):
    url = f"https://v2.jokeapi.dev/joke/{category.title()}"
    params = {
        "blacklistFlags": "nsfw,religious,political,racist,sexist,explicit",
        "type": "twopart",
    }
    response = make_request(url, params=params)
    setup, delivery = response.get("setup"), response.get("delivery")
    return setup, delivery


def news(category):
    url = "https://inshortsapi.vercel.app/news"
    params = {"category": category}
    response = make_request(url, params=params)
    response = [
        f"*{i['title']}*\n{i['content']}\n*ReadMore:* {i['readMoreUrl']}\n_{i['author']}{i['date']}_"
        for i in response.get("data")
    ]
    return response


def weather(city):
    params = {"key": "da3eb76c67714939a7a72559230109", "q": city, "aqi": "no"}
    url = "https://api.weatherapi.com/v1/current.json"
    data = make_request(url, params=params)

    response = f"""*_Location_*\n*City*: {data['location']['name']}\n*Region*: {data['location']['region']}\n*Country*: {data['location']['country']}
*Local Time*: {data['location']['localtime']}\n\n*_Weather Data_*\n*Temperature*: {data['current']['temp_c']}°C/{data['current']['temp_f']}°F
*Feels Like*: {data['current']['feelslike_c']}°C/{data['current']['feelslike_f']}°F\n*Condition*: {data['current']['condition']['text']}
*Wind*: {data['current']['wind_kph']} kph / {data['current']['wind_mph']} mph\n*Wind Degree*: {data['current']['wind_degree']}°\n*Wind Direction*: {data['current']['wind_dir']}\n*Humidity*: {data['current']['humidity']}%\n*Cloud*: {data['current']['cloud']}%\n*UV*: {data['current']['uv']}
"""
    return response


def quotes(category):
    url = "https://api.quotable.io/random"
    params = {"tags": category}
    data = make_request(url, params=params)
    content, author = data.get("content"), data.get("author")
    response = f"*{content}*\n_by {author}_"
    return response


def developer():
    attrs = {
        "*Name*": "UpSkilled",
        "email": "support@upskilled.ai",
        "phone": "+91 99941 57622",
    }
    return "\n\n".join([f"{k}: {v}" for k, v in attrs.items()])


def help():
    services = {
        "*Jokes*": "(_.jokes_) returns jokes _caegories_(Programming,Miscellaneous,Dark,Pun,Spooky,Christmas) default random",
        "*News*": '(_.news <category>_) returns news based on the category provided default ("national")\n_categories_:  "national", "business", "sports", "world", "politics", "technology", "startup", "entertainment", "miscellaneous", "hatke", "science", "automobile"',
        "*Weather*": "(_.weather_ <city>) returns weather for the city",
        "*Youtube*": "(_.youtube_ <url>) returns youtube download links",
        "*Quotes*": "(_.quotes_ <category>) returns a random quote from the category provided",
        "*Help*": "(_.help_) returns this message",
    }

    return "\n\n".join([f"{k}: {v}" for k, v in services.items()])
