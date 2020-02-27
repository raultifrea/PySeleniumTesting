import unittest, HtmlTestRunner, os
#from personalprojects.Digi24.Pages.Digi24_Home import Defs
from Digi24.Pages.Digi24_Home import Defs

class TestArticlesTitles(unittest.TestCase):

    def test_article_titles(self):

        articles = Defs()
        articles.load()
        articles.get_articles_titles()
        articles.quit()


if __name__ == "__main__":

    #path = r'\personalprojects\Digi24\Reports'
    #start = r'D:\Automation'
    #relpath = os.path.relpath(path, start)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'D:\Automation\personalprojects\Digi24\Reports'))
