from elasticsearch import Elasticsearch

class MyElasticsearch:

    def __init__(self, host, ca_cert_path, username=None, password=None):
        self.client = Elasticsearch(es_host, ca_certs=ca_cert_path)
        self.username = username
        self.password = password

    def search_index(self, index_name, query):
        """
        Search an Elasticsearch index with a given query.

        Args:
            index_name (str): The name of the Elasticsearch index to search.
            query (dict): The Elasticsearch query DSL in dictionary format.

        Returns:
            dict: The search results as a dictionary.
        """
        response = self.client.options(basic_auth=(self.username, self.password)).search(index=index_name, body=query)

        return response
