from enum import Enum


class PrefKey(Enum):
    # the interface language
    LANG = 'lang'

    # prompt up the warning message-box before cancelling at adding a new example sentence
    MSG_BOX_CANCELLING_NEW_EXAMPLE = 'msg-box-cancelling-new-example'

    # prompt up the warning message-box before removing the added example sentence
    MSG_BOX_DELETING_ADDED_EXAMPLE = 'msg-box-removing-added-example'
