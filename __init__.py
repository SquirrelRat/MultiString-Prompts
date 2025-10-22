from .multi_prompt_node import NODE_CLASS_MAPPINGS as string_node_mappings
from .multi_prompt_node import NODE_DISPLAY_NAME_MAPPINGS as string_name_mappings

from .multi_prompt_encode_node import NODE_CLASS_MAPPINGS as encode_node_mappings
from .multi_prompt_encode_node import NODE_DISPLAY_NAME_MAPPINGS as encode_name_mappings

NODE_CLASS_MAPPINGS = {**string_node_mappings, **encode_node_mappings}
NODE_DISPLAY_NAME_MAPPINGS = {**string_name_mappings, **encode_name_mappings}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']