from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
# get the task results by id
# GET /v3/business_data/google/hotel_info/task_get/advanced/$id
id = "05211451-2692-0282-0000-f0d1d5e9012d"
response = client.get("/v3/business_data/google/hotel_info/task_get/advanced/" + id)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"])) 