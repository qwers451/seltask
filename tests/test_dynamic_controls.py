from pages.dynamic_controls_page import DynamicControlsPage

class TestDynamicControls:
    def test_remove_and_add_checkbox(self, driver):
        page = DynamicControlsPage(driver)
        page.open()

        assert page.is_checkbox_present()

        page.click_remove()
        assert not page.is_checkbox_present()
        msg = page.get_message()
        assert "It's gone!" in msg

        page.click_add()
        assert page.is_checkbox_present()
        msg2 = page.get_message()
        assert "It's back!" in msg2
