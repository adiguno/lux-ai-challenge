# Goal: Maximize City Tiles

    - if tie, most units on board wins
        - if tie again, its actually tie

# limits

- 360 turns
- 3 seconds of decision making per turn
  - max, excess 60 seconds

# Objects

    - Resources
        - wood
          - regrow by 2.5%
          - regrow if < 500
          - no regrow if depleted
        - coal
        - uranium
    - Units
        - workers
        - carts
    - CityTiles
    - Road

# Map

- horizaontally / verticall reflected

- Sizes:

  - 12x12
  - 16x16
  - 24x24
  - 32x32

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0,0 | 1,0 |     |     |     |     |     |     | x,0 |
| 0,1 |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     | N   |     |     |     |     |
|     |     |     | W-  | +   | -E  |     |     |     |
|     |     |     |     | S   |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
| 0,y |     |     |     |     |     |     |     | x,y |
