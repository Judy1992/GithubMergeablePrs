import unittest


from script.PrList import GithubPrList
from script.SendDingMsg import DingdingBot


class MyTest(unittest.TestCase):
    org = "$org"
    repo = "$repo"
    token = "$githubToken"
    dingWebHook = "$dingTalkWebHook"

    def test_GetMergablePrs(self):
        try:
            mergeablePrs = GithubPrList(self.org, self.repo, self.token).getMergablePrs()
        except:
            self.assertTrue(False)


    def test_GetMergablePrsCustomFilter(self):
        try:
            filter = "repo:{org}/{repo} is:pr is:open review:approved".format(org=self.org, repo=self.repo)
            mergeablePrs = GithubPrList(self.org, self.repo, self.token).getMergablePrsCustomFilter(filter)
        except:
            self.assertTrue(False)


    def test_sendPrMsgToDing(self):
        filter = "repo:{org}/{repo} is:pr is:open review:approved".format(org=self.org, repo=self.repo)
        prList = GithubPrList(self.org, self.repo, self.token).getMergablePrsCustomFilter(filter)

        xiaoding = DingdingBot(self.dingWebHook)

        txt = ""
        atPerson = ["$telephone"]
        if len(prList) > 0:
            txt = 'pr to merg: \n' + '\n '.join([str(x) for x in prList]) + "\n"

        if len(txt) > 0:
            print(txt)
            xiaoding.sendMsg(txt, atPerson)

if __name__ == "__main__":
    unittest.main()
