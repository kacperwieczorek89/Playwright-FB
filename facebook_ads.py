import json
from playwright.sync_api import sync_playwright

with open("ogloszenie.txt", "r", encoding="utf-8") as file:
    announcement_text = file.read()

# Load groups from a JSON file
with open('groups.json', 'r') as f:
    data = json.load(f)

groups = data["groups"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="logged_in.json")

    for group in groups:
        try:
            page = context.new_page()
            page.goto(group)

            # Click to start creating a new post
            page.click("css=.xqmpxtq > .x1i10hfl:nth-child(2) > .x6s0dn4")

            # Wait for the text input field to appear
            # page.wait_for_selector('#mount_0_0_Ot > div > div > div:nth-child(1) > div > div:nth-child(5) > div > div.__fb-light-mode.x14dbnvc.x67yw2k.x7uoazl.x1xb1xrg.xz3gdfk.xbi9o00.x1xkblxv.x4666fc.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x17qophe.x10l6tqk.x13vifvy.x1hc1fzr.x71s49j > form > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x17qophe.x10l6tqk.x13vifvy.x1hc1fzr.x71s49j > div > div > div.x78zum5.x1q0g3np.x1pl0jk3.x1plvlek.xryxfnj.xqui1pq.x14ocpvf.x5oemz9.x1lck2f0.xlgs127 > div > div.xb57i2i.x1q594ok.x5lxg6s.x6ikm8r.x1ja2u2z.x1pq812k.x1rohswg.xfk6m8.x1yqm8si.xjx87ck.xx8ngbg.xwo3gff.x1n2onr6.x1oyok0e.x1odjw0f.x1e4zzel.x78zum5.xdt5ytf.x1iyjqo2 > div.x78zum5.xdt5ytf.x1iyjqo2.x1n2onr6 > div.x78zum5.xdt5ytf.x16qp5pa > div.x1ed109x.x1iyjqo2.x5yr21d.x1n2onr6.xh8yej3 > div.x9f619.x1iyjqo2.xg7h5cd.x1swvt13.x1n2onr6.xh8yej3.x1ja2u2z.x11eofan > div > div > div > div > div._5rpb > div')

            # Fill the post content with the announcement text
            page.fill('#mount_0_0_Ot > div > div > div:nth-child(1) > div > div:nth-child(5) > div > div.__fb-light-mode.x14dbnvc.x67yw2k.x7uoazl.x1xb1xrg.xz3gdfk.xbi9o00.x1xkblxv.x4666fc.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x17qophe.x10l6tqk.x13vifvy.x1hc1fzr.x71s49j > form > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x17qophe.x10l6tqk.x13vifvy.x1hc1fzr.x71s49j > div > div > div.x78zum5.x1q0g3np.x1pl0jk3.x1plvlek.xryxfnj.xqui1pq.x14ocpvf.x5oemz9.x1lck2f0.xlgs127 > div > div.xb57i2i.x1q594ok.x5lxg6s.x6ikm8r.x1ja2u2z.x1pq812k.x1rohswg.xfk6m8.x1yqm8si.xjx87ck.xx8ngbg.xwo3gff.x1n2onr6.x1oyok0e.x1odjw0f.x1e4zzel.x78zum5.xdt5ytf.x1iyjqo2 > div.x78zum5.xdt5ytf.x1iyjqo2.x1n2onr6 > div.x78zum5.xdt5ytf.x16qp5pa > div.x1ed109x.x1iyjqo2.x5yr21d.x1n2onr6.xh8yej3 > div.x9f619.x1iyjqo2.xg7h5cd.x1swvt13.x1n2onr6.xh8yej3.x1ja2u2z.x11eofan > div > div', announcement_text)

            print(f"Announcement posted in group: {group}")

            # Wait to observe the UI (for testing purposes)
            page.wait_for_timeout(5000)


            # Click the add image button
            # page.click('css=.x9f619 > .html-div > .x1b0d499')

            # Wait for the hidden file input to appear
            # page.wait_for_selector('input[type="file"]')

            # Identify the input element of type file when it appears
            # input_file = page.query_selector('#mount_0_0_kO > div > div > div:nth-child(1) > div > div:nth-child(5) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x17qophe.x10l6tqk.x13vifvy.x1hc1fzr.x71s49j > form > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x17qophe.x10l6tqk.x13vifvy.x1hc1fzr.x71s49j > div > div > div.x78zum5.x1q0g3np.x1pl0jk3.x1plvlek.xryxfnj.xqui1pq.x14ocpvf.x5oemz9.x1lck2f0.xlgs127 > div > div.xb57i2i.x1q594ok.x5lxg6s.x6ikm8r.x1ja2u2z.x1pq812k.x1rohswg.xfk6m8.x1yqm8si.xjx87ck.xx8ngbg.xwo3gff.x1n2onr6.x1oyok0e.x1odjw0f.x1e4zzel.x78zum5.xdt5ytf.x1iyjqo2 > div.x78zum5.xdt5ytf.x1iyjqo2.x1n2onr6 > div.x78zum5.xdt5ytf.x16qp5pa > div.x1sxyh0.xurb0ha > div > div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x193iq5w.x1l7klhg.x1iyjqo2.xs83m0k.x2lwn1j.x1y1aw1k.xwib8y2 > div > div:nth-child(1) > input')

            # if input_file:
            #     # Send image to input
            #     input_file.set_input_files("post.jpg")

            # # Click the "Post" button
            # page.click('button[aria-label="Opublikuj"]')
            # page.wait_for_timeout(2000)  # Please wait a while for the publication to finish
        except Exception as e:
            print(f"Error while processing group {group}: {e}")
        # finally:
        #     page.close()
        #
        # browser.close()

