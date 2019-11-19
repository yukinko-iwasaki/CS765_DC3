import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from ipywidgets import interact
import pandas as pd
import nbinteract as nbi

class visualizer():
    def __init__(self,data):
        self.combined = data
    
    ## for word count
    def show_hist_word(self,Category = "fashion", wordcount = 10):
        c = self.combined[self.combined.category == Category]
        c = c[(c["word_count"] < wordcount + 100) & (c["word_count"] > wordcount - 100)].helpfulRate
        return c

    def show_interactive_word(self,normalized = True):
        if normalized:
            options = {
            "title" :"Histogram of helfulness rate with different word counts of reviews",
            'xlabel': "helpfulness",
            'xlim': (0, 1),
            'ylim': (0, 5),
            'bins': 10,
            "normalized":normalized,    
            }
        else:
            options = {
            "title" :"Histogram of helfulness rate with different word counts of reviews",
            'xlabel': "helpfulness",
            'xlim': (0, 1),
            'ylim': (0, 400),
            'bins': 10,
            "normalized":normalized,    
            }

        return nbi.hist(self.show_hist_word, Category = ["fashion", "movies and TV", "home and kitchen", "electronics"],  wordcount =(1, 1000, 50), options=options)

    ## for word count
    def show_hist_rate(self,Category = "fashion", stars = 1):
        c = self.combined[self.combined.category == Category]
        c = c[(c["overall"] ==  stars)].helpfulRate
        return c

    def show_interactive_rate(self,normalized = True):
        if normalized:
            options = {
            "title" :"Histogram of helfulness rate with rating of the review",
            'xlabel': "helpfulness",
            'xlim': (0, 1),
            'ylim': (0, 3),
            'bins': 10,
            "normalized":normalized,    
            }

        else:
            options = {
            "title" :"Histogram of helfulness rate with rating of the review",
            'xlabel': "helpfulness",
            'xlim': (0, 1),
            'ylim': (0, 3000),
            'bins': 10,
            "normalized":normalized,    
            }

        plt.savefig("test")
        return nbi.hist(self.show_hist_rate, Category = ["fashion", "movies and TV", "home and kitchen", "electronics"],  stars =(1, 5, 1), options=options)


    def show_image(self,category = "fashion", HelpfulRate = 0):
        i = int(HelpfulRate*10)
        img = mpimg.imread("images/" + category + str(i) +".PNG")
        plt.imshow(img)
        plt.axis("off")
        plt.show()

    def show_interaction_image(self):
        return self.interact(show_image, HelpfulRate = (0,1,0.1), category = ["fashion", "video", "home_kitchen", "movies_and_TV"])
    
    def show_interaction_hist_rate(self):
        return self.show_interactive_rate(normalized = True)
    
    def show_interaction_hist_count(self):
        return self.show_interactive_word(normalized = True)



