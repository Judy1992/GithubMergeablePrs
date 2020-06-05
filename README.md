# GithubMergeablePrs

1. Install `pygithub`

```
pip3 install pygithub
```

2. If you want to integrate with Dingtalk, install `DingtalkChatbot`.

```
pip3 install pyDingtalkChatbot
```

Config Dingtalk bot following the [tutorial](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq).

To see the usage example, please refer to [MyTest](test/MyTest.py) and replace the [config](test/config.ini) with your own value.

FAQ: 

Q: where runing the test, get warning `ResourceWarning: unclosed <ssl.SSLSocket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('xxx', xx), raddr=('xxx', xx)>`

A: refer to PyGithub https://github.com/PyGithub/PyGithub/issues/1372