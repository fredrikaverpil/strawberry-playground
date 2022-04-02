import dotenv
import uvicorn

if __name__ == "__main__":
    dotenv.load_dotenv("env/.env.prod")
    uvicorn.run("sbplay.app:create_app", factory=True, reload=True)
