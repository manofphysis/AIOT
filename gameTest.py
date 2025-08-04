import pygame
import sys
import math

# 초기화
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

# 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("벽돌깨기 게임")

# 게임 설정
FPS = 60
clock = pygame.time.Clock()

class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - 50
        self.speed = 8
        
    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
            
    def move_right(self):
        if self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed
            
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Ball:
    def __init__(self):
        self.radius = 10
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x = 5
        self.speed_y = -5
        
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
        # 벽과의 충돌 검사
        if self.x <= self.radius or self.x >= SCREEN_WIDTH - self.radius:
            self.speed_x = -self.speed_x
        if self.y <= self.radius:
            self.speed_y = -self.speed_y
            
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)
        
    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 
                          self.radius * 2, self.radius * 2)
                          
    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x = 5
        self.speed_y = -5

class Brick:
    def __init__(self, x, y, color):
        self.width = 75
        self.height = 30
        self.x = x
        self.y = y
        self.color = color
        self.destroyed = False
        
    def draw(self, screen):
        if not self.destroyed:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)
            
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Game:
    def __init__(self):
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = []
        self.score = 0
        self.lives = 3
        self.font = pygame.font.Font(None, 36)
        self.create_bricks()
        
    def create_bricks(self):
        colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE]
        brick_rows = 7
        brick_cols = 10
        
        for row in range(brick_rows):
            for col in range(brick_cols):
                x = col * 80 + 5
                y = row * 35 + 50
                color = colors[row % len(colors)]
                self.bricks.append(Brick(x, y, color))
                
    def handle_collision(self):
        # 패들과 볼의 충돌
        if self.ball.get_rect().colliderect(self.paddle.get_rect()):
            if self.ball.speed_y > 0:  # 볼이 아래로 향할 때만
                # 패들의 어느 부분에 맞았는지에 따라 각도 조정
                hit_pos = (self.ball.x - self.paddle.x) / self.paddle.width
                angle = (hit_pos - 0.5) * math.pi / 3  # -60도에서 60도 사이
                speed = math.sqrt(self.ball.speed_x**2 + self.ball.speed_y**2)
                self.ball.speed_x = speed * math.sin(angle)
                self.ball.speed_y = -abs(speed * math.cos(angle))
        
        # 벽돌과 볼의 충돌
        for brick in self.bricks:
            if not brick.destroyed and self.ball.get_rect().colliderect(brick.get_rect()):
                brick.destroyed = True
                self.score += 10
                
                # 충돌 방향에 따라 볼의 방향 변경
                ball_center_x = self.ball.x
                ball_center_y = self.ball.y
                brick_center_x = brick.x + brick.width // 2
                brick_center_y = brick.y + brick.height // 2
                
                # 수직 충돌인지 수평 충돌인지 판단
                dx = abs(ball_center_x - brick_center_x)
                dy = abs(ball_center_y - brick_center_y)
                
                if dx / brick.width > dy / brick.height:
                    self.ball.speed_x = -self.ball.speed_x
                else:
                    self.ball.speed_y = -self.ball.speed_y
                break
                
    def check_game_over(self):
        # 볼이 화면 아래로 떨어짐
        if self.ball.y > SCREEN_HEIGHT:
            self.lives -= 1
            if self.lives > 0:
                self.ball.reset()
                return False
            else:
                return True
                
        # 모든 벽돌이 파괴됨
        if all(brick.destroyed for brick in self.bricks):
            return True
            
        return False
        
    def reset_game(self):
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = []
        self.score = 0
        self.lives = 3
        self.create_bricks()
        
    def draw(self, screen):
        screen.fill(BLACK)
        
        # 게임 객체들 그리기
        self.paddle.draw(screen)
        self.ball.draw(screen)
        
        for brick in self.bricks:
            brick.draw(screen)
            
        # UI 그리기
        score_text = self.font.render(f"점수: {self.score}", True, WHITE)
        lives_text = self.font.render(f"생명: {self.lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))
        
        # 게임 오버 또는 승리 메시지
        if self.lives <= 0:
            game_over_text = self.font.render("게임 오버! R키를 눌러 재시작", True, RED)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(game_over_text, text_rect)
        elif all(brick.destroyed for brick in self.bricks):
            win_text = self.font.render("승리! R키를 눌러 재시작", True, GREEN)
            text_rect = win_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(win_text, text_rect)
            
    def update(self):
        if self.lives > 0 and not all(brick.destroyed for brick in self.bricks):
            self.ball.move()
            self.handle_collision()

def main():
    game = Game()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset_game()
        
        # 키 입력 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            game.paddle.move_left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            game.paddle.move_right()
            
        # 게임 업데이트
        game.update()
        
        # 게임 오버 체크
        if game.check_game_over() and game.lives <= 0:
            pass  # 게임 오버 상태 유지
            
        # 화면 그리기
        game.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()