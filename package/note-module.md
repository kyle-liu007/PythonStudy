- if \_\_name__ == '\_\_main__':
    - 作为一个判断,使得判断后的代码只能在源文件中执行,而不能作为一个模块被调用
    - 此判断语句适合一直作为程序的入口
    
- 模块的搜素路径和存储
    - 程序默认的搜素路径
       
       impor sys
       sys.path #这里的sys.path时一个列表
       用此代码可以搜素到程序的搜素路径
    
    - 添加搜素路径
    
        sys.path.append()
        
    - 模块的加载顺序
        1.搜素程序中已经加载好的模块
        2.搜素Python的内置模块
        3.搜素sys.path路径
        
- 包的标志性文件：
    - \_\_init__.py
    - 该文件置于包的最前面,显示该文件夹为一个包

- from package_name import * :
    - 该导入方法只会导入'\_\_init__.py'内的所有函数和类
    - 使用时直接用函数或类的名称：
        func_name()
        class_name()
- from package_name.module_name import *
    - 导入指定模块内的所有内容
    - 使用方法同上
    
- '\_\_all__'的用法
     - 限定使用 from package_name import * 时可以导入的内容
     - '\_\_init__.py'中内容为空,或者没有'\_\_all__'的时候,那么只会导入'\_\_init__.py'中的内容
     - '\_\_init__.py'中如果设置了'\_\_all__'的值,那么则按照'\_\_all__'指定的子包或者模块进行导入
        如此则不会导入'\_\_init__.py'中的内容
     - '\_\_all__'的使用语法：
            \_\_all__ = ['module1','module2','subpackage',…………]
     - 用'\_\_all__'导入时函数与类的用法：
            module_name.func()
            module_name.class_name
            