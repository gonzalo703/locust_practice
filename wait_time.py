from locust import User, task, constant, between, constant_pacing
import time


class MyUser(User):

    wait_time = constant_pacing(3)

    @task
    def launch(self):
        time.sleep(2)
        print("Constant pacing demo")
