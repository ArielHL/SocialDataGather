from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# example #1 - a simple way to set a task
# this way requires you to specify a location, a language of search, and a keyword.
post_data[len(post_data)] = dict(
    location_code=1023191,
    language_code="en",
    keyword="cheap hotel"
)
# POST /v3/business_data/google/hotel_searches/live
response = client.post("/v3/business_data/google/hotel_searches/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))