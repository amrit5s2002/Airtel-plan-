from bs4 import BeautifulSoup
import requests

"""main is used to call all the other functions and perform the required function"""
def main():
    doc=get_topics_page()
    titles = get_topic_titles(doc)
    print(titles)
    desc = get_topic_descs(doc)
    print(desc)

def get_topic_descs(doc):
    """extracting data from GitHub using class name """
    desc_selector = 'f5 color-fg-muted mb-0 mt-1'
    """using find all function to get all p tag content with class name desc _selector"""
    topic_desc_tags = doc.find_all('p', {'class': desc_selector})
    """transfering all titles to topic_titles"""
    topic_descs = []
    for tag in topic_desc_tags:
        topic_descs.append(tag.text.strip())
    return topic_descs

def get_topics_page():
    """specifying url to get the data from page """
    topics_url = 'https://github.com/topics'
    """using get request to collect all the data from GitHub"""
    response = requests.get(topics_url)
    """doc is the object of class Beautifulsoap"""
    doc = BeautifulSoup(response.text, 'html.parser')
    return doc


def get_topic_titles(doc):
    """extracting data from GitHub using class name """
    selection_class = 'f3 lh-condensed mb-0 mt-1 Link--primary'
    """using find all function to get all p tag content with class name desc_selector"""
    topic_title_tags = doc.find_all('p', {'class': selection_class})
    """transfering all titles to topic_titles"""
    topic_titles = []
    for tag in topic_title_tags:
        topic_titles.append(tag.text)
    return topic_titles


"""calling the main fucntion with instruction to call other functions to get titles and description"""
main()