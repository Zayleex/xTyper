import pygame

import math
import random

from enemy import Enemy
from player import Player
from hud_elements import HealthBar, Score, Timer
from ui_elements import HeaderText, Button
from bullet import Bullet
from background import Background
import constants

class Game:
    def __init__(self, screen):
        #Defining screen and Hud
        self.screen = screen
        self.hud_layer = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        #Calculating center (making calculations easier)
        #Initialise objects
        self.player = Player(self.screen)
        self.health_bar = HealthBar(self.hud_layer)
        self.score = Score(self.hud_layer)
        self.timer = Timer(self.hud_layer)
        self.background = Background().get_background(screen.get_width(), screen.get_height())
        #Initialise needed variables
        self.enemy_list = []
        self.bullet_list = []
        self.dt = 0
        self.paused = False
        self.last_spawn = "left"
        self.game_over = False
        self.spawnrate = 3000
        self.internal_timer = 0
        self.timer_threshold = 30
        #Define events
        self.SPAWN_ENEMY = pygame.USEREVENT + 1
        self.INCREASE_TIMER = pygame.USEREVENT + 2
        pygame.time.set_timer(self.SPAWN_ENEMY, 3000)
        pygame.time.set_timer(self.INCREASE_TIMER, 1000)
        self.pause_header = HeaderText("PAUSE", self.screen.get_width() // 2, self.screen.get_height() // 4, screen)
        self.continue_button = Button("CONTINUE", self.screen.get_width() // 2, self.screen.get_height() // 2, 300, 70, screen)

        self.game_over_header = HeaderText("GAME OVER", self.screen.get_width() // 2, self.screen.get_height() // 4, screen)
        self.retry_button = Button("RETRY", self.screen.get_width() // 2, self.screen.get_height() // 2, 300, 70, screen)
        self.quit_button = Button("QUIT", self.screen.get_width() // 2, (self.screen.get_height() // 2) + 100, 300, 70, screen)

    def run(self, events):
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                return "QUIT"


            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.paused = not self.paused
                if not self.paused:
                    pygame.event.clear(self.SPAWN_ENEMY)
                    pygame.event.clear(self.INCREASE_TIMER)
                continue


            if self.game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.retry_button.is_clicked(event, mouse_pos):
                        self.reset_game()
                        return "GAME"
                    if self.quit_button.is_clicked(event, mouse_pos):
                        self.reset_game()
                        return "MENU"
                continue


            if self.paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.continue_button.is_clicked(event, mouse_pos):
                        self.paused = False
                    if self.quit_button.is_clicked(event, mouse_pos):
                        self.reset_game()
                        return "MENU"
                continue


            if not self.paused:
                if event.type == pygame.KEYDOWN:
                    self.handle_input(event.unicode)

                elif event.type == self.SPAWN_ENEMY:
                    self.spawn_enemy()

                elif event.type == self.INCREASE_TIMER:
                    self.handle_timer_increase()

        if not self.paused and not self.game_over:
            self.update()

        self.draw()
        self.draw_ui(mouse_pos)

        return "GAME"


    def update(self):
        # Bullet & Enemy cleanup
        self.enemy_list = [e for e in self.enemy_list if e.alive]
        self.bullet_list = [b for b in self.bullet_list if b.alive]
        for bullet in self.bullet_list:
            bullet.update(self.dt)
            if self.check_collision(bullet, bullet.target):
                bullet.alive = False
                if bullet.version == bullet.target.version:
                    bullet.target.take_damage()
                    if not bullet.target.alive:
                        self.score.add_points(len(bullet.target.word))
                        self.score.add_multiplier()

        for enemy in self.enemy_list:
            enemy.update(self.dt)
            if self.check_collision(self.player, enemy):
                enemy.alive = False
                self.health_bar.decrease_health()
                if self.health_bar.health <= 0:
                    self.game_over = True
                self.score.reset_multiplier()
        self.player.update(self.dt)


    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw()
        for enemy in self.enemy_list:
            enemy.draw()
        for bullet in self.bullet_list:
            bullet.draw()


    def draw_ui(self, mouse_pos):
        self.hud_layer.fill((0, 0, 0, 0))
        self.health_bar.draw()
        self.score.draw()
        self.timer.draw()
        if self.game_over:
            self.game_over_header.draw()
            self.retry_button.draw(mouse_pos)
            self.quit_button.draw(mouse_pos)
        if self.paused:
            self.pause_header.draw()
            self.continue_button.draw(mouse_pos)
            self.quit_button.draw(mouse_pos)
        self.screen.blit(self.hud_layer, (0, 0))


    def handle_input(self, key):
        if key == "":
            return
        hit_any_enemy = False
        for enemy in self.enemy_list:
            if enemy.check_input(key):
                hit_any_enemy = True
                self.player.calculate_state_from_angle(self.get_angle_to_target(self.player, enemy))
                bullet = Bullet(self.screen, key, enemy, enemy.version)
                self.bullet_list.append(bullet)
        if not hit_any_enemy:
            self.score.reset_multiplier()


    def spawn_enemy(self):
        max_x = self.screen.get_width()
        max_y = self.screen.get_height()
        distance_x = max_x / 8
        distance_y = max_y / 5

        word = random.choice(constants.word_list)

        spawn_options = ["left", "upper", "right", "bottom"]
        spawn_options.remove(self.last_spawn)
        spawn_coordinates = {
            "left": (0, random.randint(0, 5) * distance_y),
            "upper": (random.randint(0, 10) * distance_x, 0),
            "right": (max_x, random.randint(0, 5) * distance_y),
            "bottom": (random.randint(0, 10) * distance_x, max_y)
        }

        spawn_location = random.choice(spawn_options)
        x_coord = spawn_coordinates[spawn_location][0]
        y_coord = spawn_coordinates[spawn_location][1]

        e = Enemy(word,
                  self.screen,
                  x_coord,
                  y_coord,)
        self.enemy_list.append(e)
        self.last_spawn = spawn_location

    def increase_spawnrate(self):
        self.spawnrate -= 250
        pygame.time.set_timer(self.SPAWN_ENEMY, self.spawnrate)

    @staticmethod
    def check_collision(object_1, object_2):
        """Calculates if two objects collide"""
        dx = object_1.pos_x - object_2.pos_x
        dy = object_1.pos_y - object_2.pos_y
        distance = math.sqrt(pow(dx, 2) + pow(dy, 2))
        if distance < object_1.hitbox_radius + object_2.hitbox_radius:
            return True
        else:
            return False

    def reset_game(self):
        self.player = Player(self.screen)
        self.health_bar = HealthBar(self.hud_layer)
        self.score = Score(self.hud_layer)
        self.timer = Timer(self.hud_layer)
        self.spawnrate = 3000
        self.enemy_list = []
        self.bullet_list = []
        self.last_spawn = "left"
        self.game_over = False
        self.paused = False
        self.internal_timer = 0
        self.timer_threshold = 30
        pygame.time.set_timer(self.SPAWN_ENEMY, 3000)
        pygame.time.set_timer(self.INCREASE_TIMER, 1000)

    @staticmethod
    def get_angle_to_target(object_1, object_2):
        dx = object_2.pos_x - object_1.pos_x
        dy = object_2.pos_y - object_1.pos_y

        angle = math.degrees(math.atan2(dy, dx))

        if angle < 0:
            angle += 360
        return angle

    def handle_timer_increase(self):
        self.internal_timer += 1
        self.timer.get_time(self.internal_timer)
        if self.internal_timer >= self.timer_threshold:
            self.increase_spawnrate()
            self.timer_threshold += 30