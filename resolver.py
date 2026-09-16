BOOKS = [
    {"id": "1", "title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann"},
    {"id": "2", "title": "Deep Learning", "author": "Ian Goodfellow"}
]

def resolve_book_query(book_id: str, fields: list) -> dict:
    book = next((b for b in BOOKS if b["id"] == book_id), None)
    if not book:
        return {}
    return {k: book[k] for k in fields if k in book}

if __name__ == "__main__":
    print("GraphQL Query Result:", resolve_book_query("1", ["title", "author"]))
