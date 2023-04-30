CONTAINER_NAME=loop_gpt
IMAGE_NAME=loopgpt
SOURCE_DIR=$(pwd)
ENTRYPOINT=loopgpt

clear
podman run \
    --name $CONTAINER_NAME -it --rm \
    -v $SOURCE_DIR:/app \
    --env-file .env \
    --entrypoint $ENTRYPOINT \
    $IMAGE_NAME \
    run