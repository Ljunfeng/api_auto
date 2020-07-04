## 项目说明

1 本项目在实现过程中，把整个项目拆分成请求方法封装、HTTP接口封装、关键字封装、测试用例等模块。
2.1 首先利用Python把HTTP接口封装成Python接口，接着把这些Python接口组装成一个个的关键字。
2.2 再把关键字组装成测试用例，而测试数据则通过YAML文件进行统一管理
2.3 再通过Pytest测试执行器来运行这些脚本，并结合Allure输出测试报告。
以后考虑Jenkins持续集成。
pytest 测试报告生成

命令： pytest --html=report.html --self-contained-html

在项目根目录运行
--html=report.html  指定测试报告路径和名称
--self-contained-html  在html页面本地加载css样式

## pytest版本配置
    pytest==4.5.0
    allure-pytest==2.8.6
    PyYAML==5.3.1
    pytest_remotedata==0.3.2   #0.2.1过低版本会报错
    pytest-html==1.10.0
### 注意点
    修改 "config/setting.ini" 配置文件，在Windows环境下，安装相应依赖之后，在命令行窗口执行命令：pytest
    若报错：  ImportError while loading conftest 
    解决办法： 删掉缓存文件夹删除 __pycache__
    
    
    生成requirements.txt文件
    pip freeze > requirements.txt
安装包 pip install -r requirements.txt


## 项目结构
- config ====>> 配置文件
- pytest.ini ====>> pytest配置文件
- testcases ====>> 测试用例
- pytest.ini ====> 配置执行哪些测试用例，以及报告的命令
### markers 作用是给标记内容加注释，去掉警告
    例如你标记为webapi testcase
    @pytest.mark.webapi
    marks = 
        webapi: run web api testcase 
        ;内容随便写，为了运行过程中不报警告，分号为注释键

## 关键字封装说明

关键字应该是具有一定业务意义的，在封装关键字的时候，可以通过调用多个接口来完成。在某些情况下，比如测试一个充值接口的时候，在充值后可能需要调用查询接口得到最新账户余额，来判断查询结果与预期结果是否一致，那么可以这样来进行测试：

- 1, 首先，可以把 **```充值-查询```** 的操作封装为一个关键字，在这个关键字中依次调用充值和查询的接口，并可以自定义关键字的返回结果。
- 2, 接着，在编写测试用例的时候，直接调用关键字来进行测试，这时就可以拿到关键字返回的结果，那么断言的时候，就可以直接对关键字返回结果进行断言。


## pytest /allure一些方法记录 
## 参考 https://www.cnblogs.com/xiaogongjin/p/11705134.html
    1、@pytest.fixture(conftest.py里的函数名)   @pytest.usefixture(conftest.py里的函数名)
    如果一个测试class都需要用到fixture，每个用例都去传参，会比较麻烦，这个时候，可以在class外面加usefixtures装饰器，让整个class都调用fixture
    注意：当fixture用return值需要使用时，只能在用例里面传fixture参数了。当fixture没有return值的时候，两种方法都可以
    
    2、@allure.feature(msg)
    接口用例所属模块，比如：获取用户信息
    
    3、@allure.story(msg)
    接口测试用例描述
    
    4、@allure.description("描述这个用例是测什么的，我一般不写，@allure.story(msg)足够")
    用例描述
    
    5、@allure.issue("https://www.xxx", name="点击，跳转到对应BUG的链接地址")
    该条接口用例对应的bug链接
    
    6、@allure.testcase("https://www.xxx", name="点击，跳转到对应用例的链接地址")
    用例管理系统里对应该条用例的链接。excel管理用例就不用写。
    
    7、 @allure.severity(allure.severity_level.TRIVIAL)
    测试用例的优先级，我一般也不写
    
    8、@allure.epic("针对单个接口的测试")
      敏捷里面的概念，定义史诗，往下是feature