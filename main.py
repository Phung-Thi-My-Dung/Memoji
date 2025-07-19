import asyncio
from core.game_engine import GameEngine
from core.word_manager import WordManager
from core.stats_tracker import StatsTracker
from core.history_manager import HistoryManager
from ulti.timer import Timer
from ulti.logger import Logger
from ui.app import PygameUI
import config

async def main():
    logger = Logger(config.settings["log_path"])
    timer = Timer()
    word_manager = WordManager(config.settings["data_path"] + "words.xlsx", logger)
    stats_tracker = StatsTracker(logger)
    history_manager = HistoryManager(config.settings["data_path"] + "history.xlsx", logger)
    ui = PygameUI(history_manager)
    
    game = GameEngine(
        config=config.settings,
        word_manager=word_manager,
        stats_tracker=stats_tracker,
        history_manager=history_manager,
        timer=timer,
        logger=logger
    )

    while True:
        action = await ui.run()
        if action in ["mode1", "mode2", "mode3"]:
            game.start_session(action)
            for _ in range(config.settings["max_questions"]):
                word = game.get_next_word()
                if not word:
                    break
                if action == "mode1":
                    ui.display_word(word.word, word.meanings_english)
                elif action == "mode2":
                    ui.display_word(word.word, word.meanings_vietnamese)
                elif action == "mode3":
                    ui.display_word(word.word)
                
                while True:
                    sub_action = await ui.run()
                    if sub_action == "submit":
                        answer = ui.get_user_answer()
                        is_correct = game.check_answer(word, answer)
                        if action == "mode1":
                            ui.display_result(is_correct, word.meanings_english)
                        elif action == "mode2":
                            ui.display_result(is_correct, word.meanings_vietnamese)
                        elif action == "mode3":
                            ui.display_result(is_correct, word.pos)
                        break
                await asyncio.sleep(2)  # Chờ để người chơi thấy kết quả
            ui.display_session_summary(game.end_session())
        elif action == "stats":
            start_date = input("Enter start date (YYYY-MM-DD, press Enter to skip): ")
            end_date = input("Enter end date (YYYY-MM-DD, press Enter to skip): ")
            ui.show_stats_chart(start_date or None, end_date or None)
        elif action == "exit":
            break

if __name__ == "__main__":
    asyncio.run(main())