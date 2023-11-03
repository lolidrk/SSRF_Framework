from flask import Flask, request, render_template
# Import model heree
import url_features
import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_ssrf', methods=['POST'])
def check_ssrfs():
    url = request.form.get('url')
    url_features_data = url_features.extract_features_from_url(url)
    result = predict.make_prediction(url_features_data)

    return render_template('result.html', result=result, url=url)

if __name__ == '__main__':
    app.run(debug=True)
