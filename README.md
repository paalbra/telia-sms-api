# telia-sms-api

## About

Simple API tool for the [Telia](https://www.telia.no/min-side/) SMS webservice.

## Setup

```
pip install git+https://github.com/paalbra/telia-sms-api.git@master
```

## Example

```
import telia
api = telia.TeliaAPI("12345678", "mypassword")
api.send_sms("Hello SMS!", ["12345678"])
```
