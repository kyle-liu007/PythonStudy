# LOG
## 日志相关概率
- 日志的级别（level）
    - 不同的用户关注不同的程序信息
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO操作不要太频繁
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志的信息
    - when
    - where
    - how（程度,也就是level）
    - what（发生了什么）
- 成熟的第三方日志

## logging模块
- 日志级别
    - 级别可以自定义（但基本不用自定义,内置定义基本够用）
    - 默认级别：
        - DEBUG,INFO,WARNING,ERROR,CRITICAL
- 初始化日志实例或写日志时需要指定级别,只有当级别等于或高于指定级别才被记录
- 使用方式
    - 直接使用logging（）（已封装了其他组件,使用于小软件）
    - logging四大组件直接定制（适用于大软件）
    
## logging模块级别的日志
- 有以下几个函数

    logging.debug（masg,*args,**kwargs）
    ……………………info(…………)
    ………………………………………………
    logging.log(level,*args,**kwargs)  创建一条严重级别为level的日志记录
    logging.basicConfig(**kwargs)    对root logger进行一次性配置

- logging.basicConfig(**kwargs)
    - 只有在第一次调用的时候起作用
    - 不配置logger则使用默认值
        - 输出： sys.stderr
        - 级别： WARNING
        - 格式： level:log_name:content
    - 内部的format关键字的可设置的值：百度
## logging模块的处理流程
- 四大组件
    - 日志器（Logger）：产生日志的一个接口
    - 处理器（Handler）：把产生的日志发送到相应的目的地
    - 过滤器（Filter）：更精细地控制那些日志输出
    - 格式器（Formatter）：对输出信息进行格式化
- Logger
    - 产生一个日志
    - 操作
    
        Logger.setLevel()
        Logger.addHandler() 和 Logge.removeHandler()
        Logger.addFilter() 和 Logger.removeHandler()
        Logge.debug()产生一条debug级别的日志,同理info,error……
        Logger.exception():创建类似于Logger.error的日志消息
        Logger.log()获取一个明确的日志level参数类创建一个日志记录
    - 如何得到一个logger对象
        - 实例化
        - logging.getlogger()
- Handler
    - 把log发送到指定位置
    - 方法：
        - setLevel
        - setFormat
        - addFilter, removeFilter
    - 不需要直接使用,Handler是基类（用于继承）
        - 有如下子类：百度
- Format类
    - 直接实例化
    - 可以继承Format添加特殊内容
    - 三个参数
        - fmt：指定消息格式化字符串,如果不指定该参数则默认使用message的原始值
        - datefmt：指定日期格式化字符串,如果不指定则该参数默认使用“%Y%m%d%H%M%S"
        - style:可取值为‘%’,'{','$',如果不指定该参数则默认使用‘%’
    - Filter类
        - 可以被Handler和Logger使用
        - 控制传递过来的信息的具体内容