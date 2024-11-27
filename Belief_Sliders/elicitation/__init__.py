from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'beta_distribution'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    mean = models.FloatField()
    variance = models.FloatField()

class Sliders(Page):
    form_model = 'player'
    form_fields = ['mean', 'variance']

    def vars_for_template(self):
        min_value = 0  # Replace with your actual min value
        max_value = 10  # Replace with your actual max value
        initial_mean = (min_value + max_value) / 2
        return {
            'min': min_value,
            'max': max_value,
            'initial_mean': initial_mean
        }

class Results(Page):
    pass

page_sequence = [Sliders, Results]