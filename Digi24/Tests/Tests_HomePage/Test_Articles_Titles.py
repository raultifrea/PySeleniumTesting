import unittest

#from personalprojects.Digi24.Pages.Digi24_Home import Defs
from Digi24.Pages.Digi24_Home import Defs

class TestArticlesTitles(unittest.TestCase):

    articles = Defs()
    articles.load()
    articles.get_articles_titles()
    articles.quit()

if __name__ == "__main__":
    unittest.main()