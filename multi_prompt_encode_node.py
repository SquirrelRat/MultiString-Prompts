import torch

class MultiStringPromptsEncode:
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "clip": ("CLIP", ),
                "enable_prefix": (["true", "false"], {"default": "true"}),
                "enable_suffix": (["true", "false"], {"default": "true"}),
                "prefix": ("STRING", {"default": ""}),
                "suffix": ("STRING", {"default": ""}),
                "positive_prompt_1": ("STRING", {"multiline": True, "default": ""}),
                "positive_prompt_2": ("STRING", {"multiline": True, "default": ""}),
                "positive_prompt_3": ("STRING", {"multiline": True, "default": ""}),
                "positive_prompt_4": ("STRING", {"multiline": True, "default": ""}),
                "positive_prompt_5": ("STRING", {"multiline": True, "default": ""}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
            }
        }
        
    RETURN_TYPES = ("CONDITIONING", "CONDITIONING", "CONDITIONING", "CONDITIONING", "CONDITIONING", "CONDITIONING",)
    RETURN_NAMES = (
        "positive_1", 
        "positive_2",
        "positive_3",
        "positive_4",
        "positive_5",
        "negative",
    )
    FUNCTION = "encode"
    CATEGORY = "MultiString Prompts"

    def _process(self, prompt_text, prefix, suffix, enable_prefix, enable_suffix):
        prompt_text = prompt_text.strip()
        
        is_prefix_enabled = (enable_prefix == "true")
        is_suffix_enabled = (enable_suffix == "true")

        prefix_text = prefix.strip() if is_prefix_enabled else ""
        suffix_text = suffix.strip() if is_suffix_enabled else ""

        parts = []
        if prefix_text:
            parts.append(prefix_text)
        
        if prompt_text:
            parts.append(prompt_text)
        
        if suffix_text:
            parts.append(suffix_text)
        
        return ",".join(parts)

    def _encode_prompt(self, clip, prompt):
        if not prompt:
            tokens = clip.tokenize("")
            cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
            return [[cond, {"pooled_output": pooled}]]
            
        tokens = clip.tokenize(prompt)
        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
        return [[cond, {"pooled_output": pooled}]]

    def encode(self, clip, prefix, suffix, enable_prefix, enable_suffix, 
                 positive_prompt_1, positive_prompt_2, positive_prompt_3, 
                 positive_prompt_4, positive_prompt_5, negative_prompt):
        
        p1 = self._process(positive_prompt_1, prefix, suffix, enable_prefix, enable_suffix)
        p2 = self._process(positive_prompt_2, prefix, suffix, enable_prefix, enable_suffix)
        p3 = self._process(positive_prompt_3, prefix, suffix, enable_prefix, enable_suffix)
        p4 = self._process(positive_prompt_4, prefix, suffix, enable_prefix, enable_suffix)
        p5 = self._process(positive_prompt_5, prefix, suffix, enable_prefix, enable_suffix)
        n = self._process(negative_prompt, prefix, suffix, enable_prefix, enable_suffix)

        cond_p1 = self._encode_prompt(clip, p1)
        cond_p2 = self._encode_prompt(clip, p2)
        cond_p3 = self._encode_prompt(clip, p3)
        cond_p4 = self._encode_prompt(clip, p4)
        cond_p5 = self._encode_prompt(clip, p5)
        cond_n = self._encode_prompt(clip, n)
        
        return (cond_p1, cond_p2, cond_p3, cond_p4, cond_p5, cond_n)

NODE_CLASS_MAPPINGS = {
    "MultiStringPromptsEncode": MultiStringPromptsEncode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MultiStringPromptsEncode": "MultiString Prompts Encode"
}