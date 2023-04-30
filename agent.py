import shutil, errno, os, loopgpt

AGENT_DESCRIPTION = (
    "the AI podcast producer of 'The Joe Rogan Experience'. Joe has podcasts planned for this week with Elon Musk, Jordan Peterson and David Goggins."
    + "Research recent events that happened in the last week and prepare 5 topics to discuss with each of them with very long descriptions, website links and targeted "
    + "questions for the host (Joe Rogan). Write all of your findings to neatly formatted files. There should be one file for each guest. Remember to only include "
    + "news from the last week."
)
AGENT_GOALS = [
    "Research events of the past week on the internet",
    "Write a podcast outline for 3 guests on 5 topics with descriptions, references and targeted questions for the host (Joe Rogan)",
    "Terminate the session once all 3 files are completed.",
]

WORKSPACE_PATH="/workspace"
WORKSPACE_OUTPUT_PATH="/app/workspace"
AGENT_MEMORY_FILE = ""
AGENT_NAME = ""
IS_AUTOMATED = False
CLEAR_WORKSPACE_ON_START = False

def setup_environment():
  global AGENT_MEMORY_FILE
  global IS_AUTOMATED
  global AGENT_NAME
  global CLEAR_WORKSPACE_ON_START
  AGENT_MEMORY_FILE = os.getenv('AGENT_MEMORY_FILE', 'HAL.json')
  IS_AUTOMATED = os.getenv('IS_AUTOMATED', 'False').lower() in ('true', '1', 't')
  AGENT_NAME = os.getenv('AGENT_NAME', 'HAL')
  CLEAR_WORKSPACE_ON_START = os.getenv('CLEAR_WORKSPACE_ON_START', 'False').lower() in ('true', '1', 't')
  
def clean_workspace():
  if os.path.exists(WORKSPACE_OUTPUT_PATH):
    shutil.rmtree(WORKSPACE_OUTPUT_PATH)

def ensure_workspace_exists():
  if not os.path.exists(WORKSPACE_PATH):
      os.makedirs(WORKSPACE_PATH)

def setup_path():
  if CLEAR_WORKSPACE_ON_START:
    clean_workspace()
  else:
    restore_workspace()
  ensure_workspace_exists()
  os.chdir(WORKSPACE_PATH)

def copyanything(src, dst):
    try:
      shutil.copytree(src, dst)
    except OSError as exc:
      if exc.errno in (errno.ENOTDIR, errno.EINVAL):
        shutil.copy(src, dst)
      else: raise

def save_workspace():
  clean_workspace()
  copyanything(WORKSPACE_PATH, WORKSPACE_OUTPUT_PATH)

def restore_workspace():
  if os.path.exists(WORKSPACE_OUTPUT_PATH):
    copyanything(WORKSPACE_OUTPUT_PATH, WORKSPACE_PATH)

def run_agent():
  try:
    agent = loopgpt.Agent()
    if os.path.exists(AGENT_MEMORY_FILE):
      agent.load(AGENT_MEMORY_FILE)
    agent.name = AGENT_NAME
    agent.description = AGENT_DESCRIPTION
    agent.goals = AGENT_GOALS
    agent.cli(continuous=IS_AUTOMATED)
    agent.save(AGENT_MEMORY_FILE)
  finally:
    save_workspace()

setup_environment()
setup_path()
run_agent()