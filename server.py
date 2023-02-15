import mesa
from mesa.visualization.UserParam import Slider
from agents import *
from model import CityModel
from visualization import SimpleCanvas


def agent_draw(agent):
  portrayal = {
    "Filled": "true",
    "Shape": "circle",
  }
  if isinstance(agent, MosquitoAgent):
    portrayal["Color"] = "red"
    portrayal["Layer"] = 0
    portrayal["r"] = 4
  elif isinstance(agent, BirdAgent):
    portrayal["Color"] = "black"
    portrayal["Layer"] = 1
    portrayal["r"] = 7
  else:
    portrayal["Color"] = "blue"
    portrayal["Layer"] = 2
    portrayal["r"] = 10

  
  if agent.status == 'I':
    portrayal["Color"] = "yellow"
  elif agent.status == 'R':
    portrayal["Color"] = "grey"
  return portrayal

model_canvas = SimpleCanvas(agent_draw, 1000, 1000)

n_mosq_slider = Slider("Number of Mosquitos", value=100, min_value=2, max_value=200, step=1)
n_bird_slider = Slider("Number of Ravens", value=100, min_value=2, max_value=200, step=1)
n_hum_slider = Slider("Number of People", value=100, min_value=2, max_value=200, step=1)
repro_num_slider = Slider("Transmission Probability", value=50, min_value=0, max_value=100, step=1)
recov_per_slider = Slider("Recovery Period", value=7, min_value=0, max_value=28, step=1)
n_init_inf_mosq_slider = Slider("Initial Infected Mosquito Count", value=1, min_value=0, max_value=200, step=1)

model_param = {"N_mosq": n_mosq_slider, 
               "N_bird": n_bird_slider, 
               "N_hum": n_hum_slider, 
               "width": 20, 
               "height":20,
               "repro_num": repro_num_slider,
               "recov_per": recov_per_slider,
               "N_init_inf_mosq":n_init_inf_mosq_slider,
              }

chart = mesa.visualization.ChartModule([{"Label": "SIR Graph",
            "Color": "Black"}],
          data_collector_name='data_collector')

server = mesa.visualization.ModularServer(
    CityModel, [model_canvas, chart], "City Model", model_param
)