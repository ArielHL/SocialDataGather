from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    task_id="06211235-0696-0139-1000-36727fbd3c90",
    prompt="give a short description of 100 characters",
    include_links=True,
    fetch_content=True,
    suport_extra=True
)
# POST /v3/serp/ai_summary
response = client.post("/v3/serp/ai_summary", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))