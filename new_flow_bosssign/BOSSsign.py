from selenium import webdriver
from time import sleep
import time
import sys
import os
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
sys.path.append('E:/JackyYang/venv/work outing/')
from OATest import OA

#创建流程使用的用户名
username = 'xxxx'
#密码（测试环境随意填写）
password = 'xxxxxx'
#测试的流程地址
url = 'http://xxx.xxx.xx.xxx:xxxx/'
#需要测试的流程，必须与web上所需要创建的流程名字一致，否则link跳转失败，无法创建成功
flowname = 'BOSS签字申请流程'

def Bosssign():
    #初始化一个OA类
    Testflow = OA(url)
    #调用登录方法，传入用户名与密码
    Testflow.login(username,password)
    #调用创建新流程的方法，传入的是申请流程的名称
    Testflow.newflow(flowname)

    #下面的是BOSS签字申请流程界面资料填写等操作,因为每个界面的填写内容与必填项等都不相同，所以每块需要单独拿出来写
    element = Testflow.driver.find_element_by_xpath("//input[@id='WF_TITLE']")
    element.clear()
    #记录申请单子的名称,很重要！！！实名时间戳的目的在于使单号唯一，以便后面审批搜索使用
    Approvalname = 'xxx-签字申请-' + str(int(time.time()))
    print(f"创建的单号名称:{Approvalname}")
    element.send_keys(Approvalname)
    element = Testflow.driver.find_element_by_xpath("//span[@class='ant-select-arrow']").click()
    sleep(1)
    elements2 = Testflow.driver.find_elements_by_xpath("//li[@unselectable='unselectable']")
    sleep(2)
    element = random.choice(elements2)
    element.click()
    sleep(2)
    element = Testflow.driver.find_element_by_xpath("//div[@class='ant-select-selection__rendered']/div[@class='ant-select-selection-selected-value']")
    #记录BOSS的名字
    Bossname = element.text
    print(f'签字BOSS的名字是:{Bossname}')
    element = Testflow.driver.find_element_by_xpath("//a[@class='btns btns-primary']").click()
    sleep(1)
    #此处使用了一个处理弹窗的工具，在里面一个文件夹中，会有对应的使用方法，目的是为了在弹出的窗口中自动上传一个图片，selenium无法处理此类弹窗，所以必须借用其它工具
    os.system('E:/JackyYang/venv/testbosssign/bosssigntest.exe')
    element = Testflow.driver.find_element_by_xpath("//textarea[@id='REMARK']")
    element.send_keys(str(int(time.time())))
    sleep(2)
    element = Testflow.driver.find_element_by_xpath("//button[@id='btnSubmit']").click()
    sleep(2)
    element = Testflow.driver.find_element_by_xpath("//a[@class='NY_rt_btn NY_rt_active NY_rt_single']").click()
    Testflow.logout()


    """注销用户切换下一级,逐级进行审批，直到结束，审批的操作都是一样的，因此只要准备好对应的审批人即可"""
    #逐级审批人在List添加即可，再调用AutoApproval函数，并传入列表，与单子的名称即可,如果是要密码验证的，可能需要使用到元祖，这个可以拓展
    ApprovalPeopleList = ['xxxx', 'xxxx', 'xxxx', 'xxxxxxx']

    #调用逐级审批的函数
    Testflow.AutoApproval(ApprovalPeopleList, password, Approvalname)
    #最后一级Boss签字判断+审批
    Testflow.BossApproval(Bossname, password , Approvalname)
    Testflow.close()

if __name__ == '__main__':
    Bosssign()
