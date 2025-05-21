import pytest
from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:8000/"

@pytest.mark.parametrize(
        ("num", "num_root"),
        (
            (10, 1000),
            (5, 125),
            (4, 64),
            (3, 27),
            (2, 8),
            (1, 1),
        )
)
def test_cube(num, num_root, page: Page):
    page.goto(BASE_URL)

    input = page.get_by_placeholder("enter number...")

    input.fill(f"{num}")

    page.get_by_role('button', name="Cube").click()

    res = page.locator("p#result")

    expect(res).to_contain_text(f"{num_root}")


def test_empty_input(page: Page):
    page.goto(BASE_URL)

    input = page.get_by_placeholder("enter number...")

    input.fill("")

    page.get_by_role('button', name="Cube").click()
    
    res = page.locator("p#result")

    expect(res).to_contain_text("Enter something!")


