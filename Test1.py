
i = []
i.append(int(input('請輸入您的預算 = (單位為K)')))
i.append(input('有需要正版WIN10系統嗎?(Y or N)'))
i.append(input('有需要Fluid Montion嗎?(Y or N)'))
i.append(input('此電腦的主要工作用途?(F=Fps遊戲 G=其他類型遊戲 C=影音剪輯 W=繪圖軟體)'))
i.append(input('有實況的需求嗎?(Y or N)'))
i.append(input('有需要方便攜帶或體積小的用途嗎?(Y or N)'))
i.append(input('有需要組裝黑蘋果嗎?(Y or N)'))
i.append(input('有靜音需求嗎?(Y or N)'))
g=[[55,"N","N","G","N","N","N","N","http://coolpc.com.tw/tmp/1534263382381371.htm"],
    [55,"N","N","G","Y","N","N","N","http://coolpc.com.tw/tmp/153426338552381371.htm"],
   [55,"N","N","F","N","N","N","N","http://coolpc.com.tw/tmp/1534264051610497.htm"]]
search_all= False

for gg in g:
     search = True
     for j in range(2):
           if gg[j] !=  i[j]:
               search =  False
     if  search == True:
               print(g[j][8])
               search_all = True
               break

     if  search_all == False:
               print("目前無相符的項目!")
