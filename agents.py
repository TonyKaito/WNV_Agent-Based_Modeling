import mesa
import numpy as np

def compute_sus(model):
  pass

class MosquitoAgent(mesa.Agent):

  def __init__(self, unique_id, model, repro_num, recov_per):
    super().__init__(unique_id, model)
    self.repro_num = repro_num
    self.recov_per = recov_per
    self.status = 'S' # Susceptible
    self.infect_dur = 0

  def move(self):
    new_position = self.pos + np.random.random(2) * 2 - 1
    self.model.space.move_agent(self, new_position)

  def bite(self):
    
    neighbors = self.model.space.get_neighbors(self.pos, 0.5, False)
    for neighbor in neighbors:
      if self.status == 'R':
        break
      
      # If it is infected
      if self.status == 'I' and neighbor.status != 'R' and not isinstance(neighbor, MosquitoAgent):
        tran_prob = np.random.random()
        if tran_prob < self.repro_num:
          neighbor.infected()
        pass

      # Mosquito becomes infected
      if neighbor.status == 'I' and isinstance(neighbor, BirdAgent):
        tran_prob = np.random.random()
        if tran_prob < self.repro_num:
          self.status = 'I'
        pass

  def step(self):
    self.bite()
    if self.status == 'I':
      self.infect_dur += 1
    if self.infect_dur == self.recov_per:
      self.status = 'R'
    self.move()

class HumanAgent(mesa.Agent):

  def __init__(self, unique_id, model, repro_num, recov_per):
    super().__init__(unique_id, model)
    self.repro_num = repro_num
    self.recov_per = recov_per
    self.status = 'S' # Susceptible
    self.infect_dur = 0

  def infected(self):
    self.status = 'I' # Infected

  def move(self):
    new_position = self.pos + np.random.random(2) * 2 - 1
    self.model.space.move_agent(self, new_position)
  
  def step(self):
    if self.status == 'I':
      self.infect_dur += 1
    if self.infect_dur == self.recov_per:
      self.status = 'R'
    self.move()

class BirdAgent(mesa.Agent):

  def __init__(self, unique_id, model, repro_num, recov_per):
    super().__init__(unique_id, model)
    self.repro_num = repro_num
    self.recov_per = recov_per
    self.status = 'S' # Susceptible
    self.infect_dur = 0

  def infected(self):
    self.status = 'I' # Infected
  
  def move(self):
    new_position = self.pos + np.random.random(2) * 2 - 1
    self.model.space.move_agent(self, new_position)

  def step(self):
    if self.status == 'I':
      self.infect_dur += 1
    if self.infect_dur == self.recov_per:
      self.status = 'R'
    self.move()