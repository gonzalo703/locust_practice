from locust import HttpUser, task, constant


class MyLoadTest(HttpUser):

    wait_time = constant(1)

    @task
    def launch(self):
        self.client.get("/")

# locust -f file_name.py -u 1 -r 1 -t 10s --headless --print-stats --csv Run1.csv --csv-full-history
# --host=https://example.com
# -u = users
# -r = respawn rate
# -t = time
# --csv name.csv = save in csv file
# --csv-full-history = show all the activity history
