
class test():
 def __init__(self,budget,windows,fm,work_for,stream,itx,hackintosh,slient,link):
   self.budget=budget
   self.windows=windows
   self.fm=fm
   self.work_for=work_for
   self.stream=stream
   self.itx=itx
   self.hackintosh=hackintosh
   self.link=link
   self.slient=slient
g1 = test(55,"N","N","G","N","N","N","N","http://coolpc.com.tw/tmp/1534263382381371.htm")
g2 = test(55,"N","Y","G","N","N","N","N","http://coolpc.com.tw/tmp/1534263382381371.htm")
g3 = test(55,"N","N","F","N","N","N","N","http://coolpc.com.tw/tmp/1534264051610497.htm")
list =[g1,g2,g3]
class stest(test):
    def __init__(self,budget,windows,fm,work_for,stream,itx,hackintosh,slient):
     self.budget=budget
     self.windows=windows
     self.fm=fm
     self.work_for=work_for
     self.stream=stream
     self.itx=itx
     self.hackintosh=hackintosh
     self.slient=slient
    def search(self):

      for index in range(len(list)):
       if ask.__dir__(self) ==list[index[0:7]]:
        return (list[index.link])

       else:
          print("目前無任何資料!")
      
ask_budget = int(input('請輸入您的預算 = (單位為K)'))
ask_windows = input('有需要正版WIN10系統嗎?(Y or N)')
ask_fm = input('有需要Fluid Montion嗎?(Y or N)')
ask_work_for = input('此電腦的主要工作用途?(F=Fps遊戲 G=其他類型遊戲 C=影音剪輯 W=繪圖軟體)')
ask_stream = input('有實況的需求嗎?(Y or N)')
ask_itx = input('有需要方便攜帶或體積小的用途嗎?(Y or N)')
ask_hackintosh =input('有需要組裝黑蘋果嗎?(Y or N)')
ask_slient =input('有靜音需求嗎?(Y or N)')
ask = stest(ask_budget,ask_windows,ask_fm,ask_work_for,ask_stream,ask_itx,ask_hackintosh,ask_slient)
stest.search(ask)
