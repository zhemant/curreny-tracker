import yaml
import time
from src.currency import tracker

def main():
    # load yml file to dictionary
    config = yaml.load(open('./config.yml'), Loader= yaml.BaseLoader)
    track = tracker(config=config)
    while True:
        try:
            track.refresh_value()
            time.sleep(int(config['refresh_time_min']))
        except KeyboardInterrupt:
                break


if __name__ == '__main__':
    main()