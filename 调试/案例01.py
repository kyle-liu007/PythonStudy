
def fun(name):
    print('测试中')
    print('名字是{}'.format(name))

if __name__ == '__main__':
    name = input('please write your name:')
    fun(name= name)
    print('##' * 20)