import elasticsearch
import json
import datetime as dt

ES_HOST = 'localhost'   # IP address of the elasticsearch server
ES_PORT = 9200  # Port on which the elasticsearch is listening


def get_logs(page=1):
    """ The get_logs function connects to the elasticsearch server then searches for all the indexed data
    having 'wineventlog' as value of the 'type' field. size number of data is retrieved starting from offset.
    The offset value is calculated using the page value provided in the parameters of the function.
    Furthermore, all the retrieved data are sorted on the @timestamp field in the ascending order. """

    # Connection to the elasticsearch server
    es = elasticsearch.Elasticsearch([{'host': ES_HOST, 'port': ES_PORT}])
    size = 100   # Number of data to get from the elasticsearch database
    offset = size * (page - 1)  # Offset from which to start collecting data
    # query = {   # Query written in the DSL format
    #     "sort": [
    #         {
    #             "@timestamp": {"order": "desc"}},
    #     ],
    #     'from': offset,
    #     'size': size,
    #     'query':
    #     {
    #         'bool': {
    #             'must': [
    #                 {'term': {'type': 'wineventlog'}},
    #                 {'match': {'event_data.Image': 'python chrome'}}

    #                 # {'bool': {'should': [
    #                 #     {'match': {'event_data.Image': 'python'}},
    #                 #     {'match': {'message.Image': 'chrome'}}
    #                 # ]}}
    #             ]
    #         }
    #     }
    # }
    query = {   # Query written in the DSL format
        "sort": [
            {
                "@timestamp": {"order": "desc"}},
        ],
        'from': offset,
        'size': size,
        'query':
          {
            'bool': {
                'must': [
                    {'term': {'type': 'wineventlog'}},
                    {'term': {'log_name': 'Microsoft-Windows-Sysmon/Operational'}},
                    {
                        'bool': {
                            'should': [
                                {
                                    'bool': {
                                        'must': {'match': {'event_id': 13}} # Registry value set
                                        # 'must': [
                                        #     {'match': {'event_id': 13}}, # Registry value set
                                        #     {'match_phrase_prefix': {
                                        #         # 'message': 'TargetImage: C:\\Windows\\system32\\lsass.exe'
                                        #         'message': 'Image: C:\python\python371\python.exe'
                                        #     }}
                                        # ]
                                    }
                                },
                                {
                                    'bool': {
                                        'must': [
                                            {'match': {'event_id': 10}}, # Process access
                                            # {'match': {'event_id': 2}},
                                            {'match_phrase_prefix': {
                                                'message': 'TargetImage: C:\\Windows\\system32\\lsass.exe'
                                                # 'message': 'Image: C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
                                            }}
                                        ]
                                    }
                                },
                                {
                                    'bool': {
                                        'must': [
                                            {'match': {'event_id': 1}} # Process access
                                                                       
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
      
    }
    # Performing the search
    result = es.search(index='win*', body=query,
                       filter_path=['hits.total', 'hits.hits._source'])
    # If the search hits at least 1 document then extrac the logs
    if int(result['hits']['total']) > 0:
        # Returns the extracted logs
        return extract_logs(result['hits']['hits'], '_source')
    else:   # Otherwise return None
        return None


def extract_logs(logs, attribute):
    """
        The extract_logs function extracts the logs residing under a specific attribute, collects them
        in a list then return the list.
        It takes an itterable containing the attribute from which we want to extract logs and the attribute name.
        If any of the logs' field starts with @ or _ the leading @ or _ is then removed from the extracted log.
    """
    results = []    # The list containing the extracted logs
    for log in logs:    # We itterate over the logs parameter
        obj = {}    # The log dictionary object to be added to the results list
        # We itterate through the key and value items of the dictionary
        for k, v in log[attribute].items():
            if k[0] == '@' or k[0] == '_':  # Removing leading @ or _ from the extracted log
                k = k[1:]
            obj[k] = v  # Adding the key:value pair to the extracted log
            print(f'{k}: "{v}"')
        results.append(obj)  # Appending the extracted log to the results list
    return results  # Return the list
