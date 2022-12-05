from imp import reload
from decouple import config
import uvicorn

if __name__ == "__main__":
    uvicorn.run('Main:app', host="0.0.0.0",
                port=int(config('PORT')), reload=True)
