from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    targets=[
        "forbes.com",
		"cnn.com",
		"bbc.com",
		"yelp.com",
		"https://www.apple.com/iphone/",
		"https://ahrefs.com/blog/",
		"ibm.com",
		"https://variety.com/",
		"https://stackoverflow.com/",
		"www.trustpilot.com"
    ]
)
# POST /v3/backlinks/bulk_ranks/live
response = client.post("/v3/backlinks/bulk_ranks/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
