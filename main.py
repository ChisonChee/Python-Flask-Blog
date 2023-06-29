from flask import Flask, render_template, request
import requests
import smtplib

content_api = "https://api.npoint.io/d9e60425ed5e4d22d2bf"
data = requests.get(url=content_api).json()

app = Flask(__name__)


@app.route("/")
def home_page():
    data_index = len(data)
    return render_template("index.html", content=data, data_size=data_index)


@app.route("/contact", methods=['GET', 'POST'])
def contact_page():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        my_email = "udemy.testing.day32@gmail.com"
        receiver_addr = email
        pw = "aefjqwdzfzndffwl"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=pw)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=receiver_addr,
                msg=f"Subject: Connection!\n\nFrom:{name},\n\n{message}\n\n Contact Number: {phone}."
            )

        return render_template("contact.html", response=True)
    else:
        return render_template("contact.html", response=False)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/post/<num>")
def post_page(num):
    content = data[int(num)-1]
    return render_template("post.html", page_content=content)


if __name__ == "__main__":
    app.run(debug=True)