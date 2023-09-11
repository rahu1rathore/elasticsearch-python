from elasticsearch.helpers import scan
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import ElasticSearch
        
class ElkStackSearch(APIView):

    def get(self,request):
        es = ElasticSearch()
        return Response ({"context":es.search_record(request.query_params.get("search_text"))})

    def post(self, request):

        data = request.data.get('data')
        record = ElasticSearch()
        record.insert_record(data)
        return Response ({"context":"data inserted"})

    
class IndexStack(APIView):

    def get(self,request):
        es = ElasticSearch()
        return Response({"context":es.get_index()})

    def post(self,request):    
        record = ElasticSearch()
        return Response ({"context":record.create_index(request.data.get('index_name'))})

    def delete(self,request):
        record = ElasticSearch()
        return Response ({"context":record.delete_record(request.query_params.get("index_name"))})













        

