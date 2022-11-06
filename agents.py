import mesa

def compute_sus(model):
  pass

class MosquitoAgent(mesa.Agent):

  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.status = 'S' # Susceptible

  def move(self):
    possible_steps = self.model.grid.get_neighbors(
      self.pos,
      radius=2.0,
      include_center=False
    )
    new_position = self.random.choice(possible_steps)
    self.model.grid.move_agent(self, new_position)

  def step(self):
    if self.status == 'I':
      pass
    self.move()

class HumanAgent(mesa.Agent):

  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.status = 'S' # Susceptible

  def infected(self):
    self.status = 'I' # Infected

  def move(self):
    possible_steps = self.model.grid.get_neighbors(
      self.pos,
      radius=2.0,
      include_center=False
    )
    new_position = self.random.choice(possible_steps)
    self.model.grid.move_agent(self, new_position)
  
  def step(self):
    if self.status == 'I':
      pass
    self.move()

class BirdAgent(mesa.Agent):

  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.status = 'S' # Susceptible

  def move(self):
    possible_steps = self.model.grid.get_neighbors(
      self.pos,
      radius=2.0,
      include_center=False
    )
    new_position = self.random.choice(possible_steps)
    self.model.grid.move_agent(self, new_position)

  def step(self):
    if self.status == 'I':
      pass
    self.move()