from typing import Any

from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.config import templates
from app.routers import deps
from app import schema
from app.security import superuser_required
from app.models import UserPayload
from app.api import userfunc


router = APIRouter(prefix='/user-activity')


@router.get('/')
@superuser_required
async def list_user_exam(
    request: Request,
    current_user: UserPayload = Depends(deps.get_current_user)
) -> Any:
    users = await userfunc.get_all_user()
    return templates.TemplateResponse(
        'manager/user-statusboard.jinja2', {
            'request': request,
            'current_user': current_user,
            'users': users
        }
    )
