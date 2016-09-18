#Setup Logging
import logging
log = logging.getLogger(__name__)

#Python modules

#Local modules
from ..alarm import Alarm
# from ..utils import * # This is a basic alarm. No utils needed.
#Bot Implementation included
import requests
from json import dumps as jsondumps
#Emote List

class Groupme_Alarm(Alarm):
  _defaults = {
    "pokemon":{},
    "lures":{},
    "gyms":{}    
  }
  
  #Gather settings and create alarm
  def __init__(self, settings):
    self.bot_id = settings.get('bot_id')
    self.group_id = settings.get('group_id')
    log.info('bot init')
  
  #(Re)establishes Service connection
  def connect():
    print('groupme bot needs no connect')
  
  #Set the appropriate settings for each alert
  def set_alert(self, settings):
    raise NotImplementedError("This is an abstract method.")
  
  #Send Alert to the Service
  def send_alert(self, alert_settings, info):
    print('no send_alert')
  
  #Trigger an alert based on Pokemon info
  def pokemon_alert(self, pokemon_info):
    data = {'bot_id'  :self.bot_id,
            'group_id':self.group_id,
            'text'    :"".join([pokemon_info['pkmn'], ' until ', pokemon_info['24h_time']]),
            'attachments':
            [
              {'type':'location',
               'lng' :pokemon_info['lng'],
               'lat' :pokemon_info['lat'],
               'name':"".join([pokemon_info['pkmn'], ' until ', pokemon_info['24h_time']])
              }
            ]
           }
    r = requests.post('https://api.groupme.com/v3/bots/post', jsondumps(data))
    log.info(r)
  #Trigger an alert based on PokeLure info
  def pokestop_alert(self, pokelure_info):
    data = {'bot_id'  :self.bot_id,
            'group_id':self.group_id,
            'text'    :"".join(['Pokestop lured until ', pokelure_info['24h_time']]),
            'attachments':
            [
              {'type':'location',
               'lng' :pokelure_info['lng'],
               'lat' :pokelure_info['lat'],
               'name':''.join(['(NotYetImplementedPokestopName)', ' lured until ', pokelure_info['24h_time']])
              }
            ]
           }
    r = requests.post('https://api.groupme.com/v3/bots/post', jsondumps(data))
    log.info(r)
  #Trigger an alert based on PokeGym info
  def gym_alert(self, pokegym_info):
    log.warning('gym alert not yet implemented')
    
