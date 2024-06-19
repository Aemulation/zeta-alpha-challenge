class Client:
    def __init__(self, n_list: int):
        self.hits = [str(i) for i in range(n_list)]

    def search(self, client_page: int, client_page_size: int) -> list:
        return self.hits[
            (client_page - 1) * client_page_size : (client_page) * client_page_size
        ]


class Searcher:
    def __init__(self, client: Client):
        self.client = client
        self.M = 200

    def search(self, page: int, page_size: int) -> list:
        page = page - 1
        M = self.M
        start_client_page = ((page) * page_size) // M + 1
        num_client_pages = page_size // M + 1

        results = [
            client_result
            for client_page in range(
                start_client_page, start_client_page + num_client_pages + 1
            )
            for client_result in self.client.search(client_page, M)
        ]

        start_index = (page * page_size) % M
        end_index = start_index + page_size
        return results[start_index:end_index]


client = Client(1000)

searcher = Searcher(client)
result = searcher.search(2, 120)
print(result)
