from django.shortcuts import render


# Create your views here.


posts = [
    {
        'title': 'Post 1',
        'author': 'Samyak Jain',
        'date': '13 January 2023',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque eligendi excepturi quam quia, repellendus saepe similique. Accusamus amet aperiam aspernatur, assumenda consequuntur delectus dolor excepturi iure labore molestiae mollitia nihil nobis officia optio perferendis quaerat, repellat, repellendus sequi sunt tempora veniam vero voluptates! Accusantium libero, maiores minima mollitia obcaecati quo similique ut vitae! Alias aliquam animi aperiam aspernatur consequuntur corporis culpa dicta eius esse eveniet explicabo facilis, hic ipsa itaque magni maxime molestias mollitia natus necessitatibus nisi numquam odio perferendis porro praesentium quaerat qui quidem quod reiciendis repudiandae sequi suscipit temporibus tenetur totam unde velit voluptates voluptatum. Quam, vel, voluptatum.'
    },
    {
        'title': 'Post 2',
        'author': 'Samyak Jain',
        'date': '13 January 2023',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aliquam aut blanditiis consequuntur culpa cumque dolorum eius est et facere facilis harum ipsa ipsam ipsum laudantium libero magni maiores minima modi nesciunt numquam odio officiis perferendis perspiciatis porro praesentium quas ratione reprehenderit rerum sint soluta tempora tempore, vel veniam voluptatum.'
    }
]  # let's just pretend for now that we made a database call and got back this list of posts, and we want to display
# these posts on our blog homepage


def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request=request, template_name='blog/home.html', context=context)
    # views always need to return either an `HttpResponse` or an `Exception`
    # [Part 3 - Templates](https://youtu.be/qDwdMDQ8oX4)


def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
