import elasticsearch
import json
import datetime as dt

ES_HOST = 'localhost'   # IP address of the elasticsearch server
ES_PORT = 9200  # Port on which the elasticsearch is listening


def get_number_1003(page=1):
    # Connection to the elasticsearch server
    es = elasticsearch.Elasticsearch([{'host': ES_HOST, 'port': ES_PORT}])
    size = 5   # Number of data to get from the elasticsearch database
    offset = size * (page - 1)  # Offset from which to start collecting data

    query = {   # Query written in the DSL format
        "sort": [
            {
                "@timestamp": {"order": "desc"}},
        ],
        'from': offset,
        'size': size,
        'query':
        {
    "bool": {
      "must": [
        {
          "term": {
            "type": "wineventlog"
          }
        },
        {
          "term": {
            "log_name": "Microsoft-Windows-Sysmon/Operational"
          }
        },
        {
          "bool": {
            "should": {
              "bool": {
                "must": {
                  "match": {
                    "mitre_technique_id": {
                      "query": "T1003",
                      
                    }
                  }
                }
              }
            }
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
    return int(result['hits']['total'])        


def get_number_1086(page=1):
    # Connection to the elasticsearch server
    es = elasticsearch.Elasticsearch([{'host': ES_HOST, 'port': ES_PORT}])
    size = 5   # Number of data to get from the elasticsearch database
    offset = size * (page - 1)  # Offset from which to start collecting data

    query = {   # Query written in the DSL format
        "sort": [
            {
                "@timestamp": {"order": "desc"}},
        ],
        'from': offset,
        'size': size,
        'query':
        {
    "bool": {
      "must": [
        {
          "term": {
            "type": "wineventlog"
          }
        },
        {
          "term": {
            "log_name": "Microsoft-Windows-Sysmon/Operational"
          }
        },
        {
          "bool": {
            "should": {
              "bool": {
                "must": {
                  "match": {
                    "mitre_technique_id": {
                      "query": "T1086",
                      
                    }
                  }
                }
              }
            }
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
    return int(result['hits']['total'])        

def get_number_1027(page=1):
    # Connection to the elasticsearch server
    es = elasticsearch.Elasticsearch([{'host': ES_HOST, 'port': ES_PORT}])
    size = 5   # Number of data to get from the elasticsearch database
    offset = size * (page - 1)  # Offset from which to start collecting data

    query = {   # Query written in the DSL format
        "sort": [
            {
                "@timestamp": {"order": "desc"}},
        ],
        'from': offset,
        'size': size,
        'query':
        {
    "bool": {
      "must": [
        {
          "term": {
            "type": "wineventlog"
          }
        },
        {
          "term": {
            "log_name": "Microsoft-Windows-Sysmon/Operational"
          }
        },
        {
          "bool": {
            "should": {
              "bool": {
                "must": {
                  "match": {
                    "mitre_technique_id": {
                      "query": "T1027",
                      
                    }
                  }
                }
              }
            }
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
    return int(result['hits']['total'])        

def get_number_1136(page=1):
    # Connection to the elasticsearch server
    es = elasticsearch.Elasticsearch([{'host': ES_HOST, 'port': ES_PORT}])
    size = 5   # Number of data to get from the elasticsearch database
    offset = size * (page - 1)  # Offset from which to start collecting data

    query = {   # Query written in the DSL format
        "sort": [
            {
                "@timestamp": {"order": "desc"}},
        ],
        'from': offset,
        'size': size,
        'query':
        {
    "bool": {
      "must": [
        {
          "term": {
            "type": "wineventlog"
          }
        },
        {
          "term": {
            "log_name": "Microsoft-Windows-Sysmon/Operational"
          }
        },
        {
          "bool": {
            "should": {
              "bool": {
                "must": {
                  "match": {
                    "mitre_technique_id": {
                      "query": "T1136",
                      
                    }
                  }
                }
              }
            }
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
    return int(result['hits']['total'])        


def get_logs(page=1):
    es = elasticsearch.Elasticsearch([{'host': ES_HOST, 'port': ES_PORT}])
    size = 5   # Number of data to get from the elasticsearch database
    offset = size * (page - 1)  # Offset from which to start collecting data

    query = {  
        "sort": [
            {
                "@timestamp": {"order": "desc"}},
        ],
        'from': offset,
        'size': size,
        'query':
        {
    "bool": {
      "must": [
        {
          "term": {
            "type": "wineventlog"
          }
        },
        {
          "term": {
            "log_name": "Microsoft-Windows-Sysmon/Operational"
          }
        },
        {
          "bool": {
            "should": {
              "bool": {
                "must": {
                  "match": {
                    "mitre_technique_id": {
                      "query": "T1003",
                      
                    }
                  }
                }
              }
            }
          }
        }
      ]
    }
    }
    }
    result = es.search(index='win*', body=query,
                       filter_path=['hits.total', 'hits.hits._source'])
    if int(result['hits']['total']) > 0:
        return extract_logs(result['hits']['hits'], '_source')
    else:   
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
