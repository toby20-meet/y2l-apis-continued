from flask import Flask, render_template, request
import json
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
    image_url = request.form['url-input']
    # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result, make sure that you read and understand the
    # example we covered in the slides! 

    # YOUR CODE HERE!
    headers = {'Authorization': 'Key 7c097f6c67ed4e9e9f55f74b932b6281'}
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}
    response = requests.post(api_url, headers=headers, data = json.dumps(data))
    print(response.status_code)
    response_json = json.loads(response.content)
    response_list = response_json["outputs"][0]["data"]["concepts"]
    send_list = []
    for i in response_list:
    	send_list.append(i["name"])
    print(response_list)
    return render_template('home.html', results=send_list)

if __name__ == '__main__':
    app.run(debug=True)