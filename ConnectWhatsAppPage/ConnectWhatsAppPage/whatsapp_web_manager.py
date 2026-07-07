from playwright.sync_api import sync_playwright


class WhatsAppWebManager:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def open_whatsapp_web(self):
        if self.page is not None:
           self.page.goto("https://web.whatsapp.com")
           return
        
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch_persistent_context(
            user_data_dir="whatsapp_session",
            headless=False
        ) 

        self.page = self.browser.new_page()
        self.page.goto("https://web.whatsapp.com")

    def close_browser(self):
        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()

    def is_logged_in(self):
       if self.page is None:
          return False

       try:
        self.page.wait_for_selector("div[role='grid']", timeout=30000)
        return True
       except:
        return False

    def open_phone_number_linking(self, phone_number):
        self.open_whatsapp_web()

        try:
           self.page.get_by_role("link", name="Log in with phone number").click(timeout=10000)
        except:
           try:
              self.page.get_by_text("Log in with phone number").click(timeout=10000)
           except:
              return False

        try:
            phone_input = self.page.locator("input").last
            phone_input.fill(phone_number)

            self.page.get_by_text("Next").click(timeout=5000)

            return True

        except:
               return False