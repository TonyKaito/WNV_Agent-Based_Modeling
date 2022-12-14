# West Nile Virus Agent-Based Modeling

## Introduction

In an ever-changing world, where everything is in constant motion and there are too many variables to mathematically know what precisely is going on, we then rely on numerical and computational simulations to give a concrete and visual representation of a process. As such, we will simulate the spread of the West Nile Virus using Agent-Based Modelling. However, even this task in itself is difficult, as knowing the correct context to a specific phenomenon is very tedious to know precisely. As our main task is to show temperature, humidity, and precipitation affects the spread of the West Nile Virus, we must make some simplifications:
1.	The Birds have no migratory behavior and move at random.
  The main hosts of the West Nile Virus are Corvidae, and Corvidae are shown to have no specific migratory behavior. However, they are shown to wander around, especially when temperatures get extremely cold [100]. As such, Corvidae do slightly tend to locate in cities as the temperatures are slightly warmer due to a phenomenon known as Urban Heat Islands [101]. We will not be considering this when it comes to modelling. (Especially since most Corvidae can already survive very harsh arctic weather.)
2.	Mosquitoes slowly expand towards areas that become more habitable to them. 
  The main effects we will consider when it comes to what is more “habitable” will only rely on three factors, being temperature, humidity, and precipitation. Features such as elevation levels (i.e., “mosquito line”) are either still debated or disregarded when it comes to how it affects Mosquito Population Rates [102], and as such will not be considered. Some intervention strategies relating to the eradication of mosquitoes (i.e., cleaner environment) will be considered later. We will also assume that a city is uniformly susceptible and vulnerable, even if mosquito population rates do vary within cities, depending on factors such as average neighborhood income levels [103]. 
3.	All humans remain within their respective cities. 
  One of the key features about West Nile Virus is that it does not depend specifically on humans, due to its vector-borne nature. The main circulation method of West Nile seems to follow a mosquito-bird-mosquito pattern [104], being completely independent of humans. As such, we will not be considering ideas such as gathering places (i.e., a local grocery store, school, etc.) or immigration rates (i.e., driving/flying between cities). Rather, humans will remain within their cities, and will randomly float within it.

## Methodology

The specific methodology we will use to measure newly susceptible areas is to initialize a space of 9 different cities. Each of them will contain a variable amount of people living within it. Since we have noted that human-to-human interaction is not a factor, we do not care about specific habits of the movements of the people, and they will be wandering around the city borders aimlessly. As for the mosquitoes, we will assume that they start within a variable region of the plane, whether it be within the lower-left most city, or the right-half of the map. As for the birds, they will initially be starting out in random locations and will move around randomly. In this case, a bird within the model could represent a singular bird, or it could represent a flock of birds moving together. 
We will then analyze how the infection spreads. We will start with the condition that a single mosquito has the virus. If a mosquito is within a certain radius of another agent, the mosquito will “feed” upon that agent. If a healthy mosquito “feeds” into a human (whether healthy or infected), nothing will occur; however, if a healthy mosquito “feeds” into an infectious bird, it will have a probability of becoming infectious itself. Likewise, if an infectious mosquito “feeds” into an agent, whether human or bird, the bird then has a likely chance of becoming infected (unless already infected). There will be no direct interactions between humans and the birds.
The agent will continue to be in the infected state until after their period has passed, and then they enter the removed category. Once the agent has entered the recover category, they will gain life-long immunity and continue on with their life.

## Citation

[100] https://www.tandfonline.com/doi/pdf/10.1080/00063657109476300
[101] https://keep.lib.asu.edu/_flysystem/fedora/2022-05/1-s2.0-s1001074208600194-main_0.pdf
[102] http://www.lomborg-errors.dk/MalariaKenya.htm
[103] https://www.caryinstitute.org/news-insights/podcast/poor-neighborhoods-and-mosquitoes
[104] https://www.cdc.gov/westnile/transmission/index.html

