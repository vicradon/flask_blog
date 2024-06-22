from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for blog posts
posts = [
    {
        'id': 1,
        'title': 'First Post',
        'content': 'This is the content of the first post.'
    },
    {
        'id': 2,
        'title': 'Second Post',
        'content': 'This is the content of the second post.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return "Post not found!", 404
    return render_template('post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_id = len(posts) + 1
        posts.append({'id': new_id, 'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
