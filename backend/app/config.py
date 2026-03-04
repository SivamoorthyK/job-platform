import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
HF_TOKEN     = os.getenv("HF_TOKEN")

# Supabase client — use this everywhere in the app
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)