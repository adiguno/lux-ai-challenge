import math, sys
from lux.game import Game
from lux.game_map import Cell, RESOURCE_TYPES
from lux.constants import Constants
from lux.game_constants import GAME_CONSTANTS
from lux import annotate

DIRECTIONS = Constants.DIRECTIONS
game_state = None


def agent(observation, configuration):
    global game_state

    ### Do not edit ###
    if observation["step"] == 0:
        game_state = Game()
        game_state._initialize(observation["updates"])
        game_state._update(observation["updates"][2:])
        game_state.id = observation.player
    else:
        game_state._update(observation["updates"])
    
    actions = []

    ### AI Code goes down here! ### 
    player = game_state.players[observation.player]
    # opponent = game_state.players[(observation.player + 1) % 2]
    width, height = game_state.map.width, game_state.map.height
    resource_tiles = get_resource_tiles(width, height)

    # we iterate over all our units and do something with them
    for unit in player.units:
        if is_movable_worker(unit):
            if has_cargo_space(unit):
                closest_dist = math.inf
                closest_resource_tile = None
                for resource_tile in resource_tiles:
                    if is_wood_tile(resource_tile):
                    # if resource_tile.resource.type == Constants.RESOURCE_TYPES.COAL and not player.researched_coal(): continue
                        distance_to_worker = resource_tile.pos.distance_to(unit.pos)
                        closest_resource_tile = update_closest_tile(closest_dist, resource_tile, distance_to_worker)
                if closest_resource_tile is not None:
                    actions.append(unit.move(unit.pos.direction_to(closest_resource_tile.pos)))
            else:
                # circle if worker is full
                # actions.append(annotate.circle(unit.pos.x, unit.pos.y))

                # if unit is a worker and there is no cargo space left, and we have cities, lets return to them
                if len(player.cities) > 0:
                    closest_dist = math.inf
                    closest_city_tile = None
                    for k, city in player.cities.items():
                        for city_tile in city.citytiles:
                            distance_to_worker = city_tile.pos.distance_to(unit.pos)
                            if distance_to_worker < closest_dist:
                                closest_dist = distance_to_worker
                                closest_city_tile = city_tile
                    if closest_city_tile is not None:
                        move_dir = unit.pos.direction_to(closest_city_tile.pos)
                        actions.append(unit.move(move_dir))

    # you can add debug annotations using the functions in the annotate object
    # actions.append(annotate.circle(0, 0))
    
    return actions

def get_resource_tiles(width, height):
    resource_tiles: list[Cell] = []
    for y in range(height):
        for x in range(width):
            cell = game_state.map.get_cell(x, y)
            if cell.has_resource():
                resource_tiles.append(cell)
    return resource_tiles

def update_closest_tile(closest_dist, resource_tile, distanceToWorker):
    if distanceToWorker < closest_dist:
        closest_dist = distanceToWorker
        closest_resource_tile = resource_tile
    return closest_resource_tile

def is_wood_tile(resource_tile):
    return resource_tile.resource.type == Constants.RESOURCE_TYPES.WOOD


def is_movable_worker(unit):
    return unit.is_worker() and unit.can_act()

def has_cargo_space(unit):
    return unit.get_cargo_space_left() > 0