from pages.hovers_page import HoversPage

class TestHovers:
    def test_hover_shows_caption(self, driver):
        page = HoversPage(driver)
        page.open()

        page.hover_over_figure(index=0)

        caption = page.get_caption_text(index=0)
        assert "name: user1" in caption
