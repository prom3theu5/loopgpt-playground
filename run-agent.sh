CONTAINER_NAME=loop_gpt
IMAGE_NAME=loopgpt
SOURCE_DIR=$(pwd)

clear
podman run \
    --name $CONTAINER_NAME -it --rm \
    -v $SOURCE_DIR:/app \
    --env-file .env \
    $IMAGE_NAME