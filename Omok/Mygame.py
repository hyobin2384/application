# 인터페이스
from typing import Protocol

class Mygame(Protocol):
    def screen_set(self,width,height):
        '''
        width,height의 크기로 창을 설정해줍니다.
        '''
    
    def screen_name(self,name:str):
        '''
        게임의 이름을 지정해줍니다.
        '''
    
    def image_load(self,path:str):
        '''
        path를 입력하여 이미지를 불러옵니다.
        '''
    
    def color_transparents(target,r,g,b):
        '''
        이미지(target)에서 특정 색을 투명화해주는 기능입니다.
        배경제거에 이용합니다. 
        '''
    
    def get_size(self, target) -> int:
        '''
        이미지(target)의 크기를 알아내는 기능입니다.
        width와 height를 리턴합니다.
        '''

    def bilt(self,screen,target,x,y):
        '''
        어디위에(screen) 어떤것을(target) 그려줍니다.
        x,y좌표로 위치를 설정합니다. 
        '''

    def mouse_click_pos(self) -> int:
        '''
        마우스를 클릭하고 마우스에서 손을땔 때의 좌표를 받아옵니다.
        x,y좌표를 리턴합니다.
        '''

    def max_min_click_range(self,x,y,max):
        '''
        마우스 클릭의 자표가 창을 넘어가지않게 조절해줍니다.
        조절된 x,y좌표를 리턴합니다.
        '''

    def event_get(self):
        '''
        이벤트가 일어나고 있는지 확인합니다.
        '''

    def event_occur(self, event):
        '''
        어떤 이벤트가 일어났는지를 체크해줍니다.
        현재 진행중인 이벤트의 상태를 반환합니다.
        '''
    
    def update(self):
        '''
        창을 새로 업데이트합니다.
        '''

    def finish(self):
        '''
        1초의 여유시간을 두고, 게임을 종료합니다.
        '''