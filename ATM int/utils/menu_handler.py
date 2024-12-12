from typing import Dict, Callable
from utils.menu_display import MenuDisplay

class MenuHandler:
    def __init__(self):
        self.actions: Dict[str, Callable] = {}
        
    def register_action(self, choice: str, action: Callable):
        self.actions[choice] = action
        
    def handle_choice(self, choice: str) -> bool:
        if choice in self.actions:
            self.actions[choice]()
            return True
        return False