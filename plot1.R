library(ggplot2)
devtools::install_github("bdilday/GeomMLBStadiums")
library(GeomMLBStadiums)
library(dplyr)

ggplot() + 
  geom_mlb_stadium(stadium_ids = "all_mlb", 
                   stadium_segments = "all") + 
  facet_wrap(~team) + 
  coord_fixed() + 
  theme_void()

ggsave('plot.png') 
