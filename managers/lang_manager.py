from enums.strs import Strs


class LangManager:
    # the supported languages
    supported_languages = ('繁體中文', '简体中文', 'English')

    # the dictionary to contain all registered nodes (components)
    __registered_dict = dict()

    # register a single node
    @staticmethod
    def register(node, str_enum_or_literal_str):
        if isinstance(str_enum_or_literal_str, Strs):
            LangManager.__registered_dict[node] = str_enum_or_literal_str
            LangManager.notify_registered(node)

    # register multiple nodes
    @staticmethod
    def register_all(*nodes_and_str_enums):
        for (node, str_enum) in nodes_and_str_enums:
            Strs.register(node, str_enum)

    # unregister a node
    @staticmethod
    def unregister(*nodes):
        for node in nodes:
            LangManager.__registered_dict.pop(node)

    # notify all registered nodes to be updated
    @staticmethod
    def notify_all_registered():
        for key, _ in LangManager.__registered_dict.items():
            print(key, type(key))
            LangManager.__update_registered(key)
        print()

    # notify a node to be updated
    @staticmethod
    def notify_registered(node):
        LangManager.__update_registered(node)

    # update a registered node w/ text-changing
    @staticmethod
    def __update_registered(node):
        if node in LangManager.__registered_dict:
            # set the literal string to the node
            node.set_string_by_str_enum_or_literal_str(LangManager.__registered_dict[node])
