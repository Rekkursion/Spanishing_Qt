from enum import Enum


class PrefKey(Enum):
    # the interface language
    LANG = 'lang'

    # prompt up the make-sure message-box before cancelling at adding a new example sentence
    MSG_BOX_CANCELLING_NEW_EXAMPLE = 'msg-box-cancelling-new-example'
