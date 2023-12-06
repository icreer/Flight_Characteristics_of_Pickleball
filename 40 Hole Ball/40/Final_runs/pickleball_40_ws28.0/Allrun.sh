
#!/bin/sh

runApplication surfaceFeatureExtract

runApplication blockMesh

runApplication snappyHexMesh -overwrite

runApplication simpleFoam