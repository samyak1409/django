# Open cmd in the project root dir, and paste the following command to create sample posts:

"""
python manage.py shell


from json import load
from blog.models import Post


for post in load(open(file='../Resources/Creating Sample Posts/posts.json')):
    Post(title=post['title'], content=post['content'], author_id=post['user_id']).save()

"""
