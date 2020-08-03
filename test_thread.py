import threading
import time

def my_func(thread_number):
    return print('my_func called by thread No{}'.format(thread_number))

def function_A():
    print(threading.current_thread().getName() + str('-->starting \n'))
    time.sleep(2)
    print(threading.current_thread().getName() + str('-->exiting \n'))

def function_B():
    print(threading.current_thread().getName() + str('-->starting \n'))
    time.sleep(2)
    print(threading.current_thread().getName() + str('-->exiting \n'))

def function_C():
    print(threading.current_thread().getName() + str('-->starting \n'))
    time.sleep(2)
    print(threading.current_thread().getName() + str('-->exiting \n'))

if __name__ == '__main__':
    t1 = threading.Thread(name='function_A', target=function_A)
    t2 = threading.Thread(name='function_B', target=function_B)
    t3 = threading.Thread(name='function_C', target=function_C)

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()