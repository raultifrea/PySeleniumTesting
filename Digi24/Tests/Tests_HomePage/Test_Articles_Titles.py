import unittest, HtmlTestRunner, os
#from personalprojects.Digi24.Pages.Digi24_Home import Defs
from Digi24.Components.Report_Path import report_path_homepage_workbench
from Digi24.Pages.Digi24_Home import Defs

class TestArticlesTitles(unittest.TestCase):

    def test_article_titles(self):

        articles = Defs()
        articles.load()
        articles.get_articles_titles()
        articles.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path_homepage_workbench))
