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
      

class CityModel(mesa.Model):
  """A model with Multiple Cities"""
  def __init__(self, N_mosq, N_hum, N_bird, width, height):
    self.num_mosq = N_mosq
    self.num_hum = N_hum
    self.num_bird = N_bird
    self.grid = mesa.space.MultiGrid(width, height, False) # False -> not toridial
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
    
  