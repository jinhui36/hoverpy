# import hoverpy's main class: HoverPy
from hoverpy import HoverPy

# import requests and random for http
import requests

# create our HoverPy object in capture mode
hp = HoverPy(capture=True)

# print the json from our get request. Hoverpy acted as a proxy: it made
# the request on our behalf, captured it, and returned it to us.
print(requests.get("http://ip.jsontest.com/myip").json())

# switch HoverPy to simulate mode. HoverPy no longer acts as a proxy; all
# it does from now on is replay the captured data.
hp.simulate()

# print the json from our get request. This time the data comes from the store.
print(requests.get("http://ip.jsontest.com/myip").json())
