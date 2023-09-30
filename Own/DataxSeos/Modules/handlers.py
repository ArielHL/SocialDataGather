import pandas as pd
import json
import time
from tqdm import tqdm


def from_json_to_df(path:str=None,
                    is_json:bool=False,
                    data:str=None
                    ) -> pd.DataFrame:
    
    if is_json:
        if path:
            # reading json file
            result=json.loads(path)
        else:
            raise Exception('No path provided')    
        
    else:
        result=data

    # get item list
    item_list=result['tasks'][0]['result'][0]['items']
    
    # Create DataFrame
    df=pd.DataFrame(item_list)
    
    # expand dataframe with rating data
    df= pd.concat([df,df['rating'].apply(pd.Series)],axis=1)
    # expand dataframe with info data
    df= pd.concat([df,df['delivery_info'].apply(lambda x: pd.Series(x, dtype=object))], axis=1)
    df.drop(['rating','delivery_info','xpath'],axis=1,inplace=True)
    
    return df


def checking_task_list(task_id:str,client:object,task_type:str) -> list:

    task_complete=False
    
    while task_complete==False:
        # checking what tasks have been finished
        print('checking_task_list')
        tasks_ready=client.get_task_list(task_type=task_type)

    
        if any(task_id == task for task in tasks_ready):
            print('Task ready')
            task_complete=True
            # get with task_id is ready
            matching_elements=[task for task in tasks_ready if task_id==task]

            print('getting task data')
            # get the response of the task
            response=client.get_task(id=matching_elements[0],task_id=task_type)
            

        else:
            print('Task not ready yet')
            total_seconds=45
            with tqdm(total=total_seconds, desc="Progress") as pbar:
                for i in range(total_seconds):
                    time.sleep(1)  
                    pbar.update(1)  
    
    if task_type=='products':
            print('converting to dataframe')
            # convert the response to a pandas dataframe
            df=from_json_to_df(data=response)
        
            return df
        
    if task_type=='asin':

            return response
            