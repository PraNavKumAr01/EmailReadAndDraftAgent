from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.graph import WorkFlow

app = FastAPI()

class EmailInput(BaseModel):
    emailID: str

@app.post("/invoke_workflow/")
def invoke_workflow(email_input: EmailInput):
    try:
        mail = email_input.emailID
        workflow_app = WorkFlow(emailID=mail).app
        workflow_app.invoke({})

        # Read the contents of output.txt
        with open('output.txt', 'r') as file:
            output_text = file.read()

        return {"message": "Workflow invoked successfully!", "output_text": output_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to invoke workflow: {str(e)}")