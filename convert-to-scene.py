huefile = '/Users/april/projects/homeauto/homekit-backup/kitchenCleanup.json'

import json
import sys

import yaml


"""
scene:
  - name: Romantic
    entities:
      light.tv_back_light: "on"
      light.ceiling:
        state: "on"
        xy_color: [0.33, 0.66]
        brightness: 200
  - name: Movies
    entities:
      light.tv_back_light:
        state: "on"
        brightness: 125
      light.ceiling: off
      media_player.sony_bravia_tv:
        state: "on"
        source: HDMI 1
        state: "on"
    """

names = list()


def key_entity_for_light(light):
    entity_name = light['name'].lower().replace(' ', '_')
    entity_name = f"light.{entity_name}"

    entity_type = light['config']['archetype']
    entity_state = "on" if light['state']['on'] else "off"

    if entity_type == 'plug':
        return entity_name, entity_state

    return entity_name, {
        "state": entity_state,
        "brightness": light["state"]["bri"],
        "xy_color": light["state"]["xy"]
    }


def make_scene(scene_data):
    entities = dict(key_entity_for_light(light) for light in scene_data.values())
    return {"entities": entities}


with open(huefile) as json_file:
    scene_data = json.load(json_file)

    scene = make_scene(scene_data)

    yaml.dump(scene, sys.stdout)
