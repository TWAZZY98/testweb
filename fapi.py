from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from celery_worker import save_user
import database

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def main_get():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Form</title>
    </head>
    <body>
        <h2>Enter User Data</h2>
        <form method="post" action="/">
            <label for="fn">First Name:</label>
            <input type="text" id="fn" name="fn" required><br><br>

            <label for="ln">Last Name:</label>
            <input type="text" id="ln" name="ln" required><br><br>

            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    """


@app.post("/")
async def main_post(
    fn: str = Form(...),
    ln: str = Form(...)
):
    print("hello")

    database.connect_to_db()
    database.input_name(fn, ln)
    database.discon()

    #save_user.delay(fn, ln)

    return {"message": "task queued"}