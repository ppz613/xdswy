"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
import time

from common.sendMessageWeCom import SendMessageToWeCom


# 法一：conftest.py中重写pytest_terminal_summary方法
def pytest_terminal_summary(terminalreporter, exitstatus,config):
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    error = len(terminalreporter.stats.get('error', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    wecom = SendMessageToWeCom(total, passed, failed, error, skipped)
    print("total:", terminalreporter._numcollected)
    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    print('total times:', duration, 'seconds')
    wecom.sendMessageWeCom()


# 法二：conftest.py中重写pytest_sessionfinish方法
def pytest_sessionfinish(session):
    terminalreporter = session.config.pluginmanager.get_plugin('terminalreporter')
    total_case = terminalreporter._numcollected
    pass_case = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    fail_case = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    error_case = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    skip_case = len([i for i in terminalreporter.stats.get('skip', []) if i.when != 'teardoen'])
    pass_rate = round((len(terminalreporter.stats.get('pass', [])) / (total_case - skip_case) * 100), 2)
    duration = round((time.time() - terminalreporter._sessionstarttime), 2)
    wecom = SendMessageToWeCom(total=total_case, passed=pass_case, failed=fail_case, error=error_case, skipped=skip_case, duration = duration)
    wecom.sendMessageWeCom()
