from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'beta_distribution'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    MIN_ALLOWED = -100  # Add reasonable bounds for inflation
    MAX_ALLOWED = 200

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    min_inflation = models.FloatField(
        label='',  # Empty label
        label_tag=None,  # This prevents label from being rendered
        min=C.MIN_ALLOWED,
        max=C.MAX_ALLOWED,
    )
    max_inflation = models.FloatField(
        label='',  # Empty label
        label_tag=None,  # This prevents label from being rendered
        min=C.MIN_ALLOWED,
        max=C.MAX_ALLOWED,
    )
    mean = models.FloatField()
    variance = models.FloatField()


# PAGES

class MinMaxInput(Page):
    form_model = 'player'
    form_fields = ['min_inflation', 'max_inflation']
    
    def error_message(self, values):
        if values['min_inflation'] >= values['max_inflation']:
            return 'The minimum value must be less than the maximum value'

class Sliders(Page):
    form_model = 'player'
    form_fields = ['mean', 'variance']

    def vars_for_template(self):
        return {
            'min': self.min_inflation,
            'max': self.max_inflation,
            'initial_mean': (self.min_inflation + self.max_inflation) / 2
        }

class Results(Page):
    pass

page_sequence = [MinMaxInput, Sliders, Results]