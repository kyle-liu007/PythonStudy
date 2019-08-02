# 多线程 vs 多进程
- 进程： 程序运行的状态
    - 包含地址空间,内存,数据栈等
    - 每个进程有自己完全独立的运行环境,多进程共享数据是一个问题
- 线程： 
    - 一个进程的独立运行片段,一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁（GIL）
    - Python代码的执行是由Python虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行

- Python包
     - thread：有问题,不好用,Python3改成了_thread
     - threading:通行的包
     
- threading的使用：
    - 直接利用threading.Thread生成Tread实例
        1. t = threading.Thread(target = xxx, args = (xxx,))
        2. t.start():启动该线程
        3. t.join():等待该线程执行完成
    - 守护线程-daemon
        - 如果在程序中将子线程设置成守护线程,则子线程在主线程结束时自动退出
        - 一般认为,守护线程不重要或不允许离开主线程独立运行
        - 守护线程能否有效与环境相关
    - 线程常用属性：
        - threading.currentThread 返回当前的线程变量
        - threading.enumerate 返回一个包含正在运行的线程的list,正在运行的线程是指启动后的线程
        - threading.activeCount 返回正在运行的线程数量,效果跟len(threading.enumerate)
        - thread_name.setName:给线程起名
        - thread_name.getName:获取线程的名字
    - 直接写一个子类,继承自thread.Thread
        - 直接继承Thread
        - 重写run函数
        - 类实例可以直接运行
- 共享变量
    - 共享变量：当多个线程同时访问一个变量的时候,会产生共享变量问题
    - 解决方案：锁,信号灯
    - 锁（Lock）：
        - 是一个标志,表示一个线程在占用一些资源
        - 使用方法
            - 上锁
            - 使用共享资源
            - 取消锁,释放锁
        - 锁谁：哪个资源需要多个线程共享,锁哪个
        - 理解锁：锁其实不是锁住谁,而是一个令牌
    - 线程安全问题：
        - 如果一个资源/变量,它对于多线程来讲,不用加锁也不会引起任何问题,则称该变量线程安全
        - 线程不安全变量类型: list, set, dict
        - 线程安全的变量类型： queue
    - 生产者消费者问题
        - 这是一个模型,可以用来搭建消息队列
        - queue是一个用来存放变量的数据结构,特点是先进先出,内部元素需要排队,可以理解成一个特殊的list
    - semaphore
        - 允许一个资源最多由指定个数多线程同时使用
    - threading.Timer
    - 可重入锁
        - 一种锁,可以被一个线程多次申请
        - 主要解决递归调用的时候,需要申请锁的情况
        
# 线程替代方案
- subprocess
    - 完全跳过线程,使用进程
    - 是派生进程的主要替代方案
- multiprocessing
    - 使用threading接口派生,使用子进程
    - 允许多核或者多cpu派生进程,接口跟threading非常相似
    
- concurrent.futures
    - 新的异步执行操作
    - 任务级别的操作

# 多进程
- 进程间通讯（InterprocessCommunication, IPC）
- 进程间无任何共享状态
- 进程的创建
    - 直接生成Process实例对象
    - 派生子类
    
- 在os中查看pid,ppid以及他们的关系