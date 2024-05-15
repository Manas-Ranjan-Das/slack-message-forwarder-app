from flask import Flask, render_template, request ,jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form  # Get the JSON data from the request
        url = 'https://hooks.slack.com/services/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'
        data ={
            "text": data.get("text").upper()
        }


        response = requests.post(url, json=data)

        if response.status_code == 200:
            return jsonify({"response_type": "ephemeral","text": "Forwarded Successfully"}), 200
        else:
            return jsonify({"response_type": "ephemeral","text":'Request failed:'+ str(response.status_code)}), 200
        
    else:
        return "This is a Slack app url to receive slash commands"








if __name__ == '__main__':
    app.run(debug=True)