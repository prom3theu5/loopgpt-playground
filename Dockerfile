FROM mcr.microsoft.com/dotnet/sdk:7.0 as dotnet
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    chromium-driver firefox-esr \
    ca-certificates

RUN apt-get install -y curl jq wget git nano

ENV PIP_NO_CACHE_DIR=yes \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH=$PATH:/usr/share/dotnet

COPY --from=dotnet /usr/share/dotnet /usr/share/dotnet

RUN dotnet help

ENV PATH="$PATH:/root/.local/bin"
RUN pip install loopgpt
WORKDIR /app
ENTRYPOINT ["python", "agent.py"]