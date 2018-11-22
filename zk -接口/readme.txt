1.主要分为base,data,file,log,main,util几个模块
base里是写的请求的方法和判断结果的方法
data 写的是获取excel里用例中各项参数的方法
file 是case和json封装的data数据

main 是主函数
util是封装的json,mysql,excel,send_email,,log的几个方法

接口依赖还未完善，后续继续补充


执行只需执行main里的 run_test.py