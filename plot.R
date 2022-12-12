library(ggplot2)
library(GeomMLBStadiums)
library(dplyr)

ggplot() + 
  geom_mlb_stadium(stadium_ids = "all_mlb", 
                   stadium_segments = "all") + 
  facet_wrap(~team) + 
  coord_fixed() + 
  theme_void()

ggsave('plot2.png') 
