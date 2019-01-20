from behave import then

from features.pages.search_results_page import SearchResultsPage


@then("I assert data")
def step_impl(context):
    search_results_page = SearchResultsPage(context.driver)
    assert search_results_page.label_top_posts in search_results_page.get_header_text()
