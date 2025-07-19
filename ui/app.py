import pygame
import sys
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
from core.history_manager import HistoryManager
from model.words import Word
from model.session import Session
import platform
import asyncio

class PygameUI:
    def __init__(self, history_manager: HistoryManager):
        pygame.init()
        self.history_manager = history_manager
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Word Game")
        self.font = pygame.font.SysFont("arial", 24)
        self.input_font = pygame.font.SysFont("arial", 20)
        self.colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "gray": (200, 200, 200),
            "blue": (0, 120, 255),
            "green": (0, 200, 0),
            "red": (255, 0, 0)
        }
        self.input_text = ""
        self.active_input = False
        self.state = "menu"
        self.buttons = []
        self.current_word = None
        self.result_message = ""
        self.result_timer = 0
        self.FPS = 60

    def create_button(self, text, x, y, width, height, action):
        return {"text": text, "rect": pygame.Rect(x, y, width, height), "action": action}

    async def draw_menu(self):
        self.buttons = [
            self.create_button("Mode 1: English Meaning", 300, 100, 200, 50, "mode1"),
            self.create_button("Mode 2: Vietnamese Meaning", 300, 160, 200, 50, "mode2"),
            self.create_button("Mode 3: Part of Speech", 300, 220, 200, 50, "mode3"),
            self.create_button("Show Statistics", 300, 280, 200, 50, "stats"),
            self.create_button("Exit", 300, 340, 200, 50, "exit")
        ]
        self.screen.fill(self.colors["white"])
        title = self.font.render("Word Game Menu", True, self.colors["black"])
        self.screen.blit(title, (300, 50))
        for button in self.buttons:
            pygame.draw.rect(self.screen, self.colors["gray"], button["rect"])
            text = self.font.render(button["text"], True, self.colors["black"])
            text_rect = text.get_rect(center=button["rect"].center)
            self.screen.blit(text, text_rect)
        pygame.display.flip()
        await asyncio.sleep(1.0 / self.FPS)

    async def draw_game(self, prompt: str, example: str = ""):
        self.screen.fill(self.colors["white"])
        question = self.font.render(f"Question: {prompt}", True, self.colors["black"])
        self.screen.blit(question, (50, 100))
        if example:
            example_text = self.font.render(f"Example: {example}", True, self.colors["black"])
            self.screen.blit(example_text, (50, 150))
        
        input_box = pygame.Rect(50, 200, 400, 40)
        pygame.draw.rect(self.screen, self.colors["black"], input_box, 2)
        input_surface = self.input_font.render(self.input_text, True, self.colors["black"])
        self.screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))
        
        submit_button = self.create_button("Submit", 460, 200, 100, 40, "submit")
        pygame.draw.rect(self.screen, self.colors["blue"], submit_button["rect"])
        text = self.font.render("Submit", True, self.colors["white"])
        text_rect = text.get_rect(center=submit_button["rect"].center)
        self.screen.blit(text, text_rect)
        
        if self.result_message:
            color = self.colors["green"] if "Correct" in self.result_message else self.colors["red"]
            result_text = self.font.render(self.result_message, True, color)
            self.screen.blit(result_text, (50, 300))
        
        self.buttons = [submit_button]
        pygame.display.flip()
        await asyncio.sleep(1.0 / self.FPS)

    async def draw_session_summary(self, session: Session):
        self.screen.fill(self.colors["white"])
        lines = [
            f"Session ID: {session.session_id}",
            f"Mode: {session.mode}",
            f"Player: {session.player_name}",
            f"Score: {session.score}",
            f"Correct: {session.correct_count}",
            f"Wrong: {session.wrong_count}",
            f"Duration: {session.duration:.2f} seconds",
            f"Words used: {', '.join(session.words_used)}"
        ]
        for i, line in enumerate(lines):
            text = self.font.render(line, True, self.colors["black"])
            self.screen.blit(text, (50, 100 + i * 40))
        
        back_button = self.create_button("Back to Menu", 300, 400, 200, 50, "back")
        pygame.draw.rect(self.screen, self.colors["blue"], back_button["rect"])
        text = self.font.render("Back to Menu", True, self.colors["white"])
        text_rect = text.get_rect(center=back_button["rect"].center)
        self.screen.blit(text, text_rect)
        
        self.buttons = [back_button]
        pygame.display.flip()
        await asyncio.sleep(1.0 / self.FPS)

    async def draw_stats_chart(self, start_date: str = None, end_date: str = None):
        sessions = self.history_manager.load_history(start_date, end_date)
        if not sessions:
            self.screen.fill(self.colors["white"])
            text = self.font.render("No history data available.", True, self.colors["black"])
            self.screen.blit(text, (50, 100))
            back_button = self.create_button("Back to Menu", 300, 400, 200, 50, "back")
            pygame.draw.rect(self.screen, self.colors["blue"], back_button["rect"])
            text = self.font.render("Back to Menu", True, self.colors["white"])
            text_rect = text.get_rect(center=back_button["rect"].center)
            self.screen.blit(text, text_rect)
            self.buttons = [back_button]
            pygame.display.flip()
            await asyncio.sleep(1.0 / self.FPS)
            return

        df = pd.DataFrame([
            {
                "timestamp": s.timestamp,
                "score": s.score,
                "correct_count": s.correct_count,
                "wrong_count": s.wrong_count,
                "duration": s.duration
            } for s in sessions
        ])

        plt.figure(figsize=(8, 6))
        plt.subplot(2, 1, 1)
        plt.plot(df["timestamp"], df["score"], marker="o", label="Score")
        plt.title("Score Over Time")
        plt.xlabel("Time")
        plt.ylabel("Score")
        plt.grid(True)
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(df["timestamp"], df["correct_count"], marker="o", label="Correct")
        plt.plot(df["timestamp"], df["wrong_count"], marker="x", label="Wrong")
        plt.title("Correct vs Wrong Answers Over Time")
        plt.xlabel("Time")
        plt.ylabel("Count")
        plt.grid(True)
        plt.legend()

        plt.tight_layout()
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        image = Image.open(buffer)
        mode = image.mode
        size = image.size
        data = image.tobytes()
        pygame_image = pygame.image.fromstring(data, size, mode)
        plt.close()

        self.screen.fill(self.colors["white"])
        self.screen.blit(pygame_image, (50, 50))
        back_button = self.create_button("Back to Menu", 300, 500, 200, 50, "back")
        pygame.draw.rect(self.screen, self.colors["blue"], back_button["rect"])
        text = self.font.render("Back to Menu", True, self.colors["white"])
        text_rect = text.get_rect(center=back_button["rect"].center)
        self.screen.blit(text, text_rect)
        
        self.buttons = [back_button]
        pygame.display.flip()
        await asyncio.sleep(1.0 / self.FPS)

    def display_menu(self) -> str:
        self.state = "menu"
        return ""

    def display_word(self, prompt: str, example: str = ""):
        self.state = "game"
        self.current_prompt = prompt
        self.current_example = example
        self.input_text = ""
        self.active_input = True
        self.result_message = ""

    def get_user_answer(self) -> str:
        return self.input_text

    def display_result(self, is_correct: bool, correct_answer: str):
        self.result_message = f"{'Correct!' if is_correct else f'Wrong! Correct answer: {correct_answer}'}"
        self.result_timer = pygame.time.get_ticks() + 2000  # Hiển thị kết quả trong 2 giây
        self.active_input = False

    def display_session_summary(self, session: Session):
        self.state = "summary"
        self.current_session = session

    def show_stats_chart(self, start_date: str = None, end_date: str = None):
        self.state = "stats"
        self.start_date = start_date
        self.end_date = end_date

    async def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button["rect"].collidepoint(event.pos):
                        return button["action"]
            if event.type == pygame.KEYDOWN and self.state == "game" and self.active_input:
                if event.key == pygame.K_RETURN:
                    return "submit"
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                elif event.unicode.isprintable():
                    self.input_text += event.unicode
        return None

    async def run(self):
        while True:
            if self.state == "menu":
                await self.draw_menu()
            elif self.state == "game":
                await self.draw_game(self.current_prompt, self.current_example)
                if self.result_timer and pygame.time.get_ticks() > self.result_timer:
                    self.result_message = ""
                    self.result_timer = 0
                    self.active_input = True
            elif self.state == "summary":
                await self.draw_session_summary(self.current_session)
            elif self.state == "stats":
                await self.draw_stats_chart(self.start_date, self.end_date)
            
            action = await self.handle_events()
            if action:
                return action
            await asyncio.sleep(1.0 / self.FPS)

async def main():
    history_manager = HistoryManager("data/history.xlsx", Logger())
    ui = PygameUI(history_manager)
    await ui.run()

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())