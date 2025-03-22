
from behave import given, when, then

@given('the user interacts with "{topic}"')
def step_impl_given_interaction(context, topic):
    context.topic = topic

@when('the user requests multi-format content')
def step_impl_request_multi_format(context):
    context.recommendations = [
        {"type": "video", "title": "GenAI for Devs - Video Guide"},
        {"type": "article", "title": "Understanding GenAI - In Depth"}
    ]

@then('the system should return both videos and articles matching the interest topic')
def step_impl_verify_recommendations(context):
    types = [item["type"] for item in context.recommendations]
    assert "video" in types and "article" in types

@given('the user prefers "{format}" content')
def step_impl_given_preference(context, format):
    context.preferred_format = format

@when('a recommendation is generated')
def step_impl_generate_recommendation(context):
    all_recommendations = [
        {"type": "video", "title": "GenAI for Devs - Video Guide"},
        {"type": "article", "title": "GenAI Whitepaper"}
    ]
    context.recommendations = [
        item for item in all_recommendations if item["type"] == context.preferred_format
    ]

@then('only {format} content links should be included')
def step_impl_verify_filtered_recommendations(context, format):
    for item in context.recommendations:
        assert item["type"] == format
