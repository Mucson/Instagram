from behave import then

from features.pages.search_results_page import SearchResultsPage


@then("I assert data")
def step_impl(context):
    assert "Лучшие Публикации" in SearchResultsPage(context.driver).get_header_text()
