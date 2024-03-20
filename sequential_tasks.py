from locust import SequentialTaskSet, HttpUser, constant, task


class MySequentialTask(SequentialTaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Status code 200")

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Status code 500")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MySequentialTask]
    wait_time = constant(1)
