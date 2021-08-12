import bs4, requests
class WebScraper():
  def __init__(self, website, config):
    reqs = requests.get(website)
    if config[0]:
      self.soup = bs4.BeautifulSoup(reqs.text, 'html.parser', parse_only=bs4.SoupStrainer(config[1]))
    else:
      self.soup = bs4.BeautifulSoup(reqs.text, 'html.parser') # strains for all span elements
  def getElementsByClass(className):
    return self.soup.find_all(class_ = className)
