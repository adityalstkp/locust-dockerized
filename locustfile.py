from locust import HttpUser, task, between


class AttackSSR(HttpUser):
    wait_time = between(1, 2.5)

    def get_home(self):
        with self.client.get("/coba") as response:
            print("Response code: {}".format(response.status_code))

    def get_about(self):
        with self.client.get("/coba/about") as response:
            print("Response code: {}".format(response.status_code))

    @task(1)
    def home(self):
        self.get_home()

    @task(1)
    def about(self):
        self.get_about()
