"""
Basic terrain generation made to test out EmptyRegion and related
Needs the `opensimplex` package to work

Generated terrain is 128x128 blocks and in the North-West corner
"""
import _path
import anvil

region = anvil.EmptyRegion(0, 0)
air = anvil.Block('minecraft', 'air')
xoff = region.x * 0
zoff = region.z * 0
for z in range(512):
    for x in range(512):
        region.set_block(air, x, 2, z)

save = region.save('r.0.0.mca')

