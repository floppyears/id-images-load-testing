from locust import HttpLocust, TaskSet, task
from config import *
import random

class UserBehavior(TaskSet):

    @task(80)
    def get_image(self):
        request = api_path + osu_id_with_image
        self.client.get(request, verify=False, auth=(user, password))

    @task(100)
    def get_resized_image(self):
        request = api_path + osu_id_with_image + "?w=" + str(random.randrange(50,250))
        self.client.get(request, verify=False, auth=(user, password))

    @task(20)
    def get_placeholder_image(self):
        request = api_path + osu_id_no_image        
        self.client.get(request, verify=False, auth=(user, password))

    @task(1)
    def get_bad_id(self):
        request = api_path + "5555"    
        with self.client.get(request, 
                             catch_response=True, 
                             verify=False, 
                             auth=(user, password)) as response:
            if response.status_code == 404:
                response.success()

    @task(1)
    def get_regex_id(self):
        request = api_path + "notanid"
        with self.client.get(request, 
                             catch_response=True, 
                             verify=False, 
                             auth=(user, password)) as response:
            if response.status_code == 404:
                response.success()

    @task(2)
    def get_bad_width(self):
        request = api_path + osu_id_with_image + "?w=" + str(random.randrange(2001, 2100))
        with self.client.get(request, 
                             catch_response=True, 
                             verify=False, 
                             auth=(user, password)) as response:
            if response.status_code == 400:
                response.success()

class ApiUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 100
    max_wait = 5000
