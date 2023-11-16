import pygame
import random
import math


class Particle:
    def __init__(self, x, y, size, color, speed, lifespan):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.angle = random.uniform(0, 2 * 3.1415)
        self.lifespan = lifespan

    def move(self):
        self.x += self.speed * 0.5 * math.sin(self.angle)
        self.y += self.speed * 0.5 * math.cos(self.angle)
        self.lifespan -= 1


class ParticleSimulation:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Particle Simulation")

        self.particle_color = (200, 100, 50)
        self.particles = []

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 36)
        self.text_color = (0, 0, 0)

        self.run_simulation()

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.text_color)
        self.screen.blit(text_surface, (x, y))

    def start_simulation(self):
        particle_size = self.particle_size
        particle_speed = self.particle_speed
        particle_lifespan = 1000  # Set the initial lifespan for particles

        # Create a new particle with the current color and lifespan
        particle = Particle(400, 300, particle_size,
                            self.particle_color, particle_speed, particle_lifespan)

        # Append the new particle to the list
        self.particles.append(particle)

    def choose_color(self):
        color = pygame.Color(random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255))
        self.particle_color = color

    def run_simulation(self):
        self.particle_size = 5
        self.particle_speed = 2

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start_simulation()
                    elif event.key == pygame.K_LEFT:
                        self.particle_size = max(self.particle_size - 1, 1)
                    elif event.key == pygame.K_RIGHT:
                        self.particle_size = min(self.particle_size + 1, 20)
                    elif event.key == pygame.K_UP:
                        self.particle_speed = min(
                            self.particle_speed + 1, 10)
                    elif event.key == pygame.K_DOWN:
                        self.particle_speed = max(self.particle_speed - 1, 1)

            self.screen.fill((255, 255, 255))

            for particle in self.particles:
                particle.move()

                # Render particles based on lifespan
                alpha = int((particle.lifespan / 1000) * 255)
                particle_color = (*particle.color, alpha)
                pygame.draw.circle(self.screen, particle_color, (int(
                    particle.x), int(particle.y)), particle.size)

            # Remove particles with lifespan <= 0
            self.particles = [
                particle for particle in self.particles if particle.lifespan > 0]

            self.draw_text("Press Space to Start Simulation", 50, 20)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    ParticleSimulation()
