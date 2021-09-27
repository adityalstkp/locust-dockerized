import string
import random
from locust import HttpUser, task, between


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class AttackSSR(HttpUser):
    wait_time = between(1, 2.5)

    def get_artemis(self):
        with self.client.get("/kartu-kredit/", headers={
                "user-agent": "dexter/hammertime, Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1", "Cookie": "_SID_Tokopedia_=" + id_generator()}) as response:
            print("Response code: {}".format(response.status_code))

    # ! uncomment if need another path
    # def get_next(self):
    #     with self.client.get("/kartu-kredit-next") as response:
    #         print("Response code: {}".format(response.status_code))

    @task(1)
    def artemis(self):
        self.get_artemis()

    # ! uncomment if get_next is uncomment
    # @task(1)
    # def next(self):
    #     self.get_next()
