class MultiStringPrompts:
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "enable_prefix": (["true", "false"], {"default": "true"}),
                "enable_suffix": (["true", "false"], {"default": "true"}),
                "prefix": ("STRING", {"default": ""}),
                "suffix": ("STRING", {"default": ""}),
                "multi_prompt_1": ("STRING", {"multiline": True, "default": ""}),
                "multi_prompt_2": ("STRING", {"multiline": True, "default": ""}),
                "multi_prompt_3": ("STRING", {"multiline": True, "default": ""}),
                "multi_prompt_4": ("STRING", {"multiline": True, "default": ""}),
                "multi_prompt_5": ("STRING", {"multiline": True, "default": ""}),
            }
        }
        
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING",)
    RETURN_NAMES = (
        "prompt_1", 
        "prompt_2", 
        "prompt_3", 
        "prompt_4", 
        "prompt_5", 
        "prompt_list",
    )
    OUTPUT_IS_LIST = (False, False, False, False, False, True,)
    FUNCTION = "process_prompts"
    CATEGORY = "MultiString Prompts" 

    def process_prompts(self, prefix, suffix, enable_prefix, enable_suffix, 
                          multi_prompt_1, multi_prompt_2, multi_prompt_3, 
                          multi_prompt_4, multi_prompt_5):
        
        def _process(prompt_text, prefix, suffix, enable_prefix, enable_suffix):
            
            prompt_text = prompt_text.strip()
            
            if not prompt_text:
                return ""

            is_prefix_enabled = (enable_prefix == "true")
            is_suffix_enabled = (enable_suffix == "true")

            prefix_text = prefix.strip() if is_prefix_enabled else ""
            suffix_text = suffix.strip() if is_suffix_enabled else ""

            parts = []
            if prefix_text:
                parts.append(prefix_text)
            
            parts.append(prompt_text)
            
            if suffix_text:
                parts.append(suffix_text)
            
            return ",".join(parts)

        prompts_in = [
            multi_prompt_1, 
            multi_prompt_2, 
            multi_prompt_3, 
            multi_prompt_4, 
            multi_prompt_5
        ]

        prompt_list_out = [
            _process(p, prefix, suffix, enable_prefix, enable_suffix) for p in prompts_in
        ]

        return (
            prompt_list_out[0],
            prompt_list_out[1],
            prompt_list_out[2],
            prompt_list_out[3],
            prompt_list_out[4],
            prompt_list_out,
        )

NODE_CLASS_MAPPINGS = {
    "MultiStringPrompts": MultiStringPrompts
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MultiStringPrompts": "MultiString Prompts"
}