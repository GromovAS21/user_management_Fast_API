from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogMiddleware(BaseHTTPMiddleware):
    """Логирование запросов к серверу"""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        logging.info(f"Запрос: {request.method} {request.url}")
        response = await call_next(request)
        logging.info(f"Ответ: {response.status_code}")
        return response

