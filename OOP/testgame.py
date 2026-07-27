import pygame
import random
import sys
import time

# Khởi tạo Pygame
pygame.init()
pygame.font.init()

# Cấu hình Màn hình
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 720
FPS = 60

# Màu sắc
BG_COLOR = (20, 24, 33)
PANEL_BG = (32, 38, 52)
TEXT_COLOR = (240, 240, 240)
BTN_ACTIVE = (52, 152, 219)        # Xanh sáng: Đi được
BTN_INACTIVE = (60, 65, 80)        # Xám tối: Bị tường cản
BTN_FROZEN = (100, 40, 40)         # Đỏ tối: Khi bị đóng băng phạt
BTN_TEXT_ACTIVE = (255, 255, 255)
BTN_TEXT_INACTIVE = (120, 125, 140)

MAZE_WALL_COLOR = (231, 76, 60)    # Màu tường người chơi đặt (Đỏ)
MAZE_GRID_COLOR = (70, 80, 100)     # Đường lưới mờ
PLAYER_COLOR = (46, 204, 113)      # Vị trí hiện tại (Xanh lá)

GRID_SIZE = 9
CELL_SIZE = 48
MAP_X = 580
MAP_Y = 160

# HÀM HỖ TRỢ PHÔNG CHỮ TIẾNG VIỆT
def get_vietnamese_font(size, bold=False):
    system_fonts = ["segoeui", "arial", "tahoma", "helvetica"]
    for font_name in system_fonts:
        font_path = pygame.font.match_font(font_name, bold=bold)
        if font_path:
            return pygame.font.Font(font_path, size)
    return pygame.font.SysFont(None, size)

