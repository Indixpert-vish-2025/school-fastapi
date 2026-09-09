from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.routers.student_routers import router as student_router
from app.routers.teacher_routers import router as teacher_router
from app.routers.course_routers import router as course_router
from app.routers.user_routers import router as user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(course_router)
app.include_router(user_router)