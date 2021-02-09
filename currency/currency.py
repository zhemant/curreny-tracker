from notifypy import Notify, exceptions
import requests
import json
import time
import yaml


class tracker:
    def __init__(self, config):
        # API details
        self.url = config["url"]
        self.api_key = config["api-key"]
        # Currency filtering
        self.currency = config["currency"]
        # Symbols
        self.up = config["up-symbol"]
        self.down = config["down-symbol"]
        self.tone = config["alert-tone"]
        # Refresh time
        self.refresh = config["refresh_time_min"]

        # Internal
        self.rate = 0
        self.counter = 0
        self.test_data = config["test_data"]

    def refresh_value(self):
        self.get_data()
        self.notify_msg()

    def get_data(self):
        headers = {"api-key": self.api_key}
        # data = requests.get(self.url, headers = headers)
        # parsed_data = json.loads(data.text)

        parsed_data = json.loads(self.test_data[self.counter])
        self.counter += 1
        if self.counter > len(self.test_data) - 1:
            self.counter = 0
        curr_rate = float("{:.2f}".format(parsed_data["rates"][self.currency]))

        if curr_rate > self.rate:
            self.indicator = self.up
        elif curr_rate < self.rate:
            self.indicator = self.down
        else:
            self.indicator = ""

        self.rate = curr_rate
        self.time = time.strftime("%H:%M:%S", time.localtime(parsed_data["timestamp"]))

    def notify_msg(self):
        notification = Notify()
        notification.title = self.currency
        message = str(self.rate) + "@ \n" + self.time
        notification.message = message
        try:
            notification.audio = self.tone
            notification.icon = self.indicator
            notification.send(block=False)
        except (
            exceptions.InvalidAudioFormat,
            exceptions.InvalidIconPath,
            exceptions.InvalidAudioPath,
        ):
            pass


def main():
    # load yml file to dictionary
    config = yaml.load(open("./config.yml"), Loader=yaml.BaseLoader)
    track = tracker(config=config)
    while True:
        try:
            track.refresh_value()
            time.sleep(int(config["refresh_time_min"]))
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
