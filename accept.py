from flask import Flask, request, render_template
# Import model hereee

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_ssrf', methods=['POST'])
def check_ssrfs():
    url = request.form.get('url')
    # get result here
    result = 'malicious'

    return render_template('result.html', result=result, url=url)

if __name__ == '__main__':
    app.run(debug=True)
