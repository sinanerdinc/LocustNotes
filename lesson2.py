import random
from locust import HttpLocust, TaskSet
from data.blog import Blog


website_url = Blog.url()

def print_log(param):
    print(param)

def not_exist(l):
    with l.client.get("/does_not_exist/", catch_response=True) as response:
        print("Response status code:", response.status_code)
        print("Response content:", response.text)
        if response.status_code == 404:
            response.success()

def random_page(l):
    l.client.get(random.choice(website_url))

class UserBehavior(TaskSet):
    tasks = {not_exist:1}

    def on_start(self):
        print_log("Test Başlıyor.")

    def on_stop(self):
        print_log("Test bitiyor.")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
