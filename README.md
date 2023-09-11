# IMPLEMENTATION OF ELASTICSEARCH WITH PYTHON

## Installation
Use the package manager [pip](https://pypi.org/project/elasticsearch/) to install elasticsearch.

   ```bash
   $ pip install elasticsearch
   ```

## Usage

Connection and authentication of elastic cloud with python client

While connecting to Elastic cloud with python Elasticsearch client,cloud_id parameter is used which can be found within the'Manage Deployment'page after a cluster has been created and api_key which also can be created while cluster creation.

   ```bash
   from elasticsearch import Elasticsearch
   client = Elasticsearch(cloud_id="CLOUD_ID",api_key="API_KEY")
   ```

### CREATE AN INDEX

    client.options().indices.create(index='index_ name', ignore=400)

### GETTING LIST OF ALL INDEXES

    LIST OF ALL INDEXES WILL BE GENERATED.

    result = client.indices.get_alias(index="*")
    for Name in result:
        print(Name)

### ADDING DATA IN INDEX
    
    data = {"username":"XYZ","address":"MP"}
    result = client.index(index='energy06',body=data)
    print("RECORD : {}".format(result))

### QUERY TO FETCH DATA

    query={"query" : {
        "match_all" : {}
    }}

    result = client.search(index="index_name", body=query, size=1000)
    print(result)

### DELETE DOCUMENTS FROM INDEX

    Below query will delete a specific document or item from a particular index on the basis of _id.

    client.delete(index="index_name", id="id")

### DELETE  AN INDEX

    In order to delete a particular index the below query is used.

    client.indices.delete(index='index_name')

## Documentation
For the complete Elasticsearch documentation visit [elastic.co](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
