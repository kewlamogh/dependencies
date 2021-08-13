import bs4, requests
class WebScraper():
  def __init__(self, website, config):
    reqs = requests.get(website)
    if config[0]:
      self.soup = bs4.BeautifulSoup(reqs.text, 'html.parser', parse_only=bs4.SoupStrainer(config[1]))
    else:
      self.soup = bs4.BeautifulSoup(reqs.text, 'html.parser')
    self.rawText = self.soup.text
    self.rawHTML = self.soup
  def getElementsByClass(self, className):
    return self.soup.find_all(class_ = className)
  def getElementById(self, id):
    return self.soup.find(id = id)
  def getElementByTitle(self,title):
    return self.soup.find(title = title)