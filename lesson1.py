import random
from locust import HttpLocust, TaskSet
from data.blog import Blog


website_url = Blog.url()

def print_log(param):
    print(param)

def home_page(l):
    l.client.get("/")

def random_page(l):
    l.client.get(random.choice(website_url))

class UserBehavior(TaskSet):
    tasks = {home_page: 3, random_page:2}

    def on_start(self):
        print_log("Test Başlıyor.")

    def on_stop(self):
        print_log("Test bitiyor.")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
