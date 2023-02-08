import environs

env = environs.Env()
env.read_env()

API_TOKEN = env.str("API_TOKEN")

