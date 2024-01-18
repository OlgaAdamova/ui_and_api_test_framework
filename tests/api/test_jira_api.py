import os
from jira import JIRA


def test_jira_bugs():
    email = os.environ["EMAIL"]
    token = os.environ["ATLASSIAN_TOKEN"]
    jira = JIRA(
        server="https://oadamova82.atlassian.net",
        basic_auth=(email, token),
    )
    query = jira.search_issues(jql_str='project = "API" AND issuetype = Bug')
    assert len(query) == 2









