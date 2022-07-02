import time

from pages.elements_page import TextBoxPage

MAIN_PAGE = 'https://demoqa.com/text-box'


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, MAIN_PAGE)
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_addr, output_perm_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_curr_addr, "the current address name does not match"
            assert permanent_address == output_perm_addr, "the permanent address does not match"




