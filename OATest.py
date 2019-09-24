from selenium import webdriver
import time
from time import sleep
from selenium.webdriver import ActionChains
"""Copyright by JackyYang"""
"""类的目的是为了方便执行重复的操作，节省实际流程的重复写法，方便维护"""

class OA():
    #初始化OA系统参数
    def __init__(self,url):
        self.driver = webdriver.Chrome(r'D:\chromedriver_win32\chromedriver.exe')
        self.url = url
        self.driver.set_window_size(1920,1080)
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    #登录的方法，需要用户名uesr与pwd密码
    def login(self,user,pwd):
        element = self.driver.find_element_by_xpath("//input[@id='user']")
        element.send_keys(user)

        element = self.driver.find_element_by_xpath("//input[@id='pwd']")
        element.send_keys(pwd)

        element = self.driver.find_element_by_xpath("//button[@id='btnSubmit']")
        element.click()
        sleep(2)

    #创建新流程，需要指定一个流程的名称
    def newflow(self,flowname):
        elements1 = self.driver.find_elements_by_xpath("//li[@class='first-menu']")
        for i in elements1:
            if i.text == '流程':
                element = i
                element.click()
                break
        element = self.driver.find_element_by_link_text("新建流程").click()
        element = self.driver.find_element_by_link_text(flowname).click()

    #某一个节点的审批，需要审批单子的名称，因此在新建流程的时候，一定要保存下填写的申请单名称
    def Approval(self,Approvalname):
        elements3 = self.driver.find_elements_by_xpath("//li[@class='first-menu']")
        for i in elements3:
            if i.text == '流程':
                element = i
                element.click()
                break
        sleep(2)
        element = self.driver.find_element_by_link_text("我的审批").click()
        # element = self.driver.find_element_by_link_text(Approvalname).click()
        element = self.driver.find_elements_by_xpath("//div[@class='fl list-search-lginput']/input")[0].send_keys(Approvalname)
        # element = self.driver.find_element_by_link_text("查询").click()
        sleep(2)
        element = self.driver.find_element_by_xpath("//div[@class='fl list-top-sitem list-button-wrap clearfix']").click()
        # element = self.driver.find_element_by_link_text(Approvalname).click()
        sleep(3)
        element = self.driver.find_elements_by_xpath("//div[@class='KY-main-fluid']/div[@class]")[-1].click()
        element = self.driver.find_element_by_xpath("//button[@id='btnSubmit']").click()
        element = self.driver.find_element_by_xpath("//a[@class='NY_rt_btn NY_rt_active NY_rt_single']").click()

    #传入一个逐级审批人的列表，循环执行审批流程
    def AutoApproval(self,ApprovalList, password, Approvalname):
        for Approvalpeople in ApprovalList:
            self.login(Approvalpeople, password)
            self.Approval(Approvalname)
            self.logout()

    #boss签字判断，传入的是所选择的BOSS名字，因为自动化测试时选择的BOSS名称随机。用于自动审批BOSS签字申请流程与证件申请的最后一步
    def BossApproval(self, Bossname, password, Approvalname):
        if Bossname == 'xx':
            self.login('xx', password)
            self.Approval(Approvalname)
            self.logout()
        elif Bossname == 'xx':
            self.login('xx', password)
            self.Approval(Approvalname)
            self.logout()
        elif Bossname == 'xx':
            self.login('xx', password)
            self.Approval(Approvalname)
            self.logout()
        elif Bossname == 'xx':
            self.login('shenjun', password)
            self.Approval(Approvalname)
            self.logout()
        elif Bossname == 'xx':
            self.login('xxx', password)
            self.Approval(Approvalname)
            self.logout()

    #登出
    def logout(self):
        element = self.driver.find_element_by_xpath("//div[@class='personal-pic']").click()
        element = self.driver.find_element_by_link_text("退出").click()

    #关闭窗口，退出测试
    def close(self):
        input('Please input any key to continue......')
        self.driver.close()