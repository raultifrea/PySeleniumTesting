import unittest

#from personalprojects.Digi24.Pages.Digi24_Home import Defs
from Digi24.Pages.Digi24_Home import Defs

class TestNavMenuLinks(unittest.TestCase):

    NavMenuLinks = Defs()
    NavMenuLinks.load()
    NavMenuLinks.click_Nav_Menu_button()
    NavMenuLinks.get_nav_menu_links()
    NavMenuLinks.quit()

if __name__ == "__main__":
    unittest.main()