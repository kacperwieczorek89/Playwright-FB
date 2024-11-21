from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # Wczytaj zapisany stan sesji
    context = browser.new_context(storage_state="logged_in.json")
    page = context.new_page()

    # Otwórz stronę Facebooka
    page.goto("https://www.facebook.com")
    print("Jesteś zalogowany!")
    browser.close()