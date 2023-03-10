from flask import redirect, Flask, render_template, request
from db import get_posts, add_post, delete_post

app = Flask("Tiktok Live")


# index page
@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add_post_page():
    if (request.method == 'POST'):
        print(request.form.to_dict())
        add_post(request.form.to_dict())
        return redirect('/')
    return render_template('add.html')


@app.route('/del/<string:title>')
def delete_post_page(title):
    delete_post(title)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
