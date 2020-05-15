import pygame


class ScheduledEventsHandler:
    def __init__(self, wallet, grid):
        self.wallet = wallet
        self.grid = grid

    def calculate_income(self):
        sum = 0
        for block in self.grid.blocks.values():
            sum += self.wallet.get_income(block['name'])

        return sum

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT+1:
                amount_to_earn = self.calculate_income()
                self.wallet.add(amount_to_earn)