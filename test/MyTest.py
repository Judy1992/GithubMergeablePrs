import unittest
from configparser import ConfigParser
from src.PrList import GithubPrList
from src.SendDingMsg import DingdingBot


class MyTest(unittest.TestCase):

    FILTER_TEMPLATE = "repo:{org}/{repo} is:pr is:open review:approved"

    def setUp(self):
        cp = ConfigParser()
        cp.read("config.ini")
        githubSection = cp.sections()[0]
        dingSection = cp.sections()[1]
        self.org = cp.get(githubSection, "org")
        self.repo = cp.get(githubSection, "repo")
        self.token = cp.get(githubSection, "token")
        self.dingWebHook = cp.get(dingSection, "dingWebHook")
        self.atPerson = cp.get(dingSection, "atPerson").split(",")
        self.securitymsg = cp.get(dingSection, "securitymsg")

    def test_GetMergablePrs(self):
        GithubPrList(self.org,
                     self.repo,
                     self.token).getMergablePrsCustomFilter()
        self.assertTrue(False)

    def test_GetMergablePrsCustomFilter(self):
        filter = self.FILTER_TEMPLATE.format(org=self.org, repo=self.repo)
        GithubPrList(self.org,
                     self.repo,
                     self.token).getMergablePrsCustomFilter(filter)
        self.assertTrue(False)

    def test_sendPrMsgToDing(self):
        filter = self.FILTER_TEMPLATE.format(org=self.org, repo=self.repo)
        prList = GithubPrList(self.org,
                              self.repo,
                              self.token).getMergablePrsCustomFilter(filter)

        xiaoding = DingdingBot(self.dingWebHook)

        txt = ""
        if len(prList) > 0:
            txt = self.securitymsg + ': \n' \
                  + '\n '.join([str(x) for x in prList]) \
                  + "\n"

        if len(txt) > 0:
            print(txt)
            xiaoding.sendMsg(txt, self.atPerson)

if __name__ == "__main__":
    unittest.main()
