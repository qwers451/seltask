from pages.dropdown_page import DropdownPage

class TestDropdown:
    def test_select_option(self, driver):
        page = DropdownPage(driver)
        page.open()

        page.select_by_text("Option 2")

        selected = page.get_selected_text()
        assert selected == "Option 2"
