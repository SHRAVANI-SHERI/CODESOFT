import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape article titles from a news website
def scrape_article_titles(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('h2', class_='article-title')  # Adjust based on the actual HTML structure
        
        titles = []
        for article in articles:
            titles.append(article.text.strip())
        
        return titles
    else:
        print(f"Failed to retrieve page: {response.status_code}")
        return None

# Example usage
if __name__ == "__main__":
    url = 'https://example-news-site.com'
    article_titles = scrape_article_titles(url)
    
    if article_titles:
        # Print the titles
        for title in article_titles:
            print(title)
        
        # Store in a CSV file
        with open('article_titles.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Article Titles'])
            for title in article_titles:
                writer.writerow([title])
        print(f"Article titles have been saved to 'article_titles.csv'")
    else:
        print("No article titles found.")
