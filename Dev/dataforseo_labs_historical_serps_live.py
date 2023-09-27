from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    keyword="albert einstein",
    location_name="United States",
    language_name="English",
    date_from="2021-08-01",
    date_to="2021-09-01"
)
# POST /v3/dataforseo_labs/google/historical_serps/live
response = client.post("/v3/dataforseo_labs/google/historical_serps/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
