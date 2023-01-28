import os
import requests
import json
from duckduckgo_search import ddg_images
from articles.models import Article

def get_files_in_directory(directory):
    files = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            files.append(path)
    return files

def ddg_image(query):
    results = ddg_images(query)
    for r in results:
        if r["width"] == 1920 and r["height"] == 1080:
            return r

    return results[0]['image']

directory = './FactoidAI/bin/new_dir/2023-01-27_17:41:15_484/'
files_list = get_files_in_directory(directory)

for x in files_list:
    try:
        os.system("API_KEY='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' ./FactoidAI/bin/app a ./FactoidAI/bin/fake_dir/ " + x + " new.json")

        # Load the JSON file
        with open('new.json', 'r') as json_file:
            data = json.load(json_file)

        # Extract the title
        title = data['title']
        print('Title:', title)

        # Extract the date
        date = data['date']
        print('Date:', date)

        # Extract the substring of the topic
        topic = data['topic']

        # Create a paragraph from all the content tags
        content = ""
        for segment in data['segments']:
            content += segment['content'] + "\n\n"

        # Create a list of source URLs
        description = data["sources"][0]['title']
        source_urls = []

        for source in data['sources']:
            source_urls.append(source['url'])

        image = ddg_image(title)
        response = requests.get(image)

        with open("new.jpg", 'wb') as f:
            f.write(response.content)

        a = Article(title=title, description=description, thumbnail="new.jpg", article_text=content, category=topic)

        a.save()
    except KeyboardInterrupt:
        break

    except:
        continue
    
    
    
