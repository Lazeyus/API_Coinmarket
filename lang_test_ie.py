from selenium import webdriver
import unittest


class LanguageChange(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get("https://coinmarketcap.com/")

    def tearDown(self):
        self.driver.quit()

    def test_cs(self):
        driver = self.driver
        driver.maximize_window()
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/cs/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'cs'

    def test_da(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/da/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'da'

    def test_de(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/de/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'de'

    def test_el(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/el/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'el'

    def test_es(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/es/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'es'

    def test_fil(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/fil/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'fil'

    def test_fr(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/fr/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'fr'

    def test_hi(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/hi/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'hi'

    def test_hu(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/hu/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'hu'

    def test_id(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/id/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'id'

    def test_it(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/it/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'it'

    def test_ja(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/ja/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'ja'

    def test_ko(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/ko/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'ko'

    def test_nl(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/nl/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'nl'

    def test_no(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/no/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'no'

    def test_pl(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/pl/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'pl'

    def test_pt_br(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/pt-br/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'pt-br'

    def test_ro(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/ro/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'ro'

    def test_ru(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/ru/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'ru'

    def test_sk(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/sk/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'sk'

    def test_sv(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/sv/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'sv'

    def test_th(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/th/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'th'

    def test_tr(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/tr/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'tr'

    def test_vi(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/vi/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'vi'

    def test_zh(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/zh/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'zh'

    def test_zh_tw(self):
        driver = self.driver
        input_field = driver.find_element_by_class_name("cmc-popover")
        input_field.click()
        input_field = driver.find_element_by_xpath('//a[@href="'+ '/zh-tw/' +'"]')
        input_field.click()
        assert driver.find_elements_by_tag_name('html')[0].get_attribute('lang') == 'zh-tw'



if __name__ == '__main__':
    unittest.main()
