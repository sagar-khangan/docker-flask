import time
from flask import Flask,render_template

# import the flask extension
from flask.ext.cache import Cache   

app = Flask(__name__)

# define the cache config keys, remember that it can be done in a settings file
app.config['CACHE_TYPE'] = 'simple'

# register the cache instance and binds it on to your app 
app.cache = Cache(app)   

@app.route("/")
@app.cache.cached(timeout=300)  # cache this view for 5 minutes
def cached_view():
    return render_template('/home.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')