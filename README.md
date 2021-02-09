# curreny-tracker
Track currency rate updates

When you want to convert money, we always look for good rate. This app gives periodic updates about latest currency rates as notification. 

The API has to be added in config.yml. The example config file is given. 
```yaml
url: https://api.testexchange.com?base=EUR
api-key: abcdef
currency: INR
up-symbol: currency/media/up.png
down-symbol: currency/media/down.png
alert-tone: currency/media/mt.wav
refresh_time_min: 1 
```

# Usage

#### Requirements
pip3 install -r requirements.txt

#### Run program
python3 -m currency
or 
python3 currency/currency.py
