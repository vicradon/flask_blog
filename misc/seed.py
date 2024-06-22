from app import app, db, Post

with app.app_context():
    db.create_all()

    # Seed data
    post1 = Post(title='My first post!', content='This is the content of the first post.')
    post2 = Post(title='Oh what a second post', content='This is the content of the second post.')

    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
