import finnhub_loader
import mongodb_loader


def extract_load():
    news = finnhub_loader.scrape_news()

    collection = mongodb_loader.load('news', 'finnhub_news')
    if collection is None:
        print("Failed to connect to MongoDB. Skipping data insertion.")
        return

    collection.insert_many(news)
    print("Successfully loaded news to MongoDB")


if __name__ == "__main__":
    extract_load()
