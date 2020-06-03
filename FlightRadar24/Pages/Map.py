from selenium.webdriver.common.keys import Keys

from FlightRadar24.Components.Components import Component
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class Defs(Component):
    URL = 'https://www.flightradar24.com'
    About_locator = (By.XPATH, "//*[@class='important-banner__footer']//child::button")
    LogIn_locator = (By.XPATH, "//*[@class='dropdown-toggle logout']")
    Email_locator = (By.XPATH, "//*[@id='fr24_SignInEmail']")
    Password_locator = (By.XPATH, "//*[@id='fr24_SignInPassword']")
    SignIn_locator = (By.XPATH, "//*[@id='fr24_SignIn']")
    Login_text_locator = (By.XPATH, "//*[contains(text(),'Login authorization succeeded')]")
    Settings_button_locator = (By.XPATH, "//*[@id='fr24_SettingsMenu']")
    Settings_Map_MapStyle_dropdown_locator = (By.XPATH, '//*[@id="fr24_mapType"]/button')
    Settings_Map_MapStyle_list_locator = (By.XPATH, "//*[@id='fr24_mapType']//descendant::a")
    Settings_Map_ATCBoundaries_dropdown_locator = (By.XPATH, '//*[@id="fr24_showATC"]/button')
    Settings_Map_ATCBoundaries_list_locator = (By.XPATH, '//*[@id="fr24_showATC"]//descendant::a')
    Settings_Map_Aeronautical_Charts_dropdown_locator = (By.XPATH, '//*[@id="fr24_showNavdataLayer"]/button')
    Settings_Map_Aeronautical_Charts_list_locator = (By.XPATH, '//*[@id="fr24_showNavdataLayer"]//descendant::a')
    Settings_Map_Aircraft_Size_dropdown_locator = (By.XPATH, '//*[@id="fr24_aircraftSize"]/button')
    Settings_Map_Aircraft_Size_list_locator = (By.XPATH, '//*[@id="fr24_aircraftSize"]//descendant::a')
    Settings_Map_Aircraft_Labels1_dropdown_locator = (By.XPATH, '//*[@id="fr24_aircraftLabel1"]/button')
    Settings_Map_Aircraft_Labels1_list_locator = (By.XPATH, '//*[@id="fr24_aircraftLabel1"]//descendant::a')
    Settings_Map_Aircraft_Labels2_dropdown_locator = (By.XPATH, '//*[@id="fr24_aircraftLabel2"]/button')
    Settings_Map_Aircraft_Labels2_list_locator = (By.XPATH, '//*[@id="fr24_aircraftLabel2"]//descendant::a')
    Settings_Map_Aircraft_Labels3_dropdown_locator = (By.XPATH, '//*[@id="fr24_aircraftLabel3"]/button')
    Settings_Map_Aircraft_Labels3_list_locator = (By.XPATH, '//*[@id="fr24_aircraftLabel3"]//descendant::a')
    Settings_Map_Aircraft_Labels4_dropdown_locator = (By.XPATH, '//*[@id="fr24_aircraftLabel4"]/button')
    Settings_Map_Aircraft_Labels4_list_locator = (By.XPATH, '//*[@id="fr24_aircraftLabel4"]//descendant::a')
    Settings_Visibility_Estimations_button_locator = (By.XPATH, '//*[@id="fr24_showEstimated"]/button')
    Settings_Visibility_Estimations_list_locator = (By.XPATH, '//*[@id="fr24_showEstimated"]//descendant::a')
    Settings_Map_Brightness_slidebar_locator = (By.XPATH, '//*[@id="fr24_Brightness"]/div')
    Settings_Map_Brightness_slider_locator = (By.XPATH, '//*[@id="fr24_Brightness"]/a')
    Settings_Map_toggles_locator = (By.XPATH, "//*[@id='mapsettings']//div[contains(@class,'toggle')]")
    Settings_Weather_toggles_locator = (By.XPATH, "//div[contains(@class,'weather-tile toggle')]")
    Settings_Visibility_toggles_locator = (By.XPATH, "//div[@id='visibilitysettings']//*[contains(@class,'toggle ')]")
    Settings_Map_slidebar_locator = (By.XPATH, '//*[@id="fr24_airportDensity"]/div')
    Settings_Map_airport_pin_visibility_slider_locator = (By.XPATH, '//*[@id="fr24_airportDensity"]/a')
    Settings_dropdown_default_values_locator = (By.XPATH, "//button[@data-toggle='dropdown']")
    Settings_Weather_button_locator = (By.XPATH, '//*[@id="fr24_SettingsDropdown"]/li[1]/ul/li[2]/a')
    Settings_Visibility_button_locator = (By.XPATH, '//*[@id="fr24_SettingsDropdown"]/li[1]/ul/li[3]/a')
    Settings_Misc_button_locator = (By.XPATH, '//*[@id="fr24_SettingsDropdown"]/li[1]/ul/li[4]/a')
    Settings_Misc_toggles_locator = (By.XPATH, "//div[@id='timesettings']//*[contains(@class,'toggle ')]")
    Settings_Misc_dropdown_buttons_locator = (By.XPATH, "//div[@id='timesettings']//button[contains(@class,'dropdown')]")
    Settings_Misc_dropdown_descendants_locator = (By.XPATH, "//div[@id='timesettings']//*[@class='dropdown-menu']//descendant::a")
    iframe_locator = (By.XPATH, '//*[@id="map_canvas"]/div/div/iframe')
    subscription_plan_locator = (By.XPATH, "//*[@class='subscription']")
    upgrade_popup_close_button_locator = (By.XPATH, '//*[@id="map"]/div[15]/div[1]/a')
    upgrade_popup_title_locator = (By.XPATH, '//*[@id="ui-id-2"]/h2')
    Settings_Reset_button_locator = (By.XPATH, '//*[@id="fr24_SettingsResetButton"]')
    Settings_Reset_button_idle_locator = (By.XPATH, '//*[@class="btn dropdown-toggle btn-danger"]')
    fr_home_logo_button_locator = (By.XPATH, "//*[@class='logo-fr24-flat']")
    FullScreen_button_locator = (By.XPATH, '//*[@id="fr24_Fullscreen"]')
    FullScreen_upgrade_popup_title_locator = (By.XPATH, '//*[@id="ui-id-2"]/h2')
    Map_Body_locator = (By.XPATH, '//*[@id="map"]')
    Filter_button_locator = (By.XPATH, '//*[@id="fr24_FiltersMenu"]')
    Filter_toggle_locator = (By.XPATH, '//*[@id="fr24_enableFilters"]')
    Filter_type_dropdown_locator = (By.XPATH, '//*[@id="fr24_FilterType"]')
    Filter_type_dropdown_descendants_locator = (By.XPATH, '//*[@id="fr24_FilterSettings"]/div/div[3]/ul//descendant::a')
    Filter_inputs_locator = (By.XPATH, '//*[@id="fr24_FilterOptions"]//descendant::input')
    Filter_callsign_input_locator = (By.XPATH, '//*[@id="fr24_FilterBy_callsign"]/input')
    Filter_add_button_locator = (By.XPATH, '//*[@id="fr24_FilterAdd"]')
    Filter_item_locator = (By.XPATH, '//*[@id="fr24_FilterList"]/li/div')
    Filter_sliderbar_locator = (By.XPATH, '//*[@id="fr24_FilterSpeed"]')
    Filter_airport_dropdown_locator = (By.XPATH, '//*[@id="fr24_FilterAirportDirection"]')
    Filter_airport_dropdown_descendants_locator = (By.XPATH, '//*[@id="fr24_FilterBy_airport"]/div//descendant::a')
    Filter_speed_left_slider_locator = (By.XPATH, '//*[@id="fr24_FilterSpeed"]/a[1]')
    Filter_speed_right_slider_locator = (By.XPATH, '//*[@id="fr24_FilterSpeed"]/a[2]')
    Filter_slider_list_locator = (By.XPATH, "//*[@id='fr24_FilterOptions']//a[contains(@class, 'slider')]")
    Filter_limit_locator = (By.XPATH, '//*[@id="fr24_FilterSettings"]/div/p')
    Bookmarks_button_locator = (By.XPATH, '//*[@id="fr24_BookmarksMenu"]')
    Bookmarks_list_locator = (By.XPATH, '//*[@id="bookmarks-start"]/div//descendant::li')
    Bookmarks_Add_tab_locator = (By.XPATH, '//*[@id="fr24_BookmarksDropdown"]/li[1]/ul/li[3]/a')
    Bookmarks_Add_input_locator = (By.XPATH, '//*[@id="saveViewName"]')
    Bookmarks_Add_bookmark_locator = (By.XPATH, '//*[@id="saveViewSubmit"]')
    Bookmarks_Manage_tab_locator = (By.XPATH, "//div[text()='Manage']")
    Bookmarks_MyBookmarks_list_locator = (By.XPATH, "//input[@class='viewName renameView']")
    Bookmarks_MyBookmarks_delete_button_locator = (By.XPATH, ".//following-sibling::a[3]")
    Bookmarks_MyBookmarks_movedown_button_locator = (By.XPATH, ".//following-sibling::a[2]")
    Bookmarks_MyBookmarks_moveup_button_locator = (By.XPATH, ".//following-sibling::a[1]")
    Map_Data_locator = (By.XPATH, '//*[@id="map_canvas"]/div/div/div[4]/div/div[2]/span')
    #Map_nb_of_aircraft_on_map_locator = (By.XPATH, "//div[@class='marker_label'][1]")
    Map_nb_of_aircraft_on_map_locator = (By.XPATH, '//*[@id="menuPlanesValue"]')
    Map_search_box_locator = (By.XPATH, '//*[@id="searchBox"]')
    Map_search_box_autocomplete_locator = (By.XPATH, '//span[contains(text(), "navigate")]')
    Map_airport_pins_locator = (By.XPATH, "//div[contains(@title,'Airport')]//img")
    Map_airport_reviews_locator = (By.XPATH, "//div[@class='reviews']")
    Map_airport_photo_locator = (By.XPATH, '//*[@id="mapStaticOverlays"]/div[5]/section[3]/a')

    def get_list_of_airport_pins(self):
        return self.driver.find_elements(*self.Map_airport_pins_locator)

    def click_airport_pins(self):
        for element in self.get_list_of_airport_pins():
            self.driver.execute_script("arguments[0].click()", element)
            self.wait_for_element_to_be_clickable(self.Map_airport_reviews_locator, self.Map_airport_photo_locator)

    def get_list_of_my_bookmarks(self):
        return self.driver.find_elements(*self.Bookmarks_MyBookmarks_list_locator)

    def click_delete_bookmark(self, item):
        item.find_element(*self.Bookmarks_MyBookmarks_delete_button_locator).click()
        self.driver.switch_to.alert.accept()

    def click_moveup_bookmark(self, item):
        item.find_element(*self.Bookmarks_MyBookmarks_moveup_button_locator).click()

    def click_movedown_bookmark(self, item):
        item.find_element(*self.Bookmarks_MyBookmarks_movedown_button_locator).click()

    def manipulate_bookmark(self, bookmark: str, func):
        '''
        :param func: the function to be passed (delete, moveup, movedown)
        :param bookmark: the string of the custom bookmark saved by the user
        :return: deletes the custom bookmark based on its name, if it's available
        '''
        try:
            self.check_presence_of_bookmark(bookmark)
            for element in self.get_list_of_my_bookmarks():
                if element.get_attribute("value") == bookmark:
                    func(element)
                    time.sleep(3)
        except AssertionError:
            print("There is no bookmark under that name")

    def get_list_of_my_bookmarks_values(self):
        return [bookmark.get_attribute("value") for bookmark in self.driver.find_elements(*self.Bookmarks_MyBookmarks_list_locator)]

    def check_presence_of_bookmark(self, item):
        '''
        :param item: the value of the bookmark to be checked
        :return: checks whether the value is listed within a list of values of all custom bookmark web elements
        '''
        assert item in self.get_list_of_my_bookmarks_values(), "This bookmark is not available"

    @property
    def bookmarks_manage_tab_button(self):
        return self.driver.find_element(*self.Bookmarks_Manage_tab_locator)

    def click_bookmarks_manage_tab_button(self):
        self.bookmarks_manage_tab_button.click()

    @property
    def add_bookmark_button(self):
        return self.driver.find_element(*self.Bookmarks_Add_bookmark_locator)

    def click_add_bookmark_button(self):
        self.add_bookmark_button.click()

    @property
    def bookmarks_add_tab_button(self):
        return self.driver.find_element(*self.Bookmarks_Add_tab_locator)

    def click_bookmarks_add_tab_button(self):
        self.bookmarks_add_tab_button.click()

    @property
    def bookmarks_input_button(self):
        return self.driver.find_element(*self.Bookmarks_Add_input_locator)

    def send_keys_bookmarks_input_button(self, key: str):
        '''
        :param key: the name of the new bookmark in name of a string
        :return: selects a name for the new bookmark and clicks the Add Bookmark button
        '''
        self.bookmarks_input_button.clear()
        self.bookmarks_input_button.send_keys(key)
        self.click_add_bookmark_button()

    @property
    def search_button_autocomplete(self):
        return self.driver.find_element(*self.Map_search_box_autocomplete_locator)

    @property
    def search_button(self):
        return self.driver.find_element(*self.Map_search_box_locator)

    def click_search_button(self):
        self.search_button.click()

    def perform_search(self, key: str):
        '''
        :param key: the string to search for
        :return: searches for the input string and selects it from autocomplete
        '''
        self.search_button.clear()
        self.search_button.send_keys(key)
        self.wait_to_load(self.Map_search_box_autocomplete_locator)
        self.search_button.send_keys(Keys.ENTER)
        #self.wait_for_text_to_change(self.current_nb_of_aircraft_on_map)

    @property
    def current_nb_of_aircraft_on_map(self):
        return self.driver.find_element(*self.Map_nb_of_aircraft_on_map_locator)

    @property
    def bookmarks_button(self):
        return self.driver.find_element(*self.Bookmarks_button_locator)

    def click_bookmarks_button(self):
        self.bookmarks_button.click()

    def get_list_of_bookmarks(self):
        return self.driver.find_elements(*self.Bookmarks_list_locator)

    def click_bookmarks(self):
        '''
        :return: clicks each bookmark and waits for the airport and plane pins to load before moving to the next
        '''
        for bookmark in self.get_list_of_bookmarks():
            self.click_bookmarks_button()
            bookmark.click()
            self.wait_for_text_to_change(self.current_nb_of_aircraft_on_map)

    def get_filter_limit_text(self):
        return self.driver.find_element(*self.Filter_limit_locator).text

    def get_list_of_filter_sliders(self):
        return self.driver.find_elements(*self.Filter_slider_list_locator)

    def get_list_of_filter_airport_descendants(self):
        return self.driver.find_elements(*self.Filter_airport_dropdown_descendants_locator)

    @property
    def filter_airport_dropdown_button(self):
        return self.driver.find_element(*self.Filter_airport_dropdown_locator)

    def click_filter_airport_dropdown_button(self):
        self.filter_airport_dropdown_button.click()

    def get_list_of_filter_inputs(self):
        return self.driver.find_elements(*self.Filter_inputs_locator)

    def get_list_of_filter_descendants(self):
        return self.driver.find_elements(*self.Filter_type_dropdown_descendants_locator)

    def get_filter_item_text(self):
        return self.driver.find_element(*self.Filter_item_locator).text

    @property
    def filter_add_button(self):
        return self.driver.find_element(*self.Filter_add_button_locator)

    def click_filter_add_button(self):
        self.filter_add_button.click()

    @property
    def filter_button(self):
        return self.driver.find_element(*self.Filter_button_locator)

    def click_filter_button(self):
        self.filter_button.click()

    @property
    def filter_toggle_button(self):
        return self.driver.find_element(*self.Filter_toggle_locator)

    def click_filter_toggle(self):
        self.filter_toggle_button.click()

    @property
    def filter_type_dropdown_button(self):
        return self.driver.find_element(*self.Filter_type_dropdown_locator)

    def click_filter_type_dropdown_button(self):
        self.filter_type_dropdown_button.click()

    @property
    def filter_callsign_input_button(self):
        return self.driver.find_element(*self.Filter_callsign_input_locator)

    def click_filter_callsign_input(self):
        self.filter_callsign_input_button.click()

    def send_keys_filter_callsign_input(self, callsign: str):
        '''
        :param callsign: the callsign as a string to be passed in the input field
        :return: fills the input field with a given string representing the callsign
        '''
        self.filter_callsign_input_button.clear()
        self.filter_callsign_input_button.send_keys(callsign)

    def check_filter_text(self, text: str):
        '''
        :param text: the string representing either one of the following: callsign, airport code, aircraft type,
        registration, radar
        :return: checks whether the filter type has been saved
        '''
        assert text.upper() in self.get_filter_item_text(), "Filter was not saved correctly"

    def check_filter_functionality(self, filter_type, text='', inout=''):
        '''
        :param filter_type: the selected filter type from the dropdown list
        :param text: the input text for the selected filter. if filter is of slider type, do not fill
        :param inout: parameter if the filter_type is 'airport'. Can be either 'in or 'out'. Optional
        :return: checks whether the applied filter is saved and checks either the input text (for input field filters)
        or the filter type text (for slider filters)
        '''
        slider_filters = ["Altitude", "Speed"]
        self.click_filter_button()
        if "off" in self.filter_toggle_button.get_attribute("class"):
            self.click_filter_toggle()
        self.click_filter_type_dropdown_button()
        for descendant in self.get_list_of_filter_descendants():
            if filter_type.title() == descendant.text and descendant.text in slider_filters:
                descendant.click()
                self.slide()
                self.click_filter_add_button()
                self.check_filter_text(filter_type)
                break
            elif filter_type.title() == descendant.text:
                descendant.click()
        for input_field in self.get_list_of_filter_inputs():
            if input_field.is_displayed():
                input_field.clear()
                input_field.send_keys(text)
                if filter_type.title() == "Airport" and inout != '':
                    self.click_filter_airport_dropdown_button()
                    for option in self.get_list_of_filter_airport_descendants():
                        if option.text == inout.title():
                            option.click()
                self.click_filter_add_button()
                self.check_filter_text(text)
                break

    def check_filter_limit_text(self, text: str):
        assert text == self.get_filter_limit_text(), "The text doesn't match: " + self.get_filter_limit_text()

    def switch_to_frame(self):
        #not used
        self.driver.switch_to.frame(2)

    @property
    def full_screen_button(self):
        return self.driver.find_element(*self.FullScreen_button_locator)

    def click_full_screen_button(self):
        self.full_screen_button.click()

    def get_full_screen_popup_title_text(self):
        return self.driver.find_element(*self.FullScreen_upgrade_popup_title_locator).text

    def check_full_screen_title_text(self, title: str):
        '''
        :param title: the title string from the upgrade popup, as given in the test file
        :return: checks whether the title is correct in the full screen upgrade popup
        '''
        self.click_full_screen_button()
        assert title == self.get_full_screen_popup_title_text(), "Full Screen title text incorrect"

    def get_map_body(self):
        return self.driver.find_element(*self.Map_Body_locator)

    def check_full_screen_functionality(self):
        '''
        :return: checks whether the full screen mode has been enabled
        '''
        self.click_full_screen_button()
        assert 'fullscreenView' in self.get_map_body().get_attribute('class'), 'Full Screen has not been triggered'

    @property
    def home_logo_button(self):
        return self.driver.find_element(*self.fr_home_logo_button_locator)

    def click_home_logo_button(self):
        return self.home_logo_button.click()

    @property
    def reset_button(self):
        #defines the Reset settings button
        return self.driver.find_element(*self.Settings_Reset_button_locator)

    def click_reset_button(self):
        self.reset_button.click()

    def get_reset_button_text(self):
        return self.reset_button.text

    def check_reset_functionality(self):
        '''
        :return: Validates the text for all the 3 states of the reset button and waits for the refresh at the end
        '''
        assert self.get_reset_button_text() == 'Reset all settings', 'Text is not Reset all settings'
        self.click_reset_button()  # switches to Press to Confirm state
        assert self.get_reset_button_text() == 'Press to Confirm', 'Text is not Press to Confirm'
        self.wait_to_load(self.Settings_Reset_button_idle_locator)
        # The idle reset string is displayed only after about 4 seconds once the button is clicked above
        assert self.get_reset_button_text() in 'Reset to Default', 'Text is not Reset to Default'
        self.click_reset_button()  # switches to Press to Confirm state
        self.click_reset_button()  # performs the Reset
        self.wait_to_load(self.fr_home_logo_button_locator)

    @property
    def brigthness_button_slidebar(self):
        # defines the slide bar
        return self.driver.find_element(*self.Settings_Map_Brightness_slidebar_locator)

    @property
    def brightness_button_slider(self):
        #defines the slider circle
        return self.driver.find_element(*self.Settings_Map_Brightness_slider_locator)

    @property
    def map_slidebar(self):
        #defines the slide bar
        return self.driver.find_element(*self.Settings_Map_slidebar_locator)

    @property
    def filter_slidebar(self):
        return self.driver.find_element(*self.Filter_sliderbar_locator)

    @property
    def filter_speed_left_slider(self):
        return self.driver.find_element(*self.Filter_speed_left_slider_locator)

    @property
    def filter_speed_right_slider(self):
        return self.driver.find_element(*self.Filter_speed_right_slider_locator)

    @property
    def airport_pin_visilibity_slider(self):
        # defines the slider circle
        return self.driver.find_element(*self.Settings_Map_airport_pin_visibility_slider_locator)

    def slide(self):
        # can be expanded to accept multiple sliders
        for element in self.get_list_of_filter_sliders():
            if element.is_displayed():
                self.drag_and_drop_slider(25, element, self.filter_slidebar)
            else:
                continue

    @property
    def email_button(self):
        return self.driver.find_element(*self.Email_locator)

    def click_email_button(self):
        self.email_button.click()

    def send_keys_email_button(self, key: str):
        self.email_button.clear()
        self.email_button.send_keys(key)

    @property
    def password_button(self):
        return self.driver.find_element(*self.Password_locator)

    def click_password_button(self):
        self.password_button.click()

    def send_keys_password_button(self, key: str):
        self.password_button.clear()
        self.password_button.send_keys(key)

    @property
    def login_button(self):
        return self.driver.find_element(*self.LogIn_locator)

    def click_login_button(self):
        self.login_button.click()

    @property
    def sign_in_button(self):
        return self.driver.find_element(*self.SignIn_locator)

    def click_sign_in_button(self):
        self.sign_in_button.click()

    @property
    def settings_button(self):
        return self.driver.find_element(*self.Settings_button_locator)

    def click_settings_button(self):
        self.settings_button.click()

    def get_list_of_default_dropdown_values(self):
        #returns a list of the default drop-down web elements from the Settings menu
        return self.driver.find_elements(*self.Settings_dropdown_default_values_locator)

    def get_list_of_default_dropdown_values_strings(self):
        #returns a list of the default drop-down strings from the Settings menu
        return [element.text for element in self.get_list_of_default_dropdown_values()]

    def check_dropdown_functionality(self, the_list: list, click, title=''):
        '''
        :param title: optional param, in case the feature is locked, check the upgrade popup title text
        :param the_list: the list of all elements in a dropdown list (e.g. get_list_of_map_styles)
        :param click: clicks the button pertaining to the same dropdown list (e.g. click_map_style_button)
        :return: checks whether each dropdown value is saved in the header, one at a time
        '''
        click()
        for element in the_list:
            if element.text != "None":  #first element not clickable
                element.click()
                try:
                    assert self.upgrade_popup_title_text in title, f"incorrect popup title for {self.upgrade_popup_title_text}"
                    self.click_upgrade_popup_close_button()
                    continue
                except NoSuchElementException:
                    assert element.text in self.get_list_of_default_dropdown_values_strings(), f"option: {element.text} is not saved correctly"
            else:
                continue
            click()

    def get_list_of_misc_dropdown_buttons(self):
        return self.driver.find_elements(*self.Settings_Misc_dropdown_buttons_locator)

    def get_list_of_misc_dropdown_descendants(self):
        return self.driver.find_elements(*self.Settings_Misc_dropdown_descendants_locator)

    def check_misc_dropdown_functionality(self):
        '''
        :return: clicks each dropdown button on the misc tab and for each click the dropdown option available
        '''
        list_of_dropdowns = self.get_list_of_misc_dropdown_buttons()
        list_of_descendants = self.get_list_of_misc_dropdown_descendants()
        for element in list_of_dropdowns:
            element.click()
            time.sleep(1)
            for descendant in list_of_descendants:
                if descendant.is_displayed():
                    descendant.click()
                    time.sleep(1)
                    element.click()
                    time.sleep(1)
                else:
                    pass
            element.click()

    @property
    def upgrade_popup_close_button(self):
        return self.driver.find_element(*self.upgrade_popup_close_button_locator)

    def click_upgrade_popup_close_button(self):
        self.upgrade_popup_close_button.click()

    @property
    def upgrade_popup_title_text(self):
        #returns the title of the Upgrade Popup
        return self.driver.find_element(*self.upgrade_popup_title_locator).text

    @property
    def map_style_button(self):
        return self.driver.find_element(*self.Settings_Map_MapStyle_dropdown_locator)

    def click_map_style_button(self):
        self.map_style_button.click()

    def get_list_of_map_styles(self):
        #returns a list of dropdown values from the Map Style options of the Map tab
        return self.driver.find_elements(*self.Settings_Map_MapStyle_list_locator)

    @property
    def atc_boundaries_button(self):
        return self.driver.find_element(*self.Settings_Map_ATCBoundaries_dropdown_locator)

    def click_atc_boundaries_button(self):
        self.atc_boundaries_button.click()

    def get_list_of_atc_boundaries(self):
        #returns a list of dropdown values from the ATC Boundaries of the Map tab
        return self.driver.find_elements(*self.Settings_Map_ATCBoundaries_list_locator)

    @property
    def aeronautical_charts_button(self):
        return self.driver.find_element(*self.Settings_Map_Aeronautical_Charts_dropdown_locator)

    def click_aeronautical_charts_button(self):
        self.aeronautical_charts_button.click()

    def get_list_of_aeronautical_charts(self):
        #returns a list of dropdown values from the Aeronautical Charts of the Map tab
        return self.driver.find_elements(*self.Settings_Map_Aeronautical_Charts_list_locator)

    @property
    def aircraft_sizes_button(self):
        return self.driver.find_element(*self.Settings_Map_Aircraft_Size_dropdown_locator)

    def get_list_of_aircraft_sizes(self):
        #returns a list of dropdown values from the Aircraft sizes of the Map tab
        return self.driver.find_elements(*self.Settings_Map_Aircraft_Size_list_locator)

    def click_aircraft_sizes_button(self):
        self.aircraft_sizes_button.click()

    @property
    def aircraft_labels_button_1(self):
        return self.driver.find_element(*self.Settings_Map_Aircraft_Labels1_dropdown_locator)

    def get_list_of_aircraft_labels_1(self):
        return self.driver.find_elements(*self.Settings_Map_Aircraft_Labels1_list_locator)

    def click_aircraft_labels_button_1(self):
        self.aircraft_labels_button_1.click()

    @property
    def aircraft_labels_button_2(self):
        return self.driver.find_element(*self.Settings_Map_Aircraft_Labels2_dropdown_locator)

    def get_list_of_aircraft_labels_2(self):
        return self.driver.find_elements(*self.Settings_Map_Aircraft_Labels2_list_locator)

    def click_aircraft_labels_button_2(self):
        self.aircraft_labels_button_2.click()

    @property
    def aircraft_labels_button_3(self):
        return self.driver.find_element(*self.Settings_Map_Aircraft_Labels3_dropdown_locator)

    def get_list_of_aircraft_labels_3(self):
        return self.driver.find_elements(*self.Settings_Map_Aircraft_Labels3_list_locator)

    def click_aircraft_labels_button_3(self):
        self.aircraft_labels_button_3.click()

    @property
    def aircraft_labels_button_4(self):
        return self.driver.find_element(*self.Settings_Map_Aircraft_Labels4_dropdown_locator)

    def get_list_of_aircraft_labels_4(self):
        return self.driver.find_elements(*self.Settings_Map_Aircraft_Labels4_list_locator)

    def click_aircraft_labels_button_4(self):
        self.aircraft_labels_button_4.click()

    @property
    def estimations_button(self):
        return self.driver.find_element(*self.Settings_Visibility_Estimations_button_locator)

    def click_estimations_button(self):
        self.estimations_button.click()

    def get_list_of_estimations(self):
        return self.driver.find_elements(*self.Settings_Visibility_Estimations_list_locator)

    def change_toggle_button_state(self, lista, title=''):
        '''
        :param lista: the list of toggle WebElements to click through
        :param title: optional param, in case the feature is locked, check the upgrade popup title text
        :return: clicks each toggle button with a pause of 2 seconds between them.
        '''
        for element in lista():
            time.sleep(1)
            element.click()
            time.sleep(1)
            try:
                assert self.upgrade_popup_title_text in title, f"incorrect popup title for {self.upgrade_popup_title_text}"
            except NoSuchElementException:
                continue

    def get_list_of_toggles(self):
        return self.driver.find_elements(*self.Settings_Map_toggles_locator)

    def get_list_of_weather_toggles(self):
        return self.driver.find_elements(*self.Settings_Weather_toggles_locator)

    def get_list_of_visibility_toggles(self):
        return self.driver.find_elements(*self.Settings_Visibility_toggles_locator)

    def get_list_of_misc_toggles(self):
        return self.driver.find_elements(*self.Settings_Misc_toggles_locator)

    @property
    def weather_button(self):
        return self.driver.find_element(*self.Settings_Weather_button_locator)

    def click_weather_button(self):
        self.weather_button.click()

    @property
    def visibility_button(self):
        return self.driver.find_element(*self.Settings_Visibility_button_locator)

    def click_visibility_button(self):
        self.visibility_button.click()

    @property
    def misc_button(self):
        return self.driver.find_element(*self.Settings_Misc_button_locator)

    def click_misc_button(self):
        self.misc_button.click()

    def load(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.find_element(*self.About_locator).click()

    def login(self):
        self.click_login_button()
        self.click_email_button()
        self.send_keys_email_button("raoul_tifrea@yahoo.com")
        self.click_password_button()
        self.send_keys_password_button("FlightRadar123!")
        self.click_sign_in_button()
        self.wait_to_load(self.subscription_plan_locator)

    def quit(self):
        self.driver.quit()
