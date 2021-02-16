import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """버튼 속성을 초기화합니다"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 버튼의 크기와 프로퍼티를 정한다
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) # pygame.font 모듈은 화면 텍스트 렌더링을 담당

        # 버튼의 rect 객체를 만들고 중앙에 배치한다
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 버튼 메시지는 한 번만
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """msg를 이미지로 렌더링하고 버튼 중앙에 배치합니다"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color) # 여기서 불리언값은 텍스트 경계를 부드럽게 하는 것
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 빈 버튼을 그리고 메시지를 렌더링
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