class FogWalker9x9:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Siêu Trí Tuệ - Mê Vũ Hành Giả (9x9)")
        self.clock = pygame.time.Clock()
        
        # Load phông chữ Tiếng Việt
        self.font_large = get_vietnamese_font(24, bold=True)
        self.font_medium = get_vietnamese_font(17, bold=True)
        self.font_small = get_vietnamese_font(14)
        
        self.reset_game()

    def reset_game(self):
        # Mê cung 9x9 ẩn
        self.hidden_horiz = [[False]*GRID_SIZE for _ in range(GRID_SIZE - 1)]
        self.hidden_vert = [[False]*(GRID_SIZE - 1) for _ in range(GRID_SIZE)]
        
        # Vị trí xuất phát ở trung tâm (4, 4) - Khai báo trước khi sinh mê cung
        self.px = GRID_SIZE // 2
        self.py = GRID_SIZE // 2

        self._generate_open_maze()

        # Bàn vẽ của người chơi
        self.user_horiz = [[False]*GRID_SIZE for _ in range(GRID_SIZE - 1)]
        self.user_vert = [[False]*(GRID_SIZE - 1) for _ in range(GRID_SIZE)]

        # Bộ đếm thời gian
        self.start_time = time.time()
        self.elapsed_time = 0
        
        # Cơ chế Phạt & Đóng băng
        self.freeze_until = 0           # Thời điểm kết thúc đóng băng phạt
        self.penalty_step = 10          # Mức phạt đóng băng lần sai tiếp theo (s)
        
        self.game_completed = False
        self.status_msg = "Dùng phím Mũi tên để di chuyển, dùng Chuột để dựng lại mê cung!"

    def _generate_open_maze(self):
        """ Sinh mê cung KHÔNG khép kín (Mở rộng) """
        for r in range(GRID_SIZE - 1):
            for c in range(GRID_SIZE):
                self.hidden_horiz[r][c] = (random.random() < 0.40)

        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE - 1):
                self.hidden_vert[r][c] = (random.random() < 0.40)

        # Đảm bảo mọi ô đều có thể đi tới được
        def get_neighbors(r, c):
            neighbors = []
            if r > 0 and not self.hidden_horiz[r-1][c]: neighbors.append((r-1, c))
            if r < GRID_SIZE - 1 and not self.hidden_horiz[r][c]: neighbors.append((r+1, c))
            if c > 0 and not self.hidden_vert[r][c-1]: neighbors.append((r, c-1))
            if c < GRID_SIZE - 1 and not self.hidden_vert[r][c]: neighbors.append((r, c+1))
            return neighbors

        visited = set()
        queue = [(self.py, self.px)]
        visited.add((self.py, self.px))

        while queue:
            curr_r, curr_c = queue.pop(0)
            for nr, nc in get_neighbors(curr_r, curr_c):
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        # Phá tường nếu có ô bị cô lập
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if (r, c) not in visited:
                    adj = []
                    if r > 0: adj.append(('UP', r-1, c))
                    if r < GRID_SIZE - 1: adj.append(('DOWN', r+1, c))
                    if c > 0: adj.append(('LEFT', r, c-1))
                    if c < GRID_SIZE - 1: adj.append(('RIGHT', r, c+1))
                    
                    random.shuffle(adj)
                    for d, ar, ac in adj:
                        if d == 'UP': self.hidden_horiz[r-1][c] = False
                        elif d == 'DOWN': self.hidden_horiz[r][c] = False
                        elif d == 'LEFT': self.hidden_vert[r][c-1] = False
                        elif d == 'RIGHT': self.hidden_vert[r][c] = False
                        break

    def is_frozen(self):
        """ Kiểm tra xem người chơi có đang bị phạt đóng băng không """
        return time.time() < self.freeze_until

    def get_remaining_freeze(self):
        """ Lấy số giây còn lại bị phạt đóng băng """
        return max(0, int(self.freeze_until - time.time()) + 1)

    def get_dir_status(self):
        """ Kiểm tra 4 hướng đi tại ô hiện tại """
        up = (self.py > 0) and not self.hidden_horiz[self.py - 1][self.px]
        down = (self.py < GRID_SIZE - 1) and not self.hidden_horiz[self.py][self.px]
        left = (self.px > 0) and not self.hidden_vert[self.py][self.px - 1]
        right = (self.px < GRID_SIZE - 1) and not self.hidden_vert[self.py][self.px]
        return {"UP": up, "DOWN": down, "LEFT": left, "RIGHT": right}

    def move_player(self, dr, dc):
        # Không cho di chuyển nếu đã thắng hoặc đang bị đóng băng phạt
        if self.game_completed or self.is_frozen():
            return
        
        status = self.get_dir_status()
        if dr == -1 and status["UP"]: self.py -= 1
        elif dr == 1 and status["DOWN"]: self.py += 1
        elif dc == -1 and status["LEFT"]: self.px -= 1
        elif dc == 1 and status["RIGHT"]: self.px += 1

    def handle_mouse_click(self, pos):
        # Không cho click sửa tường nếu đã thắng hoặc đang bị đóng băng phạt
        if self.game_completed or self.is_frozen():
            return
            
        mx, my = pos
        
        # Tương tác click chuột vào các đường biên 9x9
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                x = MAP_X + c * CELL_SIZE
                y = MAP_Y + r * CELL_SIZE
                
                # Tường ngang
                if r < GRID_SIZE - 1:
                    wall_rect = pygame.Rect(x, y + CELL_SIZE - 6, CELL_SIZE, 12)
                    if wall_rect.collidepoint(mx, my):
                        self.user_horiz[r][c] = not self.user_horiz[r][c]
                        return

                # Tường dọc
                if c < GRID_SIZE - 1:
                    wall_rect = pygame.Rect(x + CELL_SIZE - 6, y, 12, CELL_SIZE)
                    if wall_rect.collidepoint(mx, my):
                        self.user_vert[r][c] = not self.user_vert[r][c]
                        return

        # Nút Nộp Bài
        btn_check = pygame.Rect(MAP_X, MAP_Y + GRID_SIZE * CELL_SIZE + 20, GRID_SIZE * CELL_SIZE, 45)
        if btn_check.collidepoint(mx, my):
            self.check_result()

    def check_result(self):
        if self.user_horiz == self.hidden_horiz and self.user_vert == self.hidden_vert:
            self.game_completed = True
            total_time = int(self.elapsed_time)
            self.status_msg = f"🎉 CHÍNH XÁC 100%! Hoàn thành mê cung trong {total_time} giây."
        else:
            # Áp dụng án phạt đóng băng
            freeze_duration = self.penalty_step
            self.freeze_until = time.time() + freeze_duration
            
            # Tăng mức phạt lần sau (tối đa 50s)
            next_penalty = min(50, self.penalty_step + 10)
            self.status_msg = f"❌ CHƯA CHÍNH XÁC! Bị đóng băng {freeze_duration}s. (Lần sai tới phạt {next_penalty}s)"
            self.penalty_step = next_penalty

    def update_timer(self):
        if not self.game_completed:
            self.elapsed_time = time.time() - self.start_time

    def draw_dpad_button(self, text, active, pos, size=(100, 70)):
        x, y = pos
        if self.is_frozen():
            bg_col = BTN_FROZEN
            txt_col = BTN_TEXT_INACTIVE
        else:
            bg_col = BTN_ACTIVE if active else BTN_INACTIVE
            txt_col = BTN_TEXT_ACTIVE if active else BTN_TEXT_INACTIVE
        
        pygame.draw.rect(self.screen, bg_col, (x, y, size[0], size[1]), border_radius=10)
        lbl = self.font_medium.render(text, True, txt_col)
        self.screen.blit(lbl, lbl.get_rect(center=(x + size[0]//2, y + size[1]//2)))

    def draw(self):
        self.screen.fill(BG_COLOR)

        # Header Info
        time_str = time.strftime("%M:%S", time.gmtime(self.elapsed_time))
        timer_lbl = self.font_large.render(f"⏱️ THỜI GIAN: {time_str}", True, (241, 196, 15))
        self.screen.blit(timer_lbl, (40, 20))

        # Hiển thị đếm ngược nếu đang bị phạt đóng băng
        if self.is_frozen():
            freeze_rem = self.get_remaining_freeze()
            freeze_lbl = self.font_large.render(f"⛔ ĐANG BỊ PHẠT ĐÓNG BĂNG: {freeze_rem}s", True, (231, 76, 60))
            self.screen.blit(freeze_lbl, (280, 20))

        # Nút Reset Game
        pygame.draw.rect(self.screen, (192, 57, 43), (900, 15, 160, 40), border_radius=8)
        lbl_reset = self.font_medium.render("R - Game Mới", True, (255, 255, 255))
        self.screen.blit(lbl_reset, lbl_reset.get_rect(center=(980, 35)))

        # Thông báo trạng thái
        status_color = (46, 204, 113) if "CHÍNH XÁC" in self.status_msg else ((231, 76, 60) if "CHƯA CHÍNH XÁC" in self.status_msg else (180, 190, 200))
        status_lbl = self.font_small.render(self.status_msg, True, status_color)
        self.screen.blit(status_lbl, (40, 65))

        # ==================== BẢNG TRÁI: HÀNH GIẢ ====================
        pygame.draw.rect(self.screen, PANEL_BG, (30, 100, 480, 580), border_radius=15)
        title_left = self.font_medium.render("HÀNH GIẢ (BỘ ĐIỀU KHIỂN SÁNG/TẮT)", True, TEXT_COLOR)
        self.screen.blit(title_left, (50, 120))

        # D-PAD Nút di chuyển
        status = self.get_dir_status()
        self.draw_dpad_button("▲ LÊN", status["UP"], (220, 170))
        self.draw_dpad_button("◄ TRÁI", status["LEFT"], (105, 250))
        self.draw_dpad_button("PHẢI ►", status["RIGHT"], (335, 250))
        self.draw_dpad_button("▼ XUỐNG", status["DOWN"], (220, 330))

        # Hướng dẫn
        pos_txt = self.font_small.render(f"Tọa độ hiện tại: Cột {self.px + 1} - Hàng {self.py + 1}", True, (150, 160, 180))
        note_txt1 = self.font_small.render("* Nút HIỆN SÁNG (Xanh) = Ô đi được", True, BTN_ACTIVE)
        note_txt2 = self.font_small.render("* Nút TẮT SÁNG (Xám) = Bị tường cản", True, (140, 145, 160))
        note_txt3 = self.font_small.render("* Nộp sai sẽ bị KHÓA DI CHUYỂN theo đếm ngược phạt!", True, (231, 76, 60))
        
        self.screen.blit(pos_txt, (50, 430))
        self.screen.blit(note_txt1, (50, 465))
        self.screen.blit(note_txt2, (50, 495))
        self.screen.blit(note_txt3, (50, 525))

        # ==================== BẢNG PHẢI: HỌA ĐỒ SƯ (9x9) ====================
        pygame.draw.rect(self.screen, PANEL_BG, (540, 100, 520, 580), border_radius=15)
        title_right = self.font_medium.render("HỌA ĐỒ SƯ (KHÔI PHỤC MÊ CUNG 9x9)", True, TEXT_COLOR)
        self.screen.blit(title_right, (560, 120))

        # Vẽ Lưới Ma Trận 9x9
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                x = MAP_X + c * CELL_SIZE
                y = MAP_Y + r * CELL_SIZE
                
                # Ô vuông background
                cell_bg = (55, 30, 35) if self.is_frozen() else (40, 46, 62)
                pygame.draw.rect(self.screen, cell_bg, (x, y, CELL_SIZE-2, CELL_SIZE-2))
                
                # Biểu thị vị trí hiện tại
                p_col = (150, 150, 150) if self.is_frozen() else PLAYER_COLOR
                if c == self.px and r == self.py:
                    pygame.draw.circle(self.screen, p_col, (x + CELL_SIZE//2, y + CELL_SIZE//2), 9)

                # Vẽ tường người chơi đặt (Ngang)
                if r < GRID_SIZE - 1:
                    w_col = MAZE_WALL_COLOR if self.user_horiz[r][c] else MAZE_GRID_COLOR
                    thickness = 5 if self.user_horiz[r][c] else 1
                    pygame.draw.line(self.screen, w_col, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), thickness)

                # Vẽ tường người chơi đặt (Dọc)
                if c < GRID_SIZE - 1:
                    w_col = MAZE_WALL_COLOR if self.user_vert[r][c] else MAZE_GRID_COLOR
                    thickness = 5 if self.user_vert[r][c] else 1
                    pygame.draw.line(self.screen, w_col, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), thickness)

        # Khung viền ngoài
        pygame.draw.rect(self.screen, (200, 200, 200), (MAP_X, MAP_Y, GRID_SIZE*CELL_SIZE, GRID_SIZE*CELL_SIZE), 2)

        # Nút Nộp Bài
        btn_check_rect = pygame.Rect(MAP_X, MAP_Y + GRID_SIZE * CELL_SIZE + 20, GRID_SIZE*CELL_SIZE, 45)
        
        if self.is_frozen():
            btn_bg = (100, 100, 100)
            lbl_check_text = f"ĐANG KHÓA PHẠT ({self.get_remaining_freeze()}s)"
        else:
            btn_bg = (46, 204, 113)
            lbl_check_text = f"NỘP BÀI & KIỂM TRA (Sai phạt đóng băng {self.penalty_step}s)"

        pygame.draw.rect(self.screen, btn_bg, btn_check_rect, border_radius=8)
        lbl_check = self.font_medium.render(lbl_check_text, True, (255, 255, 255))
        self.screen.blit(lbl_check, lbl_check.get_rect(center=btn_check_rect.center))

        pygame.display.flip()

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.update_timer()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_mouse_click(event.pos)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        self.move_player(-1, 0)
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.move_player(1, 0)
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.move_player(0, -1)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.move_player(0, 1)

            self.draw()

if __name__ == "__main__":
    game = FogWalker9x9()
    game.run()