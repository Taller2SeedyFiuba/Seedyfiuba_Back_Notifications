from src.schemas.notification import Notification, NotificationReport
from typing import List, Tuple
from exponent_server_sdk import (PushClient, PushMessage, PushTicket)
from exponent_server_sdk import (
    PushClient,
    PushMessage,
    PushServerError
)
from requests.exceptions import ConnectionError, HTTPError

def publishMessages(messages: List[PushMessage]) -> Tuple[List[str], List[str]]:

    succededTokens : List[str] = []
    failedTokens : List[str] = []
    responses : List[PushTicket] = []

    tokenStart = "ExponentPushToken[xxx]".find('[') + 1

    try:
        responses = PushClient().publish_multiple(messages)

    except PushServerError as exc:
        print(exc.errors)
        print(exc.response_data)
        failedTokens = [msg.to[tokenStart:-1] for msg in messages]
    except (ConnectionError, HTTPError) as exc:
        print(str(exc))
        failedTokens = [msg.to[tokenStart:-1] for msg in messages]

    for idx, response in enumerate(responses):
        try:
            print("Llega hasta aca")
            response.validate_response()
            print(f"Succeded token: {messages[idx].to[tokenStart:-1]}")
            succededTokens.append(messages[idx].to[tokenStart:-1])
        except Exception as exc:
            failedTokens.append(messages[idx].to[tokenStart:-1])
            print(str(exc))

    return (succededTokens, failedTokens)



def createMessages(data : Notification) -> List[PushMessage]:

    messages = []
    for token in data.tokens:
        messages.append(
            PushMessage(
                to=f'ExponentPushToken[{token}]',
                body=data.body,
                title=data.title,
                data=data.data))

    return messages

def sendNotification(noti : Notification) -> NotificationReport:
    """
    It will try to send a notification to all of the listed tokens
    """
    report : NotificationReport = NotificationReport(**noti.dict(), failed=[], succeded=[])
    sendLimit = 100 #Expo limit
    tokens = noti.tokens
    noti.tokens = tokens[:sendLimit]
    tokens = tokens[sendLimit:]

    while (len(noti.tokens) > 0):
        messages = createMessages(noti)
        (succededTokens, failedTokens) = publishMessages(messages)
        report.succeded = report.succeded + succededTokens
        report.failed = report.failed + failedTokens
        noti.tokens = tokens[:sendLimit]
        tokens = tokens[sendLimit:]

    return report
