import pandas as pd
import json
import time
from tqdm import tqdm
import validators
from urllib.parse import urlparse
import pathlib
from json.decoder import JSONDecodeError


def from_json_to_df(
                    path:str=None,
                    is_json:bool=False,
                    data:str=None
                    ) -> pd.DataFrame:
    
    if is_json:
        if path:
            # reading json file
            result=read_json_to_dict(filename=path)
        else:
            raise Exception('No path provided')    
    else:
        result=data

    # get item list
    item_list=result['tasks'][0]['result'][0]['items']
    
    # Create DataFrame
    df=pd.json_normalize(item_list)    
    
    return df

    
    

def read_json_path(client,
                merchant:str,
                task_type:str,
                task_id:str):

    # 2. Getting data path for json files
    data=client.get_task_data()['data']
    df_task=pd.DataFrame(data)

    reviews_path=df_task[df_task['task_file_name'].str.contains(task_id)]['task_file_name'].tolist()

    # 3. recover reviews files and transform in dataframes
    final_df=pd.DataFrame()
    for path in reviews_path:
        df=from_json_to_df(merchant=merchant,task_type=task_type,path=path,is_json=True)
        final_df=pd.concat([final_df,df],axis=0)
        
    return final_df
    
        
def save_dict_to_json(filename:str,data_dict:dict):
    if isinstance(filename, pathlib.Path) and isinstance(data_dict, dict):
        
        filename_string=str(filename)
        with open(filename_string, 'w') as outfile:
            json.dump(data_dict, outfile, indent=4)
    else:
        raise Exception('Incorrect input data')
    
def read_json_to_dict(filename:str):
    if isinstance(filename, pathlib.Path) or isinstance(filename, str):
        try:
            with open(filename, 'r') as infile:
                data_dict = json.load(infile)
            return data_dict
        
        except JSONDecodeError:
            raise Exception('Incorrect Json Format')
    else:
        raise Exception('Incorrect input data')


def create_post(client:object,
                api_type:str,
                merchant:str,
                value_to_search:str,
                task_type:str,
                multiple_task:bool=False,
                **kwargs):
    
    if multiple_task==False:
    
        if isinstance(value_to_search, str):
       
            post_data = dict()
            post_data[0] = dict(
                location_name="Germany",
                language_code="en",
                depth = kwargs.get("depth", 10),
                )
            
            if  (task_type == "products" and api_type=='mechant' and merchant == 'amazon') or \
                (task_type == "reviews" and api_type=='business_data' and merchant == 'google'):
                    post_data[0].update(
                        keyword=value_to_search
                    )
                
            if (task_type == "asin" or task_type == 'reviews') and api_type=='mechant':  
                    post_data[0].update(
                        asin=value_to_search
                )
                
            if (task_type =='reviews' and api_type=='business_data' and merchant=='trustpilot'):
                post_data[0].update(
                    domain=value_to_search
                )
                
                
            if (task_type =='app_reviews' and api_type=='app_data' and merchant=='apple'):
                post_data[0].update(
                    app_id=value_to_search
                )
            
            # create a Task
            client.create_task( api_type=api_type, 
                                merchant=merchant,
                                post_data=post_data,
                                task_type=task_type)
        else:
            raise Exception('Incorrect input data')
    
    elif multiple_task==True:
        
        if isinstance(value_to_search, list):
            post_array=[]
            post_data = dict()
            
            for i, value in enumerate(value_to_search):
                
                post_data[i] = dict(
                    location_name="Germany",
                    language_code="en",
                    depth = kwargs.get("depth", 10)
                    )
                                
                if  (task_type == "products" and api_type=='mechant' and merchant == 'amazon') or \
                    (task_type == "reviews" and api_type=='business_data' and merchant == 'google'):
                        post_data[i].update(
                            keyword=value
                    )
                
                if (task_type == "asin" or task_type == 'reviews') and api_type=='mechant':  
                        post_data[i].update(
                            asin=value
                 )
                
                if (task_type =='reviews' and api_type=='business_data' and merchant=='trustpilot'):
                    post_data[i].update(
                        domain=value
                    )
                    
                if (task_type =='app_reviews' and api_type=='app_data' and merchant=='apple'):
                    post_data[i].update(
                        app_id=value
                )
            
                
                post_array.append((post_data[i]))
                

            # create a Task
            client.create_task( api_type=api_type,
                                merchant=merchant,
                                post_data=post_array,
                                task_type=task_type)
        else:
            raise Exception('Incorrect input data')
            
            
def is_valid_website_format(input_string):
    
    if validators.url(input_string):
        value='trustpilot'
    else:
        value=input_string
    
    return value

def create_folder(folder_name:str):
   if not folder_name.exists():
        folder_name.mkdir(parents=True, exist_ok=True) 
        
def create_json_file(filename:str, data:dict):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)