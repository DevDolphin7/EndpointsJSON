docker run -ti --rm \
   -e DISPLAY=$DISPLAY \
   -v /tmp/.X11-unix:/tmp/.X11-unix \
   --mount src="/home",target=/mnt,type=bind \
   devdolphin7/endpoints-json