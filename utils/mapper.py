from typing import Any, List
from pydantic import BaseModel


class Query(BaseModel):
    sender: str
    message: str
    isGroup: bool
    groupParticipant: str
    ruleId: int
    isTestMessage: bool


class JsonRequest(BaseModel):
    appPackageName: str
    messengerPackageName: str
    query: Query


class Reply(BaseModel):
    message: str


class Response(BaseModel):
    replies: List[Reply]


class JsonResponse:
    def __init__(self, replies: list | str) -> None:
        self.replies = self.validate_replies(replies)

    def json(self, *args: Any, **kwds: Any) -> Any:
        return self.replies.model_dump_json()

    def validate_replies(self, replies) -> Response:
        if isinstance(replies, str):
            replies = [replies]
        elif isinstance(replies, list):
            replies = replies
        elif isinstance(replies, tuple):
            replies = list(replies)
        return Response(replies=[Reply(message=i) for i in replies])


if __name__ == "__main__":
    print(JsonResponse("Hello World").__call__())
