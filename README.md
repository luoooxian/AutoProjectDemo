# AutoProjectDemo

# 环境搭建
### selenium
```
版本： 3.12.0
网址：https://www.seleniumhq.org/
```
### python
#### https://www.python.org/downloads/
请下载安装最新版本，如：**3.7.0**

### Pycharm
由于自动化项目Demo使用Pycharm来创建的，推荐使用该IDE工具运行...

# 项目结构说明
在这项目中，创建了五个以下目录及主运行文件:
```
1. Config     配置文件
2. Img        图片文件
3. Lib        封装的方法或库
4. TestCases  测试用例库
5. TestSuites 测试套件库
6. AllTestRun 运行测试套件的主文件
```
### Config 配置文件:
配置网址或账户信息等。
```
[Linkage]
URL = http://XXXXX.XXX.XXXXX.XXXX
```
### Imag 图片文件:
```html
存放需要上传的文件，如：img.jpg
```
### Lib 封装的方法或库
存放封装的方法和要使用的库，方便调用.
- 使用的库
- 封装的方法  
  -  EmailConfig.py 主要用来读取config.ini文件的邮件配置信息
  -  ReadConfig.py  主要用来读取config.ini文件的用户信息
  -  HTMLTestRunner.py 主要用来读取运行后的测试结果并自动发邮件给相关的利益相关者。

### TestCases 测试用例库
独立的用例库，方便测试套件的使用和重用.

### TestSuites 测试套件库
组合测试用例，测试不同的测试场景.
```python
    def test_My(self):
        '''测试登录并上传用户头像'''
        LoginTest(self.driver).loginByName(UserName,Password)
        My(self.driver).myProfile()
```
### AllTestRun 运行主文件
主要用来运行测试套件和自动触发测试报告并发送给相关者。
