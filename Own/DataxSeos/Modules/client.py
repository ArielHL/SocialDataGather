from http.client import HTTPSConnection
from base64 import b64encode
from json import loads , dumps, dump
import datetime


class RestClient:
    domain = "api.dataforseo.com"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def request(self, path, method, data=None):
        connection = HTTPSConnection(self.domain)
        try:
            base64_bytes = b64encode(
                ("%s:%s" % (self.username, self.password)).encode("ascii")
                ).decode("ascii")
            headers = {'Authorization' : 'Basic %s' %  base64_bytes, 'Content-Encoding' : 'gzip'}
            connection.request(method, path, headers=headers, body=data)
            response = connection.getresponse()
            return loads(response.read().decode())
        finally:
            connection.close()

    def get(self, path):
        return self.request(path, 'GET')

    def post(self, path, data):
        if isinstance(data, str):
            data_str = data
        else:
            data_str = dumps(data)
        return self.request(path, 'POST', data_str)

    # Defining post task
    def create_task(self,
                    post_data:dict,
                    task_type:str) -> str:
        """
        summary:
        
        Creates a task for the specified task type.
        

        Args:
            post_data (dict): data to post to the server for the task creation, needs to be a dictionary
            task_type (str): task type, needs to be a string 
                            options:
                                    products
                                    asin
                                    reviews

        Raises:
            Exception: _description_

        Returns:
            str: response in json
            
            """
        
        
        if isinstance(post_data, dict) and isinstance(task_type, str):
            response = self.post(f"/v3/merchant/amazon/{task_type}/task_post", post_data)
           
            if response["status_code"] == 20000:
                print("Task accepted")
                print("Your task id is: %s." % response["tasks"][0]["id"])
                
                self._response = response
                
                # Saving response to json
                timestamp=datetime.datetime.now()
                current_time=timestamp.strftime("%d-%m-%Y_%H_%M_%S")
                task_id=response['tasks'][0]['id']
                path=f'./Task-Post/task_{task_type}_post_{task_id}_{current_time}.json'
                self.save_response(response=response,path=path)
                
                return task_id

            else:
                print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
        
        else:
            raise Exception("Incorrect input data")
        
        
    # save response to json
    def save_response(self,
                      response:dict,
                      path:str=None) -> None:
        
        with open(path, 'w') as outfile:
            dump(response, outfile, indent=4)   
        

    # Defining get task list
    def get_task_list(self,task_type:str) -> list:
        
        if isinstance(task_type, str):
            response = self.get(f"/v3/merchant/amazon/{task_type}/tasks_ready")
            if response["status_code"] == 20000:
                
                # Saving response to json
                timestamp=datetime.datetime.now()
                current_time=timestamp.strftime("%d-%m-%Y_%H_%M_%S")
                
                path=f'./Task-Get/task_ready_list_{task_type}_{current_time}.json'
                self.save_response(response=response,path=path)
                
                try:
                    task_ready_list_ids=response['tasks'][0]['result']
                    return [task ['id'] for task in task_ready_list_ids]
                except:
                  
                    return []
            
            else:
                print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
        else:
            raise Exception("Incorrect input data")
            
            
    # Defining get task
    def get_task(self,
                 task_id:str,
                 id:str) -> str:
        
        response = self.get(f"/v3/merchant/amazon/{task_id}/task_get/advanced/" + id)
        if response["status_code"] == 20000:
   
            
            # saving data to json
            timestamp=datetime.datetime.now()
            current_time=timestamp.strftime("%d-%m-%Y_%H_%M_%S")
            path=f"./Task-Get/task_get_by_id_{id}_{current_time}.json"
            self.save_response(response=response,path=path)
            
            return response

        else:
            print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))