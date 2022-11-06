import mesa
from agents import *

class CityModel(mesa.Model):
  """A model with Multiple Cities"""
  def __init__(self, N_mosq, N_hum, N_bird, width, height):
    self.num_mosq = N_mosq
    self.num_hum = N_hum
    self.num_bird = N_bird
    self.grid = mesa.space.ContinuousSpace(width, height, False) # False -> not toridial
    self.schedule = mesa.time.RandomActivation(self)
    self.running = True

    # Amount of Cities, Human Remain Within the Cities
    for i in range(0, N_hum):
      a = HumanAgent(i, self)
      self.schedule.add(a)

      x = self.random.randrange(self.grid.width)
      y = self.random.randrange(self.grid.height)
      self.grid.place_agent(a, (x, y))

    #
    for j in range(0, N_mosq):
      a = MosquitoAgent(j, self)

      x = self.random.randrange(self.grid.width)
      y = self.random.randrange(self.grid.height)
      self.grid.place_agent(a, (x, y))

    for k in range(0, N_bird):
      a = BirdAgent(k, self)

      x = self.random.randrange(self.grid.width)
      y = self.random.randrange(self.grid.height)
      self.grid.place_agent(a, (x, y))

    self.data_collector = mesa.DataCollector(
      model_reporters={},
      agent_reporters={}
    )


    def step(self):
      self.data_collector.collect(self)
      self.schedule.step()
    
  