import mesa
from mesa.visualization.UserParam import Slider
from model import *

def agent_portrayal(agent):
  portrayal = {
    "Filled": "true",
    "Shape": "circle",
    "r": 0.5,
  }
  if isinstance(agent, MosquitoAgent):
    portrayal["Color"] = "red"
    portrayal["Layer"] = 0
    portrayal["r"] = 0.3
  elif isinstance(agent, BirdAgent):
    portrayal["Color"] = "grey"
    portrayal["Layer"] = 1
    portrayal["r"] = 0.5
  else:
    portrayal["Color"] = "blue"
    portrayal["Layer"] = 2
    portrayal["r"] = 0.8
  return portrayal

n_mosq_slider = Slider("Number of Mosquitos", value=100, min_value=2, max_value=200, step=1)
n_bird_slider = Slider("Number of Ravens", value=100, min_value=2, max_value=200, step=1)
n_hum_slider = Slider("Number of People", value=100, min_value=2, max_value=200, step=1)

grid = mesa.visualization.CanvasGrid(agent_portrayal, 20, 20, 1000, 1000)
# chart = mesa.visualization.ChartModule([{"Label": "Gini", "Color": "Black"}], data_collector_name='datacollector')
server = mesa.visualization.ModularServer(
  CityModel, [grid], "City Model", {"N_mosq": n_mosq_slider, "N_bird": n_bird_slider, "N_hum": n_hum_slider , "width": 20, "height":20}
)
server.port = 8521
server.launch()