# Experiments with Utilises LoopGPT

see LoopGPT here: https://github.com/farizrahman4u/loopgpt

## Usage

1. Clone the repo

```bash
git clone https://github.com/prom3theu5/loopgpt
```

2. Copy the .env.template file to '.env' 

```bash
cp .env.template .env
```

3. Add your OpenAI api key to .env to set the env variable 'OPENAI_API_KEY'

4. Ensure shell scripts are executable

```bash
chmod a+x ./*.sh
```

5. Build the container (Requires podman)

```bash
./build.sh
```

You can now choose to either run the cli or the agent.
The agent lets you configure goals and description to run, and allows workspace to be saved etc.
Edit `agent.py` to set the description and goals.

Start with agent with `./run-agent.sh` or run the pure cli version using `./run-cli.sh`

# Warning

The only directory the agents have access to is the current git directory. This is massively better than running it freely on your machine, considering it can generate and execute code at will!
