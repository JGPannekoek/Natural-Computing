library(tidyverse)

# https://www.kaggle.com/datasets/jacekpardyak/ns-nederlandse-spoorwegen?resource=download&select=nodes.csv
stations <- read_csv("nodes.csv")

# https://wikikids.nl/Lijst_van_grote_Nederlandse_steden, edited
cities <- read_csv("cities.csv")

# Too many stations in the west side of the country, try to balance
to_remove <- c('Schiedam Centrum', 'Rijswijk', 'Capelle Schollevaar', 'Heerhugowaard', 'Zaandam', 'Hoofddorp', 'Roosendaal', 'Oss', 'Delft', 'Zoetermeer', 'Alphen a/d Rijn', 'Purmerend', 'Veenendaal-De Klomp')

# Add extremes
cities <- cities %>%
  add_row(city="Den Helder", main_station="Den Helder") %>% 
  add_row(city="Winterswijk", main_station="Winterswijk")

stations_of_interest <- stations %>% 
  filter(!station %in% to_remove) %>% 
  inner_join(cities, join_by(station == main_station)) %>% 
  select(city, station, code=name, lat, lng, province, num_inhabitants)

write_csv(stations_of_interest,"stations_of_interest.csv")
