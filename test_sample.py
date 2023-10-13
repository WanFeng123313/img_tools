# test_sample.py
# 被测功能
import pytest
def func(x):
    return x + 1

# 测试成功
def test_pass():
    assert func(3) == 4

# 测试失败
@pytest.mark.skip()
def test_fail():
    assert func(3) == 5