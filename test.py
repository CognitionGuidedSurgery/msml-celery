__author__ = 'weigl'

import msmlcelery as C

## Test date:
r = C.date.delay()
print r.get()

## Test Tetgen:
bunny = C.read_content("../msml/examples/BunnyExample/Bunny6000Surface.vtk")
r = C.TetgenCreateVolumeMesh.delay(surfaceMesh=bunny,
                                   targetMeshFilename="surface.vtk",
                                   preserveBoundary=True)
vol = r.get()
print vol['mesh']