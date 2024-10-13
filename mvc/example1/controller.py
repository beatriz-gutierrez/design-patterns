# Redirect function is used to forward user to full url if he came
# from shortened
# Request is used to encapsulate HTTP request. It will contain request
# methods, request arguments and other related information
from flask import redirect, render_template, request, Flask
from werkzeug.exceptions import BadRequest, NotFound

from models import Url

# Initialize Flask application
app = Flask(__name__, template_folder="views")


@app.route("/")
def index():
    """Renders main page."""
    return render_template("main_page.html")


@app.route("/shorten/")
def shorten():
    """Returns short_url of requested full_url."""
    # Validate user input
    full_url = request.args.get("url")
    if not full_url:
        raise BadRequest()

    # Pass data to view and call its render method
    short_url = request.host + "/" + Url.shorten(full_url)
    return render_template("success_short.html", url=short_url)


@app.route("/redirect_to_full/")
def redirect_to_full(path=""):
    """Gets short url and redirects user to corresponding full url if found."""
    # Model returns object with full_url property
    short_url = request.args.get("path")
    if not short_url:
        raise BadRequest()

    long_url = Url.get_by_short_url(short_url)
    return redirect("https://" + long_url)


@app.route("/lengthen/")
def lengthen():
    short_url = request.args.get("url")
    if not short_url:
        raise BadRequest()

    long_url = Url.get_by_short_url(short_url)
    return render_template("success_long.html", url=long_url)


if __name__ == "__main__":
    app.run(debug=True)
