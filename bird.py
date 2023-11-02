import game_framework


class Bird:
    def __init__(self):
        from pico2d import load_image
        self.bird_img = load_image('bird_animation.png')
        self.bird_dir = 1
        from random import randint
        self.bird_kph = randint(10,100) # 시간당10키로 , 100키로
        self.bird_width,self.bird_height = 183,168
        self.acc_time = 0.0
        self.bird_frame = 0
        self.bird_frame_time = 0.2 # 0.2초에 한번 날갯짓 => 초당 5번
        self.x,self.y = 500,500
        # 1픽셀 3센치
        # 1.5m , 1.5m 150cm
        # 50 ,50
        self.bird_width = 50
        self.bird_height = 50
        self.cur_action_x,self.cur_action_y = 0,0
    def bird_move(self):
        PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
        RUN_SPEED_KMPH = self.bird_kph
        RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
        self.x += self.bird_dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x + self.bird_width/4 >= 1600:
            self.bird_dir = -1
        if self.x <= self.bird_width/4:
            self.bird_dir = 1

    def update(self):
        self.bird_move()
        self.acc_time += game_framework.frame_time
        if self.acc_time >= self.bird_frame_time:
            self.acc_time = 0.0
            self.bird_frame = (self.bird_frame + 1) % 4
            if self.cur_action_y != 3:
                temp = (self.cur_action_x + 1)
                if temp == 5:
                    self.cur_action_y = (self.cur_action_y + 1) % 3
                self.cur_action_x = temp % 4
            else:
                temp = (self.cur_action_x + 1)
                if temp == 4:
                    self.cur_action_y = (self.cur_action_y + 1) % 3
                self.cur_action_x = temp % 4
    def draw(self):
        dir = 'h' if self.bird_dir != 1 else ''
        self.bird_img.clip_composite_draw(180 * self.cur_action_x ,168 * (2 - self.cur_action_y),
                                          180,
                                          168,
                                          0,
                                          dir,
                                          self.x,
                                          self.y,
                                          self.bird_width,
                                          self.bird_height)