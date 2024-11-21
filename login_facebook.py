from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Uruchom przeglądarkę z widocznym interfejsem
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()  # Tworzy nowy kontekst przeglądania
    page = context.new_page()

    # Otwórz stronę logowania Facebooka
    page.goto("https://www.facebook.com")

    print("Zaloguj się ręcznie na Facebooku, a potem zamknij to okno.")

    # Poczekaj, aż użytkownik zaloguje się i potwierdzi
    input("Naciśnij Enter, gdy zakończysz logowanie...")

    # Zapisz stan sesji do pliku
    context.storage_state(path="logged_in.json")
    print("Stan sesji został zapisany!")

    browser.close()
