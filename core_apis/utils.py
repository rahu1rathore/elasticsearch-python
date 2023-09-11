from elasticsearch import Elasticsearch

class ElasticAuth:
    def __init__(self):
        self.cloud_id = "CLOUD_ID"
        self.api_key = "API_KEY"
        self.client = Elasticsearch(cloud_id=self.cloud_id, api_key=self.api_key)
        

class ElasticSearch(ElasticAuth):

    def __init__(self):
        super().__init__()

    def get_index(self):
        return self.client.indices.get_alias()

    def create_index(self,index_name):
        return self.client.indices.create(index=index_name, ignore=400)

    def search_record(self, text):

        doc = {
                "query": {
                    "match": {
                        "address": text
                    }
                }
            }
        return self.client.search(index='energy01', body=doc,scroll='1m')

    def insert_record(self, obj, target_index='energy01'):

        if not self.client.indices.exists(index="index"):
            self.create_index(target_index)

        result = self.client.index(index=target_index,body=obj)
        return result
        

    def delete_record(self, index_name):
        return self.client.indices.delete(index=index_name, ignore=[400, 404])

