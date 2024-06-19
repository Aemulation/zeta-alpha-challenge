from typing import List


class SearchEngine:
    def __init__(self, n_list: int) -> None:
        self.hits = [str(i) for i in range(n_list)]

    def search(self, client_page: int, client_page_size: int) -> List[str]:
        return self.hits[
            (client_page - 1) * client_page_size : (client_page) * client_page_size
        ]


class SearchAPI:
    def __init__(self, search_engine: SearchEngine, chunk_size: int):
        self.search_engine = search_engine
        self.chunk_size = chunk_size

    def search(self, page: int, page_size: int) -> List[str]:
        page = page - 1
        start_client_page = ((page) * page_size) // self.chunk_size + 1
        num_client_pages = page_size // self.chunk_size + 1

        results = [
            client_result
            for client_page in range(
                start_client_page, start_client_page + num_client_pages + 1
            )
            for client_result in self.search_engine.search(client_page, self.chunk_size)
        ]

        start_index = (page * page_size) % self.chunk_size
        end_index = start_index + page_size
        return results[start_index:end_index]


search_engine = SearchEngine(1000)

search_api = SearchAPI(search_engine, 50)
result = search_api.search(7, 10)
print(result)
