from flask import Flask,render_template,request
import logging
from data import *
from werkzeug.middleware.proxy_fix import ProxyFix
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
@app.route('/')
def hello_world():  # put application's code here
    ip = request.remote_addr
    logging.debug(ip)
    return render_template('index.html', user_ip=ip)

@app.route('/choujiang')
def choujiang():
    # np.random.seed(0)
    # p = np.array(list_probability)
    # h = np.random.choice(list,p = p.ravel())
    txt = str(random.choices(list, list_probability))[2:-2]
    print(txt)
    return render_template('index.html', h = txt)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)       #   debug=True 使得改代码后程序自动运行
