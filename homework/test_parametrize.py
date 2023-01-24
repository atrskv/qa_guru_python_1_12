"""
Переопределите параметр с помощью indirect
"""

import pytest
from selene import be
from selene.support.shared import browser


@pytest.fixture(params=[('1920', '1080'),
                        ('1024', '720'),
                        ('393', '851'),
                        ('390', '844')])
def browser_management(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


@pytest.mark.parametrize('browser_management', [('1920', '1080')], indirect=True)
def test_github_desktop(browser_management):

    # GIVEN:
    browser.open('https://github.com/')

    # WHEN:
    sign_in_button = (
        browser.element('[class*="sign-in"]')
        .click()
    )

    # THEN:
    submit_button = (
        browser.element('[class$="sign-in-button"]')
        .should(be.visible)
    )


@pytest.mark.parametrize('browser_management', [('390', '844')], indirect=True)
def test_github_mobile(browser_management):

    # GIVEN:
    browser.open('https://github.com/')

    # WHEN:
    hamburger_menu = (
        browser.element('.HeaderMenu-toggle-bar')
        .click()
    )

    sign_in_button = (
        browser.element('[class*="sign-in"]')
        .click()
    )

    # THEN:
    submit_button = (
        browser.element('[class$="sign-in-button"]')
        .should(be.visible)
    )
