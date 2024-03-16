from flask import Flask, request
from utils.mapper import JsonRequest, JsonResponse
from utils.services import jokes, news, weather, help, quotes, developer
from utils.converstion import chat
from utils.ytd import youtube

app = Flask(__name__)
cmd = "."


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        data = JsonRequest(**request.json)
        message = data.query.message

        if message.startswith(cmd + "joke"):
            category = (
                message.split()[1]
                if len(message.split()) > 1
                else "Programming,Miscellaneous,Dark,Pun,Spooky,Christmas"
            )
            return JsonResponse(jokes(category)).json()

        elif message.startswith(cmd + "news"):
            category = message.split()[1] if len(message.split()) > 1 else "national"
            return JsonResponse(news(category)).json()

        elif message.startswith(cmd + "weather"):
            city = message.split()[1] if len(message.split()) > 1 else "nan"
            if city == "nan":
                return JsonResponse("Povide city name ex. (.weather coimbatore)").json()
            return JsonResponse(weather(city)).json()

        elif message.startswith(cmd + "ytd"):
            url = message.split()[1] if len(message.split()) > 1 else "nan"
            if url == "nan":
                return JsonResponse(
                    "Povide youtube url ex. (.ytd https://youtu.be/o9-ObGgfpEk?si=VL5fpbTkOJjJiZfE)"
                ).json()
            return JsonResponse(youtube(url)).json()

        elif message.startswith(cmd + "quotes"):
            category = (
                message.split()[1] if len(message.split()) > 1 else "famous-quotes"
            )
            return JsonResponse(quotes(category)).json()

        elif message.startswith(cmd + "help"):
            return JsonResponse(help()).json()

        elif message.startswith(cmd + "dev"):
            return JsonResponse(developer()).json()

        else:
            return JsonResponse(chat(message)).json()
    elif request.method == "GET":
        return JsonResponse("Endpoint working").json()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
