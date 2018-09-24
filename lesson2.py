import random
from locust import HttpLocust, TaskSet
from data.blog import Blog


website_url = Blog.url()

def print_log(param):
    print(param)

def not_exist(l):
    """Response yakalama ve success olarak işaretleme örneği."""
    with l.client.get("/does_not_exist/", catch_response=True) as response:
        print("Response status code:", response.status_code)
        print("Response content:", response.text)
        if response.status_code == 404:
            response.success()
            #response.failure("No data")

def loop_page(l):
    """Teste isim verme ve döngü parametre geçme örneği."""
    for i in range(1,10):
        l.client.get("/blog?id=%i" % i, name="/blog?id=[id]")

class UserBehavior(TaskSet):
    tasks = {not_exist:1, loop_page:3}

    def on_start(self):
        print_log("Test Başlıyor.")

    def on_stop(self):
        print_log("Test bitiyor.")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
