# 30-12-22 Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

say_hello()

def say_bye():
    print("Bye")

decorated_function = delay_decorator(say_bye)
decorated_function()


# Advance Python Decorator Functions
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

# Make sure user is logged in before a post can be created
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
        print(f"This is {user.name}'s new blog post.")

authenticated_user = User("angela")
authenticated_user.is_logged_in = True
create_blog_post(authenticated_user)
# code does not executed because is_logged_in is false
unauthenticated_user = User("jamie")
create_blog_post(unauthenticated_user)