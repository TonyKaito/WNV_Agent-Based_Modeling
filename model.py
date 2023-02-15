import mesa
from agents import *

class CityModel(mesa.Model):
  """A model with Multiple Cities"""
  def __init__(self, N_mosq, N_hum, N_bird, width, height, repro_num, recov_per, N_init_inf_mosq):
    self.num_mosq = N_mosq
    self.num_hum = N_hum
    self.num_bird = N_bird
    self.repro_num = repro_num
    self.recov_per = recov_per
    self.num_init_inf_mosq = N_init_inf_mosq
    self.space = mesa.space.ContinuousSpace(width, height, True) # False -> not toridial
    self.schedule = mesa.time.RandomActivation(self)
    self.make_agents()
    self.running = True

  def make_agents(self):
    # Amount of Cities, Human Remain Within the Cities
    for i in range(0, self.num_hum):
      a = HumanAgent(i, self, self.repro_num, self.recov_per)

      x = self.random.random() * self.space.width
      y = self.random.random() * self.space.height
      self.space.place_agent(a, (x, y))
      self.schedule.add(a)

    #
    for j in range(500, self.num_mosq+500):
      a = MosquitoAgent(j, self, self.repro_num, self.recov_per)
      if self.num_init_inf_mosq > 0:
        a.status = 'I'
        self.num_init_inf_mosq -= 1

      x = self.random.random() * self.space.width
      y = self.random.random() * self.space.height
      self.space.place_agent(a, (x, y))
      self.schedule.add(a)
    

    for k in range(1000, self.num_bird+1000):
      a = BirdAgent(k, self, self.repro_num, self.recov_per)

      x = self.random.random() * self.space.width
      y = self.random.random() * self.space.height
      self.space.place_agent(a, (x, y))
      self.schedule.add(a)

    self.data_collector = mesa.DataCollector(
      model_reporters={},
      agent_reporters={"status":"status"}
    )


  def step(self):
    self.data_collector.collect(self)
    self.schedule.step()
    
  