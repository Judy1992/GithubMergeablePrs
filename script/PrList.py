from github import Github

import tracemalloc

DEFAULT_PR_SORT = "updated"
DEFAULT_ORDER = "desc"
DEFAULT_CONNECT_TIMEOUT = 15


class PrElement:
    def __init__(self, id, title, url):
        self._id = id
        self._title = title
        self._url = url

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    def __str__(self):
        return self._title + "\n" + self._url


class GithubPrList:

    @property
    def gh(self):
        return self._gh

    @property
    def org(self):
        return self._org

    FILTER_TEMPLATE = "repo:{org}/{repo} is:pr is:open review:approved"

    def __init__(self,
                 org,
                 repo,
                 login_or_token,
                 password=None,
                 timeout=DEFAULT_CONNECT_TIMEOUT,
                 retry=None,
                 ):

        tracemalloc.start()
        """
        :param org: string
        :param repo: string
        :param login_or_token: string，token or username
        :param password: string
        :param timeout: integer
        :param retry: int or urllib3.util.retry.Retry object
        """
        self._gh = Github(login_or_token=login_or_token, password=password, timeout=timeout, retry=retry)
        self._org = org
        self._repo = repo


    def getMergablePrs(self,
                       sort=DEFAULT_PR_SORT,
                       order=DEFAULT_ORDER,
                       ):
        """
        :param order: string ('asc', 'desc')
        :param sort: string('comments', 'created', 'updated')
        :rtype :class:`List` of :class:`PrList2.PrElement`
        """

        issues = self._gh.search_issues(self.FILTER_TEMPLATE.format(org=self._org, repo=self._repo), sort, order)
        prList = []

        for issue in issues:
            prList.append(PrElement(issue.number, issue.title, issue.html_url))

        return prList

    def getMergablePrsCustomFilter(self,
                       filter,
                       sort=DEFAULT_PR_SORT,
                       order=DEFAULT_ORDER,
                       ):
        """
        :param filter: string
        :param order: string ('asc', 'desc')
        :param sort: string('comments', 'created', 'updated')
        :rtype :class:`List` of :class:`PrList2.PrElement`
        """
        tracemalloc.get_object_traceback(self._gh)
        issues = self._gh.search_issues(filter, sort, order)
        prList = []

        for issue in issues:
            prList.append(PrElement(issue.number, issue.title, issue.html_url))


        tracemalloc.get_tracemalloc_memory()
        return prList

    def tearDown(self):
        self._gh.__requester.Requester.resetConnectionClasses()