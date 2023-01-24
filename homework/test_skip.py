"""
Переопределите параметр с помощью indirect
"""

import pytest
from selene import be
from selene.support.shared import browser


@pytest.fixture(params=[pytest.param((1920, 1080)),
                        pytest.param((1024, 720)),
                        pytest.param((393, 851)),
                        pytest.param((390, 844))])
def browser_management(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


def test_github_desktop(browser_management):

    # GIVEN:
    if browser.config.window_width == 393 or browser.config.window_width == 390:
        pytest.skip(reason='Skipped mobile screen resolution')

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


def test_github_mobile(browser_management):

    # GIVEN:
    if browser.config.window_width == 1920 or browser.config.window_width == 1024:
        pytest.skip(reason='Skipped desktop screen resolution')

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
