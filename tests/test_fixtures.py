"""
Сделайте разные фикстуры для каждого теста
"""

import pytest
from selene.support.shared import browser
from selene import be


@pytest.fixture(params=[('1920', '1080'),
                        ('1024', '720')],
                ids=['First desktop screen resolution', 'Second desktop screen resolution'])
def browser_management_for_desktop(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


@pytest.fixture(params=[('390', '844'),
                        ('393', '851')],
                ids=['First mobile screen resolution', 'Second mobile screen resolution'])
def browser_management_for_mobile(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


def test_github_desktop(browser_management_for_desktop):

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


def test_github_mobile(browser_management_for_mobile):

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
